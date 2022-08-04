# Verifiar se texto digitado é um número e dizer se é par ou impar
num = input('Digite um número: ')

if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print('Este número é par')
    else:
        print('Este número é impar')
else:
    print('Você não digitou um número')
