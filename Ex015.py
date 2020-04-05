# Inicialização variáveis de configuração.
v_valor_diaria = 60
v_valor_km = 0.15

# Inicialização variáveis de input.
v_diaria = v_km = 0

# Função retorna cálculo do aluguel do veículo para modalidade diaria + KM.
def f_calcula_diaria_km(v_diaria,v_km):
    return((v_diaria * v_valor_diaria) + (v_km * v_valor_km))

# Input float dos dados com try-except.
try:
    # Recebe float da quantidade de diárias com o carro.
    v_diaria = float(input("Digite o número de diárias: "))    
    # Se o valor da diária for menor que 1, abre except e fecha o programa.
    if v_diaria < 1:
        raise
    # Recebe float da quantidade de KM com o carro.
    v_km = float(input("Digite o número de KMs percorrido: "))
except:
    print("Valor inválido!")
    exit()

# Imprime o resultado chamando a função de cálculo de diárias + KM.
print("Seu aluguel custa: {:.2f}.".format(
    f_calcula_diaria_km(v_diaria, v_km) # Passar diárias, KM para a função.
    )
)
