temp = int(input('Informar a tempetura: '))
TEMP_MAX = 15

if temp < TEMP_MAX:
    print("Sistema de Refrigeração na faixa segura")
elif temp > 25:
    print("sistema precisa ser Desligado")
else:
    print("verificar o sistema de refrigeração")
