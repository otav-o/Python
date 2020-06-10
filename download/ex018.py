# 18 seno, cosseno e tangente

an = float(input('Digite um ângulo '))
from math import sin, tan, cos, radians

angulo = radians(an)
print('''O seno de {} é {:.2f}.
O cosseno, {:.2f}
A tangente vale {:.2f}'''.format(an, sin(angulo), cos(angulo), tan(angulo)))

# feito
