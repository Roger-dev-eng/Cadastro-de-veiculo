import pandas as pd
from sqlalchemy import create_engine, text

def criar_tabela(engine):
    with engine.connect() as conn:
        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS carros (
            id SERIAL PRIMARY KEY,
            marca VARCHAR(100) NOT NULL,
            modelo VARCHAR(100) NOT NULL,
            ano INTEGER NOT NULL,
            cor VARCHAR(100) NOT NULL,
            combustivel VARCHAR(100) NOT NULL,
            cambio VARCHAR(50) NOT NULL,
            portas INTEGER NOT NULL,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """))
        conn.commit()

def inserir_carro(engine, carro):
    with engine.connect() as conn:
        conn.execute(text("""
        INSERT INTO carros (marca, modelo, ano, cor, combustivel, cambio, portas)
        VALUES (:marca, :modelo, :ano, :cor, :combustivel, :cambio, :portas)
        """), carro)
        conn.commit()

def listar_carros(engine):
    df = pd.read_sql("SELECT * FROM carros", engine)
    if df.empty:
        print("\nNenhum carro cadastrado ainda!")
    else:
        print("\n Todos os Carros Cadastrados ")
        print(df.to_string(index=False))
    return df

def atualizar_carro(engine):
    listar_carros(engine)
    try:
        id_carro = int(input("Digite o ID do carro que deseja atualizar: "))
        valores = {"id": id_carro}

        nova_marca = input("Nova marca (pressione Enter para não alterar): ").strip().title()
        if nova_marca:
            valores["marca"] = nova_marca

        novo_modelo = input("Novo modelo (pressione Enter para não alterar): ").strip().title()
        if novo_modelo:
            valores["modelo"] = novo_modelo

            
        while True:
          try:
            novo_ano = int(input("Novo ano (1801-2025, pressione Enter para não alterar): "))
            if 1800 < novo_ano <= 2025:
                break
            print("Digite um número válido!")
          except ValueError:
              print("ERRO!")
        if novo_ano:
          valores["ano"] = novo_ano        

        nova_cor = input("Nova cor (pressione Enter para não alterar): ").strip().title()
        if nova_cor:
            valores["cor"] = nova_cor

        combustiveis = ['gasolina', 'álcool', 'flex', 'diesel', 'elétrico', 'híbrido']
        novo_combustivel = input("Novo combustível (pressione Enter para não alterar): ").strip().lower()
        if novo_combustivel:
            while novo_combustivel not in combustiveis:
                print(f"Combustível inválido! Escolha entre: {', '.join(combustiveis)}")
                novo_combustivel = input("Novo combustível: ").strip().lower()
            valores["combustivel"] = novo_combustivel

        cambios = ['manual', 'automático', 'automatizado', 'cvt']
        novo_cambio = input("Novo câmbio (pressione Enter para não alterar): ").strip().lower()
        if novo_cambio:
            while novo_cambio not in cambios:
                print(f"Câmbio inválido! Escolha entre: {', '.join(cambios)}")
                novo_cambio = input("Novo câmbio: ").strip().lower()
            valores["cambio"] = novo_cambio

        while True:
          try:
            nova_porta = int(input("Nova porta (2-5, pressione Enter para não alterar): "))
            if 2 <= nova_porta <= 5:
                break
            print("Digite um número válido!")
          except ValueError:
              print("ERRO!")      
        if nova_porta:
          valores["portas"] = nova_porta   

        if len(valores) == 1:
            print("Nenhuma alteração fornecida. Operação cancelada.")
            return

        set_clause = ", ".join(f"{key} = :{key}" for key in valores.keys() if key != "id")
        query = text(f"""
            UPDATE carros
            SET {set_clause}
            WHERE id = :id
        """)
        with engine.connect() as conn:
            resultado = conn.execute(query, valores)
            conn.commit()

            if resultado.rowcount > 0:
                print(f"Carro com ID {id_carro} atualizado com sucesso!")
            else:
                print(f"Carro com ID {id_carro} não encontrado.")

    except ValueError as e:
        print(f"Erro: ID inválido ou entrada numérica incorreta. Detalhes: {e}")
    except Exception as e:
        print(f"Erro ao atualizar carro: {e}")