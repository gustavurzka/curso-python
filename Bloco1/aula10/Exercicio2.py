# Perguntar a hora e fazer a saudação correta
num = input('Digite a hora: ')

if num.isnumeric():
    num = int(num)
    if 0 <= num <= 11:
        print('Tenha um bom dia')
    elif 12 <= num <= 17:
        print('Tenha uma ótima tarde')
    elif 18 <= num <= 23:
        print('Tenha uma ótima noite')
    else:
        print('Você provavelmente não está na Terra')
else:
    print('Você não digitou um número válido')

