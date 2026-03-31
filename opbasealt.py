op = int(input("fale uma opção enrtre 1 e 2 (retanguro/triagngulo)"))
if op == 1:
    base = float(input("informe a base:"))
    alt = float(input("informe a altura:"))
    arearet = base * alt
    print("a area do retangulo é ", arearet, "cm²")
elif op == 2:
    base = float(input("informe a base:"))
    alt = float(input("informe a altura:"))
    areatri = (base*alt)/2
    print("a area do triangulo é ", areatri, "cm²")
else:
    print("valor incoerente")