def media(x, y):
    return (x+y)/2

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

print("A média entre {:.1f} e {:.1f} é {:.1f}".format(nota1, nota2, media(nota1, nota2)))
