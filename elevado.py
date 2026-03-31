capacidademax = float(input("informe qual a capacidade de peso no elevado:"))
peso1 = float(input("informe o peso da preimeira pessoa em kg:"))
peso2 = float(input("informe o peso da segunda pessoa em kg:"))
peso3 = float(input("informe o peso da terceira pessoa em kg:"))
peso4 = float(input("informe o peso da quarta pessoa em kg:"))
peso5 = float(input("informe o peso da quinta pessoa em kg:"))

pesototal = peso1 + peso2 + peso3 + peso4 + peso5

if pesototal > capacidademax:
    print("o pesso de foi excedido", pesototal,"kg")
elif pesototal < capacidademax:
    print("o peso ta suave patrão")
else:
    print("ta no limite o peso ai irmao")