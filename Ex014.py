v_celsius = 0
def f_celsius_to_fahrenheit(v_celsius):
    return( (v_celsius * 1.800) + 32 )

try:
    v_celsius = float(input("Digite a temperatura em C: "))
except:
    print("Valor inválido!")

print("{:.2f} Celsius = {:.2f} Fahrenheit.".format(
        v_celsius,
        f_celsius_to_fahrenheit(v_celsius)
    )
)
