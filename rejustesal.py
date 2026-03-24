sal = float(input("informe o salario Ex: #####.## "))
reaj = float(input("informe o reajuste em %:"))

reajsal = sal * ((reaj / 100) + 1)
print("seu novo salario é:", reajsal)