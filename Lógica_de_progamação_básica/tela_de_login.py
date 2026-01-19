
print("CRIE UM USER_NAME E SENHA")
user_name = input("Digite seu user_name: ")
senha =  input("Digite sua senha: ")

if user_name and senha:
    print("Você criou seu user_name e senha")
else:
    print("Você esqueceu de digitar seu user_name e/ou sua senha, Tente Novamente!")

user_name_criado = input("Digite seu user_name: ")
senha_criada =  input("Digite sua senha criada: ")

if user_name == user_name_criado and senha == senha_criada:
    print("Parabens, login efetuado!")
else:
    print("user_name e/ou senha incorretos, tente novamente!")