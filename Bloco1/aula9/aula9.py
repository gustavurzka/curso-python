# IF,ELSE e ELIF
num1 = input('Digite um número ')
num2 = input('Digite o segundo número')

try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print('ERROR')