# Formatação de Strings
nome = 'Gustavo'
idade = 23
altura = 1.80
e_maior = idade > 18
peso = 99
imc = peso / (altura * altura)

print(f'{nome} tem {idade} anos de idade seu imc é {imc:.1f}')
print('{} tem {} anos de idade e seu imc é {}'.format(nome, idade, imc))
