import sys

alunos_nomes = []

with open('nomes_alunos.txt', encoding="utf-8") as f:
    content = f.readlines()

content = [x.strip('\n') for x in content]

for item in content:
    n = item.upper()
    alunos_nomes.append(n)
    
original_stdout = sys.stdout 
with open('nomes_comparacao.py', 'w', encoding="utf-8") as f:  #pode mudar o tipo de arquivo aqui
    sys.stdout = f # Change the standard output to the file we created.
    print(alunos_nomes)
    sys.stdout = original_stdout # Reset the standard output to its original value