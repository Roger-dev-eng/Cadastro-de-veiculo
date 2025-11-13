import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from CRUD.database import criar_tabela, listar_carros, atualizar_carro
from CRUD.cadastro import cadastrar_novo, remover_carro

load_dotenv(dotenv_path="config/.env")

def menu_principal():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("Variável DATABASE_URL não encontrada no arquivo .env")

    engine = create_engine(database_url)
    criar_tabela(engine)
    
    while True:
        print('\n=== MENU PRINCIPAL ===')
        print('1. Ver carros cadastrados')
        print('2. Cadastrar novo carro')
        print('3. Atualizar carro')
        print('4. Deletar carro')
        print('5. Sair')
        
        opcao = input('\nEscolha uma opção (1-5): ')
        
        if opcao == '1':
            listar_carros(engine)
        elif opcao == '2':
            cadastrar_novo(engine)
        elif opcao == '3':
            atualizar_carro(engine)
        elif opcao == '4':
            remover_carro(engine)
        elif opcao == '5':
            print("\nPrograma encerrado. Até logo!")
            break
        else:
            print("\nOpção inválida! Digite um número de 1 a 5")

if __name__ == "__main__":
    menu_principal()
