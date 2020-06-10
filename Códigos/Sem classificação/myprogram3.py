name = "John"


def name_question():
    global name
    name = input("What`s your name? ")
    print('Your name is "'+name+'"')
    return name

def pergunta_idade(anoatual):
    
    #perguntar o ano que ela nasceu
    anonascimento = int(input ("Que ano você nasceu? "))
    #subtrair do ano atual

    idade = anoatual - anonascimento
    
    #imprimir na tela a idade calculada
    ##print("Você tem " + str(idade), "anos")
    print (name+", você tem ", idade, " anos")
    
    return (idade, anoatual)
    
