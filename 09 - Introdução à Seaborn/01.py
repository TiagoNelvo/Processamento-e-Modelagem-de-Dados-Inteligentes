# Introdução a Seaborn

import seaborn as sns
import pandas as pd
import numpy as np

notas = np.random.normal(loc=70, scale=10,size=100)

notas

dados = pd.DataFrame({'Notas': notas})

dados

sns.kdeplot(data=dados['Notas'],fill=True)

























