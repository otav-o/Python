print('\33[7:30mOlá, mundo!\033[m')

print('\033[0;30mEsse texto está branco\033[m')
print('\033[1;30mBranco e negrito\033[m')
print('\033[1;31;47mNegrito, vermelho, fundo cinza.\033[m')
print('\033[4;32mEste texto está sublinhado e verde\033[m')

print('\033[0;34;40mEsse texto está azul com fundo branco\033[m')
print('\033[7;34;40mEsse texto está branco com fundo azul\033[m')

a = 3
b = 5
print('Os valores são \033[35m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Otávio'
print('Muito prazer em te conhecer, {}{}{}!!'.format('\033[34;40m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'azulebranco': '\033[34;40m',
         'pretoebranco': '\033[7;30m'}

print('Olá, {}{}{}, é muito bom te ver!'.format(cores['azulebranco'], nome, cores['limpa']))
# obs.: cores['']
