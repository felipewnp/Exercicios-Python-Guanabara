# importa funções necessárias da biblioteca math
from math import radians, sin, cos, tan

# Inicialização das variáveis
v_sen = v_cos = v_tan = 0
v_dic_angulo = {}

# Função retorna dicionário com calculo de sen, cos e tan a partir de angulo
def calcula_angulo(v_angulo):
    v_angulo = radians(v_angulo)
    v_dic_angulo["sen"] = sin(v_angulo)
    v_dic_angulo["cos"] = cos(v_angulo)
    v_dic_angulo["tan"] = tan(v_angulo)
    return v_dic_angulo

# Função recebe dicionário, varre e imprime sen, cos, tan
def imprime_angulo(v_dic_angulo):
    for chave, valor in v_dic_angulo.items():
        print("{} = {}".format(
            chave,
            valor
        ))

# input do angulo
v_angulo = float(input("Digite um angulo: "))

# imprime calculo do angulo
imprime_angulo(calcula_angulo(v_angulo))
