'''Desenvolvaa um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digirado o primeiro valor 3
c) Quais foram os números pares'''

'''tupla = ''
par = ''
impar = ''

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    tupla += str(n)
    if n % 2 == 0:
        par += str(n) + ' '
    else:
        impar += str(n) + ' '

n9 = tupla.count(str(9))
if n9 != 0:
    print(f'O 9 aparece {n9} vezes!')
elif n9 == 0:
    print('O número 9 não aparece nessa sequência.')

if str(3) in tupla:
    p3 = tupla.index(str(3))
    print(f'O primeiro 3 aparece na posição {p3}')
elif str(3) not in tupla:
    print(f'O número 3 não foi digitado em nenhum momento.')


print(f'Os números pares são \033[33m{par}\033[m e os ímpares, {impar}')'''

# Completamente errado

print(f'{"Jeito do professor":=^30}')
num = (int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
       int(input('Digite o último: ')))

print(f'O valor 9 apareceu {num.count(9)} vezes!')
if 3 in num:        # essencial para não dar erro
    print(f'O número 3 apareceu pela primeira vez na {num.index(3) + 1}ª digitação.')   # cuidado!

print('Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')

# Ok
