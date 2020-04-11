from random import choice
from sys import maxsize
#from random import randint

# Inicialização de variáveis.
alunos = []
nome = ""
i = 0

# Inicializa maxlistsize como tamanho máximo de int no sistema
maxlistsize = maxsize - 1

# Loop, de tamanho maxlistsize, de inserção de dados.
while i < maxlistsize+1:
    nome = str(input("Digite o nome do aluno: ")) # Adiciona input como string em nome.
    #nome = str(randint(-9223372036854775808,9223372036854775806)) # Teste.
    alunos.append(nome) # Adiciona nome na lista alunos.
    i += 1  # Incrementa +1 no contador i.
    if alunos[-1] == "end": # Se último nome inserido em alunos == end:
        alunos.pop() # Deleta último valor inserido.
        break # Encerra o loop.
    if alunos[-1] == "": # Se último nome inserido em alunos for blank:
        alunos.pop() # Deleta último valor inserido.
        i -= 1 # Decrementa -1 no contador i.
        print("Valor inválido")

if alunos:
    print(choice(alunos)) # Escolhe um elemento da lista
else:
    print("Nenhum nome na lista!")
