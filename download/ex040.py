# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# média abaixo de 5.0: REPROVADO
# média entre 5 e 6.9: RECUPERAÇÃO
# acima de 7: APROVADO

print('Calculadora de média! Insira suas notas do boletim.')
nome = str(input('Para começar, qual é o seu nome? '))
n1 = float(input('{}, digite o primeiro resultado: '.format(nome)))
n2 = float(input('Digite a nota da segunda prova: '))
print('Calculando...')
from time import sleep
sleep(2)
media = (n1 + n2)/2
if media < 5:
    print('\033[31m{}, você foi REPROVADO! Infelizmente sua média foi de apenas {:.1f}.\033[m'.format(nome.upper(), media))
elif 5 < media < 6.9:
    print('\033[33m{} vocÊ está de RECUPERAÇÃO! Estude mais. Seu rendimento foi de apenas {:.1f} pontos.\033[m'.format(nome.upper(), media))
else:
    print('\033[32mParabéns, {}! Você foi APROVADO com rendimeto de {:.1f}%!\033[m'.format(nome, media * 10))

# feito ok