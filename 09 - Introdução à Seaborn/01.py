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






