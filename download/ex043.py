# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# - Abaixo de 18.5: abaixo do peso;
# - Entre 18.5 e 25: peso ideal;
# - 25 até 30: Sobrepeso;
# - 30 até 40: Obesidade;
# - Acima de 40: Obesidade mórbida.
# Fórmula: peso (em kg) dividido pela altura (em metros) ao quadrado

altura = float(input('Calculadora de IMC! Digite sua altura em metros. '))
peso = float(input('Agora nos diga o seu peso em quilogramas: '))
IMC = peso/(altura ** 2)
if IMC < 18.5:
    print('Você está \033[36mabaixo do peso!\033[m Seu IMC é de {:.2f}'.format(IMC))
elif IMC > 18.5 and IMC < 25:   # Exemplo de outra forma
    print('Você está com o \033[32mpeso ideal\033[m para a sua altura. Seu IMC é de {:.2f}'.format(IMC))
elif 25 < IMC < 30:
    print('Você está com \033[35msobrepeso\033[m! Seu IMC é de {:.2f}'.format(IMC))
elif 30 < IMC < 40:
    print('Seu status é de \033[34mOBESIDADE\033[m. IMC = {:.2f}'.format(IMC))
elif 40 < IMC:
    print('Você está com \033[31mOBESIDADE MÓRBIDA\033[m. IMC = {:.2f}'.format(IMC))

# feito. ok