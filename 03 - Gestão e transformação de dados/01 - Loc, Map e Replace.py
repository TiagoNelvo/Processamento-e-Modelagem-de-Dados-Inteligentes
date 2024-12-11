import pandas as pd

# Criando um novo dataframe

dados_frutas = {'fruta':['maçã', 'banana', 'laranja', 'uva'],
                'preço':['1.50', '0.50', '2.20', '0.75'],
                'quantidade':[100, 200, 50, 75]}

dados_frutas
df_frutas = pd.DataFrame(dados_frutas)
df_frutas
print(df_frutas)

df_frutas_2 = df_frutas.iloc[0]
df_frutas_2
df_frutas_3 = df_frutas.iloc[:3]

df_frutas.iloc[2]['fruta']
df_frutas.iloc[0]['quantidade']

# Projeto Cadastro de Pessoas

dados_cadastro = {'nome':['João', 'Maria', 'José','Ana', 'Pedro', 'Alan', 'Carol','Evelyn', 'Laura'],
                  'idade':[20,25,30,35,40,30,24,38,22],
                  'cidade':['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba','Campinas', 'Porto Alegre', 'Rio de Janeiro', 'Rio de Janeiro', 'Rio de Janeiro']
                  }
df_cadastro = pd.DataFrame(dados_cadastro)
df_cadastro

# Media
media_idade = df_cadastro['idade'].mean()
media_idade

# Desvio
desvio_idade = df_cadastro['idade'].std()
desvio_idade

# Soma
soma_idades = df_cadastro['idade'].sum()
soma_idades

# map()

mapeamento_cidade = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Campinas': 'SP',
    'Belo Horizonte': 'MG',
    'Curitiba': 'PR',
    'Porto Alegre': 'RS'
}

mapeamento_cidade

df_cadastro['cidade']
df_cadastro['cidade'] = df_cadastro['cidade'].map(mapeamento_cidade)

df_cadastro['cidade'] = df_cadastro['cidade'].replace('MG', 'Minas Gerais')
df_cadastro['cidade']

df_cadastro['cidade'] = df_cadastro['cidade'].replace('SP', 'São Paulo')
df_cadastro['cidade']

# Group By

df_pessoas_mais_velha = df_cadastro.loc[df_cadastro.groupby('cidade')['idade'].idxmax()]
df_pessoas_mais_velha

