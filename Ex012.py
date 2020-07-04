# Variavel global com porcentagem de desconto de vendedor
v_desc_vend = .05

# Funcao de calculo de desconto de vendedor
def f_aplica_desconto_vendedor(x):
    return(x - (x*v_desc_vend))

v_preco = float(input("Digite o valor do produto: "))
v_preco_desconto = f_aplica_desconto_vendedor(v_preco)

print("Produto com desconto vendedor: {:.2f}".format(
    v_preco_desconto
    )
)


#print(f_aplica_desconto_vendedor(100))
