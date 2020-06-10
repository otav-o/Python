# Estrutura if / else
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Seu carro está novo! Continue com ele.')
if 3 < tempo <= 5:
    print('Você já está um bom tempo com ele. Mas ele deve ter as últimas tecnologias')
if tempo > 5:
    print('Está na hora de trocar o seu carro. {} anos é bastante.'.format(tempo))
# else:
# print('vai dar erro')

# Estrutura simplificada
print('Carro novo') if tempo <= 3 else print('Carro velho')

nome = str(input('Qual é o seu nome? '))
if nome == 'Otávio':
    print('Que nome bonito você tem!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if 6 <= m < 7:
    print('Foi o suficiente para passar, mas está ruim.')
elif 7 <= m < 10:
    print('Excelente!')
else:
    print('Você foi reprovado, sinto muito.')