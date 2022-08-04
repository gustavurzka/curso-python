# Verificar se o nome digitado é longo, normal ou curto
nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif 5 <= len(nome) <= 6:
    print('seu nome é Normal')
else:
    print('seu nome é muito grande')
