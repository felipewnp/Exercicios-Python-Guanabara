# Inicialização variáveis de configuração
v_valor_diaria = 60
v_valor_km = 0.15

# Inicialização variáveis de input
v_diaria = v_km = 0

# Função retorna cálculo do aluguel do veículo para modalidade diaria + km
def f_calcula_diaria_km(v_diaria,v_km):
    return((v_diaria * v_valor_diaria) + (v_km * v_valor_km))

# Input float dos dados com try-except
try:
    v_diaria = float(input("Digite o número de diárias: "))
    
    if v_diaria < 1:
        raise

    v_km = float(input("Digite o número de KMs percorrido: "))
except:
    print("Valor inválido!")
    exit()

print("Seu aluguel custa: {:.2f}.".format(
    f_calcula_diaria_km(v_diaria, v_km)
    )
)
