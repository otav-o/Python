# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar;
# [2] multiplicar;
# [3] maior;
# [4] novos números;
# [5] sair do programa.
# Seu programa deverá realizar a operação solicitada em cada caso.
# loop até o usuário encerrar o programa.

resp = 4
while resp == 4:
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo: '))
    resp = 9    # gambiarra???

    while resp != 5:
        print('-=' * 20)
        print(''' MENU
O que você deseja fazer com esses dois números?
[1] somar;
[2] multiplicar;
[3] maior;
[4] novos números;
[5] sair do programa.''')
        print('-=' * 20)

        resp = int(input('Sua resposta: '))

        if resp == 1:
            print(f'A soma de {n1} + {n2} é {n1 + n2}!!')
            perg = input('Deseja continuar? (S/N) ').lower()
            if perg == 's':
                resp = 9
            else:
                resp = 5

        elif resp == 2:
            print(f'{n1} vezes {n2} é igual a {n1 * n2}.')
            perg = input('Deseja continuar? (S/N) ').lower()
            if perg == 's': resp = 9
            else: resp = 5

        elif resp == 3:
            maior = 0   # tem que definir as variáveis de fora para dentro.
            if n1 > n2:
                maior = n1
            elif n2 > n1:
                maior = n2
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
            perg = input('Deseja continuar? (S/N) ').lower()
            if perg == 's':
                resp = 9
            elif perg == 'n':
                resp = 5
        elif resp == 4:
            print('')



    print('Você terminou o programa! Tchau.')

# meu deus que dor de cabeça
