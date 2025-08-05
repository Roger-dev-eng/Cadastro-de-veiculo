import pandas as pd
dados={
    'Nome':["Maria", "Pedro", "João", "Marcos","Alice"],
    'Idade':[12, 46, 72, 38, 57],
    'Cidade':["SP", "RJ", "TE", "RE", "GO"]
}
df=pd.DataFrame(dados)
df['Profissão'] = ['Professor', "Médico", "Jornalista", "Motorista", "CEO"]#Adicionar uma coluda
ordenado=df.sort_values('Idade', ascending=True)#Colocar em ordem crescente(true) ou descrescente(False)
print(ordenado)