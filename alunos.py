# importing module
from pandas import *
 
todos_dados = []
lista_alunos = []

# reading CSV file
ano = 2020
for i in range(3):
    documento = 'aluno ' + str(ano) + '.csv'
    ano = ano + 1
    data = read_csv(documento)
    
    # converting column data to list
    lattes = data['lattes'].tolist()
    cota = data['cota_mec'].tolist()
    situacao = data['situacao'].tolist()
    nome = data['nome'].tolist()
    curso = data['curso'].tolist()
    matricula = data['matricula'].tolist()
    linha_pesquisa = data['linha_pesquisa'].tolist()
    cota_sistec = data['cota_sistec'].tolist()
    campus = data['campus'].tolist()
        
    nomes = []
    for item in nome:
        n = item.upper()
        nomes.append(n)
    
    
    # printing list data
    a = 0
    for n in nome:
        aluno = []
        aluno.append(nomes[a])
        aluno.append(situacao[a])
        a = a + 1
        todos_dados.append(aluno)
        
        
for d in range(len(todos_dados)):
    lista_alunos.append(todos_dados[d][0]) 
    