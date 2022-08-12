"""# Repetições e laços
---x = 0
while x < 100:
    print(x)
    x= x + 1

print('Acabou')"""

while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número')
        continue

    #+ - / *
    if operador == '+':
        print(int(num1) + int(num2))
    elif operador == '-':
        print(int(num1) - int(num2))
    elif operador ==  '/':
        print(int(num1) / int(num2))
    elif operador == '*':
        print(int(num1) * int(num2))





