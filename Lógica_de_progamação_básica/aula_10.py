
velocidade = 66
local_carro = 99

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if RADAR_1 < velocidade:
    print("Voce foi multado")
else:
    print("voce nao foi multado")

print("------------")

if RADAR_1 < velocidade and LOCAL_1 <= local_carro:
    print("Voce foi multado")
else:
    print("voce nao foi multado")