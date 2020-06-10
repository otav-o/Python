# Faça um programa que leia o sexo de uma pessoa, mas só aceite valores "M" ou "F". Caso esteja errado, peça
# a digitação novamente até ter um valor correto.

nome = str(input('Digite seu nome: '))
sexo = input('Digite seu sexo! (M/F) ').lower()
while sexo != 'm' and sexo != 'f':  # and, e não or
    sexo = input('Comando inválido! Digite seu sexo (M/F) ').lower()
print('Informações registradadas!')

# feito.
