# Desafio 005 : antecessor e sucessor

print('Bem vindo! Digite um número para saber seu antecessor e sucessor inteiros.')

numero = int(input())

print('O antecessor de {} é {} e o sucessor, {}'.format(numero, numero - 1, numero + 1))
print('Os três números formam essa sequência: ({}, {}, {}).'.format(numero - 1, numero, numero + 1))



# Desafio 006 : dobro, triplo e raiz quadrada

d = 2 * numero
t = 3 * numero
rq = numero ** (1/2)

print('''O dobro, triplo e raíz quadrada de {} são,
respectivamente: {}, {} e {:.3f}.'''.format(numero, d, t, rq))



# Desafio 007 : calcular a média entre dois números

print('''Obrigado! Agora insira dois números para eu calcular a
média entre eles''')

n1 = int(input('Qual o primeiro? '))
n2 = int(input('O outro: '))

media = (n1 + n2) / 2

print('A média entre {} e {} é {}'.format(n1, n2, media))
# Extra
print('O primeiro número é {:.3f}% do segundo!'.format(n1 / n2 * 100))



# Desafio 008 : converter um valor de metros para cm e mm

n3 = int(input('Insira um valor em metros '))
cm = n3 * 100
mm = n3 * 1000

print('{}m equivalem a {} cm ou {} mm!'.format(n3, cm, mm))



# Desafio 009 : tabuada de um número inteiro

n4 = int(input('Vamos gerar a tabuada do seguinte número: '))
print('''Aqui está:
{0} * 1 = {0}
{0} * 2 = {1}
{0} * 3 = {2}
{0} * 4 = {3}
{0} * 5 = {4}
{0} * 6 = {5}
{0} * 7 = {6}
{0} * 8 = {7}
{0} * 9 = {8}
{0} * 10 = {9}'''.format(n4*1, n4*2, n4*3, n4*4, n4*5, n4*6, n4*7, n4*8, n4*9, n4*10))
#### Ótimo!



# Desafio 010 : compra de dólares

reais = int(input('Quantos reais você tem? '))
cotação = float(input('Qual o preço do dólar hoje? '))

print('Com o dinheiro da sua carteira, você pode comprar {:.2f} dólares'.format(reais/cotação))

            


# Desafio 011 : latas de tinta

print('Insira as medidas de uma parede para calcular quantas latas de tinta serão necessárias para pintá-la')
altura = float(input('Qual a altura da parede? (em metros) '))
comprimento = float(input('Qual o comprimento? (em metros) '))
área = altura * comprimento
litros_de_tinta = área / 2
latas_de_tinta = litros_de_tinta / 15

print('''A área da parede de dimensões ({} m x {} m) é {}
e, considerando que se gasta 1 litro de tinta a cada 2m²,
e que cada lata possui 15 litros, serão necessárias {}
latas de tinta para pintar essa parede. Considerando as
perdas de 10%, é seguro comprar {} litros, em vez dos {}
litros calculados.'''.format(altura, comprimento, área, latas_de_tinta, litros_de_tinta*1.1, litros_de_tinta))



# Desafio 012 : desconto de 5%

preço = int(input('Digite o preço de um produto: '))
print('Ele custaria R${} se fosse aplicado um desconto de 5%!'.format(0.95*preço))



# Desafio 013 : aumento salarial de 15%
salario = float (input ('Insira o salário: ') )
reajuste = float (input ( 'Quantos por cento foi o reajuste?' ))
print('O novo salário, com reajuste de {}%, é igual a {}.' .format(reajuste, (salario * (1 + reajuste / 100))) )


# Um dia eu volto aqui para corigir a formatação e os números
# 18/02/2020
