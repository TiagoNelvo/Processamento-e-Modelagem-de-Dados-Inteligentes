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

import pandas as pd
import matplotlib.pyplot as plt

vendas_scatter = pd.DataFrame({'Vendas':[100,150,200,250,300,350,400,450,500],
                               'Gastos com publicicdade':[50,75,80,100,110,130,150,170,190],
                               'Média de Preço':[20,22,23,25,27,28,30,32,33]})


vendas_scatter

#Matplot

plt.scatter(x='Gastos com publicicdade',y='Média de Preço',cmap='Blues',data=vendas_scatter)
plt.title('Relação entre gastos com publicade e vendas')
plt.xlabel('Gastos com publicidade (em milhares de reais)')
plt.ylabel('Vendas (em unidades)')
plt.colorbar().set_label('Média de preço (em reais)')
plt.show()

#Seaborn

sns.scatterplot(x='Gastos com publicicdade',y='Média de Preço',cmap='Blues',data=vendas_scatter)
plt.title('Relação entre gastos com publicade e vendas')
plt.xlabel('Gastos com publicidade (em milhares de reais)')
plt.ylabel('Vendas (em unidades)')
plt.show()



#Exemplo Seaborn

horas_estudads = [1,2,3,4,5,6,7,8,9,10]
nota_obtida = [10,55,65,72,80,85,90,95,98,100]
sns.scatterplot(x=horas_estudads, y=nota_obtida)
plt.title('Relação entre horas estudadas e nota obtida')
plt.xlabel('Horas estudadas')
plt.ylabel('Nota Obtida')
plt.show()


