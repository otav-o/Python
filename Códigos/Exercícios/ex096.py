# Criar função area() para calcular a superfície de um terreno.

def area(c, l):
    a = c * l
    return a


print('Calculadora de áreas!')
n = float(input('Digite o comprimento: '))
n2 = float(input('Largura: '))
print(f'Esse terreno tem {area(n, n2)}m².')

# Feito, ok