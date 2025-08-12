from database import inserir_carro, listar_carros, deletar_carro
import pandas as pd

def cadastrar_novo():
    print('\n--- CADASTRO DE NOVO CARRO ---')
    
    try:
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
            'marca': marca,
            'modelo': modelo,
            'ano': ano,
            'cor': cor,
            'combustivel': combustivel,
            'cambio': cambio,
            'portas': portas
        }
        
        inserir_carro(novo_carro)
        print("\n✅ Carro cadastrado com sucesso!")
    
    except ValueError:
        print("❌ Entrada inválida! Ano e portas devem ser números inteiros.")

def remover_carro():
    df = listar_carros()
    if df.empty:
        return

    try:
        carro_id = int(input("\nDigite o ID do carro que deseja deletar: "))
    except ValueError:
        print("❌ ID inválido! Digite um número inteiro.")
        return
    
    confirmacao = input(f"Tem certeza que deseja deletar o carro ID {carro_id}? (s/n): ").lower()
    if confirmacao != 's':
        print("❌ Operação cancelada.")
        return
    
    linhas_afetadas = deletar_carro(carro_id)
    if linhas_afetadas > 0:
        print(f"\n✅ Carro com ID {carro_id} deletado com sucesso!")
    else:
        print(f"\n⚠ Nenhum carro encontrado com ID {carro_id}.")
