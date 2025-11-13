import pandas as pd
from sqlalchemy import text
from app import engine

def media_preco_por_marca():
    print("\n Calculando média de preço por marca...")

    query = text("""
        SELECT 
            marca, 
            ROUND(AVG(valor)::numeric, 2) AS preco_medio,
            COUNT(*) AS total_modelos
        FROM fipe_carros
        WHERE valor IS NOT NULL
        GROUP BY marca
        ORDER BY preco_medio DESC
        LIMIT 10;
    """)

    try:
        df = pd.read_sql(query, engine)
        if df.empty:
            print(" Nenhum dado encontrado na tabela 'fipe_carros'. Execute novamente a importação FIPE.")
        else:
            print(df)
        return df
    except Exception as e:
        print(f" Erro ao calcular média de preço por marca: {e}")
        return pd.DataFrame()

def media_preco_por_combustivel():
    print("\n Calculando média de preço por tipo de combustível...")

    query = text("""
        SELECT 
            combustivel, 
            ROUND(AVG(valor)::numeric, 2) AS preco_medio, 
            COUNT(*) AS total
        FROM fipe_carros
        WHERE valor IS NOT NULL
        GROUP BY combustivel
        ORDER BY preco_medio DESC;
    """)

    try:
        df = pd.read_sql(query, engine)
        if df.empty:
            print(" Nenhum dado encontrado na tabela 'fipe_carros'.")
        else:
            print(df)
        return df
    except Exception as e:
        print(f" Erro ao calcular média de preço por combustível: {e}")
        return pd.DataFrame()

def media_preco_por_ano():
    print("\n Calculando média de preço por ano do modelo...")

    query = text("""
        SELECT 
            ano_modelo,
            ROUND(AVG(valor)::numeric, 2) AS preco_medio,
            COUNT(*) AS total
        FROM fipe_carros
        WHERE valor IS NOT NULL
        GROUP BY ano_modelo
        ORDER BY ano_modelo DESC;
    """)

    try:
        df = pd.read_sql(query, engine)
        if df.empty:
            print(" Nenhum dado encontrado na tabela 'fipe_carros'.")
        else:
            print(df)
        return df
    except Exception as e:
        print(f" Erro ao calcular média de preço por ano: {e}")
        return pd.DataFrame()
