# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

print('\033[34m-=\033[m' * 18)
print('CONTAGEM REGRESSIVA PARA O ANO NOVO!')
print('\033[31m-=\033[m' * 18)
for c in range(10, -1, -1):
    print(c)
    from time import sleep
    sleep(1)
print('-=' * 12, 'FELIZ ANO NOVO!', '-=' * 12)

# ótimo ok