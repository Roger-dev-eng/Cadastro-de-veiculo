import pandas as pd
from sqlalchemy import text
from app import engine

def contar_registros():
    query = "SELECT COUNT(*) FROM fipe_carros"
    with engine.connect() as conn:
        total = conn.execute(text(query)).scalar()
    print(f" Total de registros: {total}")

def top_marcas(limit=10):
    query = f"""
    SELECT marca, COUNT(DISTINCT modelo) AS total_modelos
    FROM fipe_carros
    GROUP BY marca
    ORDER BY total_modelos DESC
    LIMIT {limit};
    """
    df = pd.read_sql(query, engine)
    print("\n Top marcas com mais modelos:")
    print(df.to_string(index=False))
    return df

def media_preco_por_marca():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT column_name FROM information_schema.columns
            WHERE table_name = 'fipe_carros';
        """))
        colunas = [r[0] for r in result]
        if 'marca' not in colunas:
            print(" Nenhum dado encontrado na tabela 'fipe_carros'. Execute novamente a importação FIPE.")
            return

    query = """
    SELECT marca, ROUND(AVG(valor), 2) AS preco_medio
    FROM fipe_carros
    WHERE valor IS NOT NULL
    GROUP BY marca
    ORDER BY preco_medio DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    print(df)

def media_preco_por_combustivel():
    query = """
    SELECT combustivel, ROUND(AVG(valor), 2) AS preco_medio, COUNT(*) AS total
    FROM fipe_carros
    WHERE valor IS NOT NULL
    GROUP BY combustivel
    ORDER BY preco_medio DESC;
    """
    df = pd.read_sql(query, engine)
    print("\n Preço médio por combustível:")
    print(df.to_string(index=False))
    return df

def distribuicao_anos():
    query = """
    SELECT ano_modelo AS ano, COUNT(*) AS total
    FROM fipe_carros
    GROUP BY ano_modelo
    ORDER BY ano_modelo DESC;
    """
    df = pd.read_sql(query, engine)
    print("\n Distribuição de carros por ano:")
    print(df.to_string(index=False))
    return df

def analise_pandas():
    df = pd.read_sql("SELECT * FROM fipe_carros", engine)
    print("\n DataFrame carregado com", len(df), "registros.")

    top = df.sort_values("valor", ascending=False).head(5)
    print("\n Top 5 carros mais caros:")
    print(top[["marca", "modelo", "ano_modelo", "valor"]].to_string(index=False))

    media = df["valor"].mean()
    print(f"\n Preço médio geral: R$ {media:,.2f}")

if __name__ == "__main__":
    contar_registros()
    top_marcas()
    media_preco_por_marca()
    media_preco_por_combustivel()
    distribuicao_anos()
    analise_pandas()
