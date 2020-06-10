# Crie a função escreva(), que mostre o texto com divisórias, deixando de tamanho adaptável

def escreva(txt):
    print('-=' * (len(txt)//2))   # não pode multiplicar sequência por número float
    print(txt)
    print('-=' * (len(txt)//2))


escreva('Bom dia meus amigos da Escola Politécnica de Manaus')
escreva('oi')

# Feito, Ok 