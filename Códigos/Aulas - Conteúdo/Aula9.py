frase = 'oi, bom dia'

print(frase[9])  # posição do caractere
print(frase[3:7])  # 3 a 7, excluindo o último
print(frase[1:11:2])  # de 1 a 11, saltando de 2 em 2
print(frase[:5])  # de zero a 5, incluindo ele(???)
print(frase[5:])  # de 5 até o final
print(frase[9::3])  # de 9 ao final, exibindo de 3 em 3

#   Análise
print(len(frase))
print(frase.count('o'))  # analisa uma string e conta quantas vezes ela aparece
print(frase.count('o', 0, 5))
print(frase.find('bom'))  # indica onde a string está ou começa
print(frase.find('Android'))  # -1
print('bom' in frase)

#   Transformação
print(frase.replace('dia', 'android'))  # função replace substitui o primeiro pelo segundo
print(frase.upper())  # deixa tudo em maiúsculo
print(frase.lower())  # deixa tudo minúsculo
print(frase.capitalize())  # tudo minúsculo, só o caractere zero fica maiúsculo
print(frase.title())  # capitaliza palavra por palavra
frase2 = '      a   dsfja  ajsocc ad      '
print(frase2.strip)  # remove os espaços inúteis
print(frase2.rstrip)  # remove os espações inúteis à direita
print(frase2.lstrip)  # remove os espaços inúteis à esquerda
print(frase.split())  # divisão onde houver espaços, cria uma lista

#   Junção
print(
    '-'.join(frase))  # string ponto join frase. Não substituiu os espaços por traço, e sim separou as letras por traço
print(frase)

###

frase3 = 'Curso em Vídeo Python'
print(frase3.count('o'))  # contou somente os minúsculos
print(frase3.upper().count('O'))  # conta todos os 'o's
print('curso' in frase3)
print('curso' in frase3.lower())
print(
    frase3.find('Curso'))  # diz-se que a string é imutável pois ela só é alterada se for atribuído um novo valor a ela.
frase3 = frase3.replace('Python', 'Android')    # frase3 mudou de valor a partir dessa linha
print(frase3)   # 'Curso em Vídeo Android'
print(frase3.split())
dividido = frase3.split()
print(dividido[0])  # mostra o elemento zero da lista
print(dividido[2][3])   # d (letra 3 do elemento 2)
