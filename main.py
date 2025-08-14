from sqlalchemy import create_engine
from database import criar_tabela, listar_carros, atualizar_carro
from cadastro import cadastrar_novo, remover_carro

def menu_principal():
    engine = create_engine('sqlite:///cadastro_carros.db')
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
            print("\n🚪 Programa encerrado. Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Digite um número de 1 a 5")

if __name__ == "__main__":
    menu_principal()