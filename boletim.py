import pandas as pd

alunos = {
            'Nome':['Everton', 'Gabriel', 'Julio', 'Rafael'],
            'Nota':[5, 4, 7, 9],
            'Situação Final':['Recuperação', 'Reprovado', 'Aprovado', 'Aprovado']
         }

dataframe = pd.DataFrame(alunos)
print(dataframe)
