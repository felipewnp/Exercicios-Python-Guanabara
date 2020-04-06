try:
    num = float(input("Digite um número: "))
except:
    print("Valor inválido!")
    exit()

print("{}".format(int(num)))
