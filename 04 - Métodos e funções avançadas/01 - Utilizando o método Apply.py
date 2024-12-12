# Projeto de notas de alunos com método Apply()

#importando bibliotecas
import pandas as pd

dados_alunos = {'Nome': ['Alice', 'Alan', 'Carol', 'Anelise', 'Evelin', 'Davi'],
                'Matematica': [90,85,70,60,100,98],
                'Ciencias': [20,50,70,90,100,98],
                'Portugues': [90,50,70,77,30,100]                
                }

dados_alunos

# DataFrame

df_notas = pd.DataFrame(dados_alunos)
df_notas

# Calculo de Media

def calculo_media(linha):
    return linha[['Matematica','Ciencias','Portugues']].mean()

df_notas['Media'] = df_notas.apply(calculo_media,axis=1)

df_notas