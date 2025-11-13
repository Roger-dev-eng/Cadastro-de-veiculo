from CRUD.database import inserir_carro, listar_carros, atualizar_carro
import pandas as pd
from sqlalchemy import text

def cadastrar_novo(engine):
    print('\n--- CADASTRO DE NOVO CARRO ---')
    

    marca = input('Marca do veículo: ').strip().title()
    modelo = input('Modelo do veículo: ').strip().title()

    while True:
      try:
        ano = int(input('Ano de fabricação (1801-2025): '))
        if 1800 < ano <= 2025:
          break
        print("Digite um número válido!")
      except ValueError:
         print("ERRO!")  
        
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

    while True:
      try:    
        portas = int(input('Número de portas (2-5): '))
        if 2 <= portas <= 5:
          break
        print("Número de portas inválido!")
      except ValueError:
         print('ERRO!')  
        
    novo_carro = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'cor': cor,
        'combustivel': combustivel,
        'cambio': cambio,
        'portas': portas
    }
        
    inserir_carro(engine, novo_carro)
    print("\n Carro cadastrado com sucesso!")

def remover_carro(engine):
    df = listar_carros(engine)
    if df.empty:
        return

    try:
        carro_id = int(input("\nDigite o ID do carro que deseja deletar: "))
    except ValueError:
        print(" ID inválido! Digite um número inteiro.")
        return
    
    confirmacao = input(f"Tem certeza que deseja deletar o carro ID {carro_id}? (s/n): ").lower()
    if confirmacao != 's':
        print(" Operação cancelada.")
        return
    
    with engine.connect() as conn:
        resultado = conn.execute(text("DELETE FROM carros WHERE id = :id"), {"id": carro_id})
        conn.commit()
        if resultado.rowcount > 0:
            print(f"\n Carro com ID {carro_id} deletado com sucesso!")
        else:
            print(f"\n Nenhum carro encontrado com ID {carro_id}.")