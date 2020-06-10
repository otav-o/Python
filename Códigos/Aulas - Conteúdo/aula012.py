# Condições aninhadas
# if, elif, else
nome = input('Qual é o seu nome? ')
if nome == 'Otávio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Prazer em te conhecer, \033[34m{}!'.format(nome))

