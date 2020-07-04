# Dolar price in brl
usd = 5.22

def brl_usd(brl):
    return (brl / usd)

brl = float(input("Digite o valor em BRL: "))

print("Você pode comprar USD {}".format(brl_usd(brl)))
