# Boletim, uma lista, mostrar as médias, responder sobre as notas
boletim = []
temp = []
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1] + temp[2]) / 2)
    boletim.append(temp[:])
    temp.clear()
    resp = input('Deseja continuar? ').strip()[0]
    if resp in 'Nn':
        break
print('-=' * 15)
print(f'{"No.":<5}', end='')
print(f'{"NOME":<15}', end='')
print(f'{"MÉDIA"}')
for c in range(0, len(boletim)):
    print(f'{c:<5}', end='')
    print(f'{boletim[c][0]:<15}', end='')
    print(f'{boletim[c][3]}')

# parte 2
while True:
    resp = int(input('Mostrar notas de qual aluno?[999 interrompe] '))
    if resp == 999:
        break
    print(f'Notas de {boletim[resp][0]}: {boletim[resp][1]} e {boletim[resp][2]}')
print('FIM')

# Feito!