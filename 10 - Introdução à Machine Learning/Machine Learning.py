# 01 - Introdução ao Aprendizado de Máquina

# Aprendizado de Máquina e IA

import numpy as np
from sklearn.linear_model import LogisticRegression

altura = [1.60,1.75,1.68,1.80,1.62,1.65,1.90,1.85]
peso = [55,70,60,75,58,62,85,80]
sexo = ['Feminino','Masculino','Feminino', 'Masculino', 'Feminino','Feminino','Masculino','Masculino']

modelo = LogisticRegression()

X = np.array(list(zip(altura,peso)))
y = np.array(sexo)

modelo.fit(X,y)

nova_amostra = np.array([[1.50,54]])
decisao = modelo.predict(nova_amostra)

if decisao[0] == 'Feminino':
    print('Provavelmente é uma mulher')
else:
    print('Provavelemente é um homem')

#alterando a amostra
nova_amostra = np.array([[1.90,78]])
decisao = modelo.predict(nova_amostra)

if decisao[0] == 'Feminino':
    print('Provavelmente é uma mulher')
else:
    print('Provavelemente é um homem')


# 02 - Aprendizado Supervisionado e Não-Supervisionado

#salvando arquivo csv

import csv

vendas = [{'produto': 'Produto A', 'quantidade':10,'preco':100.00},
          {'produto': 'Produto B', 'quantidade':5,'preco':50.00},
          {'produto': 'Produto C', 'quantidade':8,'preco':80.00},
          {'produto': 'Produto D', 'quantidade':12,'preco':120.00},
          {'produto': 'Produto E', 'quantidade':13,'preco':130.00},          
          ]

with open('Vendas.csv', mode='w',newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['produto','quantidade','preco'])
    for venda in vendas:
        writer.writerow([venda['produto'],venda['quantidade'],venda['preco']])


# 03 - Regressão Linear e Logística

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#abrindo o arquivo
dados = pd.read_csv('vendas.csv')

dados

#gerando modelo
X = dados[['quantidade','preco']]
modelo = KMeans(n_clusters=3)
modelo.fit(X)

dados['cluster'] = modelo.labels_

dados

cores = ['red','blue','green']
for i in range(3):
    plt.scatter(X[dados['cluster'] == i ]['quantidade'],X[dados['cluster'] == i]['preco'],color=cores[i])
plt.xlabel('Quantidade de produtos')
plt.ylabel('Preço')
plt.show()    


# 04 - K-NN

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

comprimento = [1.4,1.3,1.5,4.7,4.5,4.9,5.1,6.0,5.8,6.6,6.9,5.7,6.3,6.1]
largura = [0.2,0.3,0.1,1.4,1.5,1.5,1.8,2.5,2.3,2.1,2.3,2.8,2.5,2.8]
classe = ['setosa','setosa','setosa','versicolor','versicolor','versicolor','versicolor',
         'virginca','virginca','virginca','virginca','virginca','virginca','virginca']

comprimento
largura
classe

df_flores =  pd.DataFrame({'comprimento': comprimento, 'largura': largura, 'classe':classe})

df_flores

modelo = KNeighborsClassifier(n_neighbors=3)

X = df_flores[['comprimento','largura']]
y = df_flores['classe']
modelo.fit(X,y)

nova_amostra = [[5.0,2.0]]
previsao = modelo.predict(nova_amostra)

print('A nova flor pertence à classe: ',previsao[0])

#alterando a amostra
nova_amostra = [[6.0,2.4]]
previsao = modelo.predict(nova_amostra)

print('A nova flor pertence à classe: ',previsao[0])


# 05 - Árvores de Decisão



