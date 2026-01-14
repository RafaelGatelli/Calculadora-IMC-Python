nome = input("Digite seu nome: ") 
idade = int(input("Digite sua idade: ")) 
if nome:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é " f"{nome[::-1]}")
    if " " in nome:                          # AQUI AINDA ESTA ERRADO
            print("seu nome tem espaços")   # AQUI AINDA ESTA ERRADO
    else:
            print("Seu nome não tem espaços")
    print(f"Seu nome tem " f"{len(nome)} " f"letras")
    print(f"A primeira letra do seu nome é " f"{nome[0]}") # 0 para achar a ultima letra
    print(f"A ultima letra do seu nome é " f"{nome[-1]}") # -1 para achar a ultima letra
else:
    print("Desculpe, você deixou campos vazios.")

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""