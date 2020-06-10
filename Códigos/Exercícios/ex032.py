# Faça um programa que leia um ano qualquer e diga se ele é bissexto. 2020 é um ano bissexto
ano = int(input('Insira um ano: '))
if ano % 4 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))
# (acima: errado)
# anos bissextos: todo ano divisível por 4, exceto os múltiplos de 100 que não são múltiplos de 400.

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('{} é bissexto.'.format(ano))
        else:
            print('{} não é bissexto.'.format(ano))
    else:
        print('{} é bissexto'.format(ano))
else:
    print('{} não é bissexto'.format(ano))

# simplificado:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))

# São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
# São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
# Não são bissextos todos os demais anos.
# anos bissextos: todo ano divisível por 4, exceto os múltiplos de 100 que não são múltiplos de 400.


# from datetime import date
# ano = date.today().year