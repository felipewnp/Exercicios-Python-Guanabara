def imprime_tabuada(x,y):
    i = 0
    while i < (y+1):
        print("| {:2.2f} x {:2} = {:2.2f} |".format(x, i, x * i))
        i += 1

numero = float(input("Digite um número: "))

imprime_tabuada(numero,10)