# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palídromo: frase de frente para trás lida do mesmo jeito. Ex: 'A sacada da casa' 'Apos a sopa', 'A torre da derrota',
# 'O lobo ama o bolo', 'Anotaram a data da maratona', 'Subi no onibus', 'A base do teto desaba'. Não usar acentos.

frase = input('Escreva uma frase! ').strip().replace(' ', '').upper()
# é possível não digitar o replace: frase.split() e depois ''.join(palavras)

inverso = ''
for letra in range(len(frase) - 1, -1, -1):  # len(frase) - 1 pois há o zero. Ex.: 10 caracteres - vai de 0 a 9.
    # print(frase[letra])     # imprime de trás para frente cada uma das letras.
    inverso = inverso + frase[letra]
print(frase, inverso)
if frase == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Não é um palíndromo.')
# observe o inverso. O programa construiu uma frase nele, adicionando as letras de trás para frente. Fácil.
