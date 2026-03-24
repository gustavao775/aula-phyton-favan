dia = int(input("informe o dia"))
hr = int(input("informe a hora:"))
min = int(input("informe os minutos:"))
seg = int(input("informe os segunos:"))
dhms = (dia * 86400)+(hr * 3600)+(min * 60)+seg

print("o total de segundos é:", dhms)