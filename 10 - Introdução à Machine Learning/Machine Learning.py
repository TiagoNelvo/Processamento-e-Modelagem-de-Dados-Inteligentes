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



# 04 - K-NN



# 05 - Árvores de Decisão



