# Funcao que recebe cateto_oposto, cateto_adjacente e retorna o cálculo da hipotenusa.
def hip(co, ca):
    try:
        return( ((co**2)+(ca**2)) ** 0.5)
    except:
        print ("Valor inválido!")

# Lê os valores co e ca do usuário e aciona except caso seja <=0
try:
    co = float(input("Digite o valor do cateto oposto: "))
    if co <=0: raise
    ca = float(input("Digite o valor do cateto adjacente: "))
    if ca <= 0: raise
except:
    print("Valor inválido!")
    exit()

print(hip(co,ca))
