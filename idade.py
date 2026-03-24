nome = str(input("informe seu nome: "))
nasc = int(input("informe ano de nascimento: "))
hoje = int(input("informe ano atual: "))
idade = hoje - nasc
print("olá, %s" % nome)
print("você possui em torno de %d anos de idade" % idade)
