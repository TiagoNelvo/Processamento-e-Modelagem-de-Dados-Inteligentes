# Algoritmos e redes neurais

# Random Forest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

num_alunos = 1000
faixa_idade = (16,30)
faixa_nota = (2.0,4.0)
faixa_horas_estudo = (1,20)
areas_formacao = ['Ciência da Computação','Engrenharia','Matemática','Física']

alunos = []
for i in range(num_alunos):
    idade = np.random.randint(faixa_idade[0],faixa_idade[1]+1)
    nota = np.random.uniform(faixa_nota[0], faixa_nota[1])
    horas_estudo = np.random.randint(faixa_horas_estudo[0],faixa_horas_estudo[1]+1)
    area_formacao = np.random.choice(areas_formacao)
    alunos.append({'idade':idade,'nota':nota,'horas_estudo':horas_estudo,'area_formacao':areas_formacao})


df_alunos = pd.DataFrame(alunos)

df_alunos

df_alunos.to_csv('dados_alunos.csv',index=False)

df_alunos['desempenho'] = ['alto' if x >= 70 else 'baixo' for x in df_alunos['nota']]

df_alunos

# Treinamento

X = df_alunos[['idade','nota','horas_estudo']]
y = df_alunos['desempenho']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= 0.2, random_state=420)

modelo_rf = RandomForestClassifier(n_estimators=100)

modelo_rf.fit(X_train,y_train)

# Teste

score = modelo_rf.score(X_test,y_test)
print('A exatidão do modelo é: ',score)





# Gradient Boosting




# Introdução a Redes Neurais Artificiais




# Avaliação de Modelos de Aprendizado de Máquina

















