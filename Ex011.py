# Recebe altura e largura e retorna a área
def f_area(altura, largura):
    return(altura*largura)

# Recebe uma área e retorna litros de tinta para pintar área
def f_litros_tinta(area):
    return(area/2)

altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = f_area(altura, largura)
litros_tinta = f_litros_tinta(area)

print("Para pintar uma parede com área de {}m² são necessários {} litros de tinta.".format(
    area, 
    litros_tinta
    )
)
