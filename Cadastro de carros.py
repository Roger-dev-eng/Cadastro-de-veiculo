import pandas as pd

tabela=pd.DataFrame(columns=['Marca','Modelo','Ano','Cor','Combustível','Câmbio','Portas'])

print('---CADASTRO DE NOVOS CARROS---')
print('Informe os dados do veículo:')

marca=str(input('Marca do veículo: '))

modelo=str(input('Modelo do veículo: '))

ano=0
while True:
  try:
    ano=int(input('Ano de fabricação (a partir de 1886): '))
    if ano>=1886:
      break
    else:
      print('Ano inválido! Digite uma no válido apartir de 1886.')
  except ValueError:
    print('Digite um número válido!')

cor=str(input('Cor do veículo: '))

combustiveis=['gasolina', 'elétrico', 'diesel', 'etanol', 'gnv', 'flex']

while True:
  print('Tipos de combustível válidos: Gasolina, Elétrico, Diesel, Etanol, GNV, Flex')
  combustivel=str(input('Tipo de combustível:'))
  if combustivel in combustiveis:
    break
  else:
    print('Combustível inválido! Digite um tipo válido para o território brasileiro.')

cambios=['manual', 'automático', 'cvt', 'automatizado']
while True:
  print('Tipos de câmbio válidos: Manual, Automático, CVT, Automatizado')
  cambio=str(input('Tipo de câmbio: '))
  if cambio in cambios:
    break
  else:
    print('Tipo de câmbio inválido!')

porta=0    
while True:
  try:
    porta=int(input('Números de porta (2-5): '))
    if (porta>=2) and (porta<=5):
      break
    else:
      print('Digite um número de portas válidos')
  except ValueError:
    print('Digite um número válido!')

carro = {
  'Marca': marca,
  'Modelo': modelo,
  'Ano': ano,
  'Cor': cor,
  'Combustível': combustivel,
  'Câmbio': cambio,
  'Portas': porta
}

tabela = pd.concat([tabela, pd.DataFrame([carro])], ignore_index=True)
    
print(tabela)