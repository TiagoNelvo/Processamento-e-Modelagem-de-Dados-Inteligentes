# Introdução a Seaborn

# Gráficos de Densidade e Distribuição

import seaborn as sns
import pandas as pd
import numpy as np

notas = np.random.normal(loc=70, scale=10,size=100)

notas

dados = pd.DataFrame({'Notas': notas})

dados

# Gráfico
sns.kdeplot(data=dados['Notas'],fill=True)

# Gráficos de Joinplot


altura = np.random.normal(loc=175,scale=10,size=100)
largura = np.random.normal(loc=70,scale=10,size=100)

altura
largura

dados_joint = pd.DataFrame({'Altura': altura, 
                            'Largura': largura})

dados_joint

# Gráfico

sns.jointplot(x='Altura', y='Largura', data=dados_joint, kind='kde',color='blue')

# Gráficos de Categorização e Relacionamento

dados_vendas = {'Produto':['Produto A', 'Produto B', 'Produto C', 'Produto D'],
                'Vendas Janeiro':[1000,1500,800,1200],
                'Vendas Fevereiro':[1200,1700,900,1300],
                'Vendas Março':[1100,1600,1000,1400]}

dados_vendas

df_vendas = pd.DataFrame(dados_vendas)

df_vendas

# Gráfico

sns.set_style('whitegrid')
sns.barplot(x='Produto',y='Vendas Fevereiro', data=df_vendas)

# Gráfico de Scatterplot












