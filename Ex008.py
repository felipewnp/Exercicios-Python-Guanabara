def m_cm(x):
    return (x*100)
def m_mm(x):
    return(x*1000)

metros = float(input("Digite um número em metros: "))

print("{:.3f} metros = {:.3f} centimetros = {} milimetros".format(metros, m_cm(metros), m_mm(metros)))
