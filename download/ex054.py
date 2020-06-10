# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores. Considerar 21 anos.

s = 0
z = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    from datetime import date
    if date.today().year - ano >= 21:
        s = s + 1   # s += 1
    else:
        z = z + 1   # z += 1

print('{} pessoas ainda não atingiram a maioridade, e {} já são maiores.'.format(z, s))

# funciona perfeitamente!
# análise de dados