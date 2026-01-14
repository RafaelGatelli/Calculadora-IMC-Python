nome= input("Digite seu nome: ")
idade= input("Digite sua idade: ")

letras = len(nome)
p_letra = nome[0]
u_letra = nome[-1]


if nome and idade:
    print(f"Seu nome é  {nome}")
    print(f"Seu nome invertido é " f"{nome[::-1]}")
    print(f"Seu nome tem {letras} letras")

    if " " in nome:
        print("Seu nome tem espaços")

    else:
        print("Seu nome não tem espaços")
        
    print(p_letra)
    print(u_letra)

else:
    print("Desculpe, você deixou campos vazios.")

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome} ok
        Seu nome invertido é {nome invertido} ok
        Seu nome contém (ou não) espaços ok 
        Seu nome tem {n} letras ok 
        A primeira letra do seu nome é {letra} ok
        A última letra do seu nome é {letra} ok
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""