# Iterando strings com while
frase =  'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

maiscula = input('Qual letra vc quer colocar em maiúscula? ')

while contador < len(frase):
    letra = frase[contador]
    if letra == maiscula:
        nova_string += maiscula.upper()
    else:
        nova_string += letra

    contador += 1

print(nova_string)


