v_percentual_reajuste = .15
v_salario = 0

# Retorna valor do salario reajustado com percentual definido em v_percentual_reajuste
def f_reajuste_salario(v_salario):
    return(v_salario * (v_percentual_reajuste + 1)) # Adiciona +1 no percentual para retornar reajuste + salario

# Retorna o valor do reajuste do salário com percentual definido em v_percentual_reajuste
def f_valor_reajuste(v_salario):
    return(v_salario * v_percentual_reajuste)

# Recebe um salário, se não for numérico, apresenta erro.
try:
    v_salario = float(input("Digite o salario: "))
except:
    print("Valor inválido!")

# Armazena salario reajustado
v_salario_reajustado = f_reajuste_salario(v_salario)

# Armazena valor do reajuste
v_reajuste = f_valor_reajuste(v_salario)


if v_salario > 0:
    print("O salário de {:.2f} com reajuste de {:.2f} passa a ser {:.2f}".format(
        v_salario,
        v_reajuste,
        v_salario_reajustado        
    )
)
