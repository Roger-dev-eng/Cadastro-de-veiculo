from database import criar_tabela, listar_carros
from cadastro import cadastrar_novo, remover_carro

def menu_principal():
    criar_tabela()
    
    while True:
        print('\n=== MENU PRINCIPAL ===')
        print('1. Ver carros cadastrados')
        print('2. Cadastrar novo carro')
        print('3. Sair')
        print('4. Deletar carro')  
        
        opcao = input('\nEscolha uma opção (1-4): ')
        
        if opcao == '1':
            listar_carros()
        elif opcao == '2':
            cadastrar_novo()
        elif opcao == '3':
            print("\n🚪 Programa encerrado. Até logo!")
            break
        elif opcao == '4':
            remover_carro()
        else:
            print("\n❌ Opção inválida! Digite um número de 1 a 4")

if __name__ == "__main__":
    menu_principal()
