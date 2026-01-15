
"""
SUPONHA QUE TODOS MESES TENHAM 30 DIAS
E HOJE É DIA 14/01/2026!
"""

nome = input("Digite seu nome: ")
print("Digite apenas NÚMEROS NAS PROXIMAS RESPOSTAS")
dia = int(input("Digite o dia que nasceu: "))
mes = int(input("Digite o mês que nasceu: "))
ano = int(input("Digite o ano que nasceu: "))

anos = (2025 - ano)
nasceu_meses = anos * 12
nasceu_dias = nasceu_meses * 30
nasceu_segundos = nasceu_dias * 86400

if nome and dia and mes and ano:
    print(f"Bem-vindo(a) {nome}!")
    print(f"Você tem {anos} anos")
    print(f"Você nasceu a " f"{nasceu_meses} meses")
    print(f"Você viveu " f"{nasceu_dias} dias")
    print(f"E se passaram " f"{nasceu_segundos:,.0f} segundos des do seu nascimento")

print(" ")

if dia >= 14:
    dias = dia - 14
if dia < 14:
    dias = 16 + dia
    
if mes > 1:
    meses = mes - 1   
    print(f"Faltam {meses} meses para seu aniversario!")
if mes == 1:
    meses = 12
    print(f"Faltam {meses} meses para seu aniversario!")

dias_meses = meses*30
dias_ani = dias_meses + dias
seg_ani = dias_ani * 86400
print(f"ou {dias_meses + dias} dias...")
print(f"ou tambem {seg_ani:,.0f} segundo")


