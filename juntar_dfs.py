#*************CRIAR UM ARQUIVO CSV COM OS DADOS DOS SERVIDORES E ALUNOS COM BASE NOS NOMES EM COMUM***************
import pandas as pd

# ler os arquivos csv e armazená-los em um dataframe
df_servidores = pd.read_csv('C:\\Users\\palmo\\OneDrive\\Documentos\\MONYK PAOLA\\LAPES\\RASPAGEM DE DADOS\\Z COPIAR NO GIT\\Rondonopolis_raspagem.csv')
df_alunos = pd.read_csv('C:\\Users\\palmo\\OneDrive\\Documentos\\MONYK PAOLA\\LAPES\\RASPAGEM DE DADOS\\Z COPIAR NO GIT\\alunos_ifmt.csv')


df_alunos = df_alunos.rename(columns={'nome': 'nome_aluno'})

# unir os dataframes com base na coluna 'nome'
df_combinado = pd.merge(df_servidores, df_alunos[['lattes','situacao','nome_aluno','curso','matricula','campus']], left_on='nome', right_on='nome_aluno', how='left')

# salvar o dataframe unido em um arquivo csv
df_combinado.to_csv('servidores_alunos_rondonopolis.csv', index=False)