# A Confederação Nacional de Natação precisa d eum programa que leia o ano de nascimento de um atleta e mostre a sua
# categoria, de acordo com a idade:
# até 9 anos: MIRIM;
# até 14: INFANTIL;
# até 19 anos: JUNIOR;
# té 20: SÊNIOR;
# acima: MASTER.
nasc = int(input('Em que ano o nadador nasceu? '))
from datetime import date
atual = date.today().year
idade = atual - nasc
print('A idade é de {} anos.'.format(idade))
if idade < 9:
    print('Categoria MIRIM!')
elif idade < 14:    # não precisa colocar que é maior do que 9
    print('Categoria INFANTIL.')
elif idade < 19: print('Categoria JUNIOR')
elif idade < 20: print('Categoria SÊNIOR')
else: print('Categoria MASTER.')

# feito.