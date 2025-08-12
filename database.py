import pandas as pd
from sqlalchemy import create_engine, text

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

def deletar_carro(carro_id):
    with engine.connect() as conn:
        resultado = conn.execute(text("DELETE FROM carros WHERE id = :id"), {"id": carro_id})
        conn.commit()
        return resultado.rowcount