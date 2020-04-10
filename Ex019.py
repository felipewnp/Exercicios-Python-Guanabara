from random import choice, randint

alunos = []
nome = i = 0

#while i < 99999+1:
while True:
    nome = str(input("Digite o nome do aluno: "))
    #nome = str(randint(-9223372036854775808,9223372036854775806))
    alunos.append(nome)
    i += 1 
    if alunos[-1] == "end":
        alunos.pop()
        break
    if alunos[-1] == "":
        alunos.pop()
        print("Valor inválido")

print(choice(alunos))
