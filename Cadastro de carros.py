import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime

# Conexão com o banco SQLite
engine = create_engine('sqlite:///cadastro_carros.db')

def criar_tabela():
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS carros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            combustivel TEXT NOT NULL,
            cambio TEXT NOT NULL,
            portas INTEGER NOT NULL,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """))
        conn.commit()

def inserir_carro(carro):
    with engine.connect() as conn:
        conn.execute(text("""
        INSERT INTO carros (marca, modelo, ano, cor, combustivel, cambio, portas)
        VALUES (:marca, :modelo, :ano, :cor, :combustivel, :cambio, :portas)
        """), carro)
        conn.commit()

def listar_carros():
    df = pd.read_sql("SELECT * FROM carros", engine)
    if df.empty:
        print("\nNenhum carro cadastrado ainda!")
    else:
        print("\n🚗 Todos os Carros Cadastrados 🚗")
        print(df.to_string(index=False))
    return df

def cadastrar_novo():
    print('\n--- CADASTRO DE NOVO CARRO ---')
    
    marca = input('Marca do veículo: ').strip().title()
    modelo = input('Modelo do veículo: ').strip().title()
    ano = int(input('Ano de fabricação: '))
    cor = input('Cor do veículo: ').strip().title()
    
    combustiveis = ['gasolina', 'álcool', 'flex', 'diesel', 'elétrico', 'híbrido']
    combustivel = input(f"Combustível ({'/'.join(combustiveis)}): ").lower()
    while combustivel not in combustiveis:
        print("Combustível inválido!")
        combustivel = input(f"Digite um combustível válido ({'/'.join(combustiveis)}): ").lower()
    
    cambios = ['manual', 'automático', 'automatizado', 'cvt']
    cambio = input(f"Câmbio ({'/'.join(cambios)}): ").lower()
    while cambio not in cambios:
        print("Câmbio inválido!")
        cambio = input(f"Digite um câmbio válido ({'/'.join(cambios)}): ").lower()
    
    portas = int(input('Número de portas (2-5): '))
    while portas < 2 or portas > 5:
        print("Número de portas inválido!")
        portas = int(input('Digite um número entre 2 e 5: '))
    
    novo_carro = {
        'Marca': marca,
        'Modelo': modelo,
        'Ano': ano,
        'Cor': cor,
        'Combustível': combustivel,
        'Câmbio': cambio,
        'Portas': portas
    }
    
    inserir_carro(novo_carro)
    print("\n✅ Carro cadastrado com sucesso!")

def menu_principal():
    criar_tabela()
    
    while True:
        print('\n=== MENU PRINCIPAL ===')
        print('1. Ver carros cadastrados')
        print('2. Cadastrar novo carro')
        print('3. Sair')
        
        opcao = input('\nEscolha uma opção (1-3): ')
        
        if opcao == '1':
            listar_carros()
        elif opcao == '2':
            cadastrar_novo()
        elif opcao == '3':
            print("\n🚪 Programa encerrado. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Digite 1, 2 ou 3")

if __name__ == "__main__":
    menu_principal()