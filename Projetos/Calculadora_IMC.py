print("USE APENAS NUMEROS INTEIROS, SEM DECIMAIS")
print("EXEMPLO: 170 PARA ALTURA E 60 PARA PESO")

print(" ")

nome = input("Qual seu nome? ")
altura = input("Qual sua altura? ")
peso = input("Qual seu peso? ")

altura = int(altura)/100
altura_2 = (altura * altura)
peso = int(peso)
IMC = peso / altura_2

linha_1 = f"{nome}, você tem {altura:.2f}m de altura,"
linha_2 = f"está pesando {peso} quilos e seu IMC é"
linha_3 = f"{IMC:.2f}"

print(linha_1, linha_2, linha_3)

# (nome) tem (altura) de altura,
# pesa (peso) quilos e seu IMC é
# IMC

if IMC < 18.5:
    a = "peso muito baixo!"
elif 18.5 <= IMC < 24.4:
    a = "peso normal!"
else:
    a = "sobrepeso!"

resultado = f"Você está com {a}"
print(resultado)



