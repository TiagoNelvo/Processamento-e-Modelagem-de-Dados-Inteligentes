# Projeto de Câmbio Financeiro

import pandas as pd

# Criando conjunto de dados

dados_cambio = {'Produtos': ['Produto A', 'Produto B', 'Produto C'],
                'Preço USD': [100,150,200],
                'Preço EUR': [85,125,170],
                'Preço JPY': [10000,15000,20000]
                }

dados_cambio

#dataFrame
df_cambio = pd.DataFrame(dados_cambio)
df_cambio

# Criar função para converter o câmbio

def conversao_para_usd(preco,taxa):
    return preco / taxa

taxa = {'USD':1, 'EUR':1.2, 'JPY':0.009}

taxa

conversao_para_usd