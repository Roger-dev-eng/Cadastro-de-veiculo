from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv(dotenv_path="config/.env")

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(" Variável DATABASE_URL não encontrada no arquivo .env!")

engine = create_engine(DATABASE_URL)

print(" Conexão com banco inicializada (via app.__init__)")
