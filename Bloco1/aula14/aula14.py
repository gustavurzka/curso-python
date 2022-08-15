# Contadores e acumuladores
contador = 0
acumulador = 0

while contador <= 10:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
else:
    print('Cheguei no else')