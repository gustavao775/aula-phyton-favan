print("escolha um:")
print("lata de oleo-1")
print("caixa de papelão-2")
escolha = int(input())
if escolha == 1:
    raio = float(input("informe um dos raios da circunferencia da lata de oleo: "))
    h = float(input("informe a altura da lata em cm: "))
    volume = 3.141592 * raio**2 * h
    print("o volume é ", volume, "cm³")
elif escolha == 2:
    alt = float(input("informe a altura da caixa: "))
    comp = float(input("informe o comprimento da caixa: "))
    larg = float(input("informe a largura da caixa: "))
    volumecaixa = alt * comp * larg
    print("o volume da caixa é ", volumecaixa, "cm³")
else:
    print("valor incoerente")
    