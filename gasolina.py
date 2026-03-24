preco_gas = float(input("Diga o valor da gasolina atualmente em reais:" ))
rend_car = float(input("Diga quanos Km seu carro faz por litro de gasolina: "))
km_rodado = float(input("Diga quantos Km vc rodou: "))

litros = km_rodado / rend_car
valor = litros * preco_gas

print("Você ira precisar de", litros, "litro(s) de gasolina para rodar.")
print(f"E isso lhe custará", valor,"reais.")