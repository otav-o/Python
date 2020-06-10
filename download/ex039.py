# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar;
# Se é hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo

idade = int(input('Qual a sua idade? '))
if idade < 18:
    print('Jovem, faltam {} anos para o seu alistamento!'.format(18 - idade))
elif idade == 18:
    print('\033[31mEstá na hora de se alistar! Compareça a uma junta do Exército.\033[m')
else:
    print('Fique traquilo! O momento do seu alistamento foi há {} anos.'.format(idade - 18))


# um pouco diferente
ano = int(input('Em que ano você nasceu? '))
from datetime import date
atual = date.today().year
if atual < ano + 18:
    print('Jovel, faltam {} anos para o seu alistamento, pois você tem {} anos!'.format(ano + 18 - atual, atual - ano))
elif atual > ano + 18:
    print('Seu alistamento foi há {} anos.'.format(ano - atual - 18))
elif atual == ano + 18:
    print('Aliste-se imediatamente! Você tem {} anos.'.format(atual - ano + 18))

# errado