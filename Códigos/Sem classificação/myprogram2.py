name = "John"


def name_question():
    global name
    name = input("What`s your name? ")
    print('Your name is "'+name+'"')
    return name

#name_question()



def pergunta_idade():
    
    #Para saber a idade da pessoa
    
    #1 perguntar em que ano ela nasceu
    anonascimento = int(input ("Que ano você nasceu? "))
    anoatual = int(input ("Em que ano estamos? ")) 
    idade = anoatual - anonascimento
    
    #imprimir na tela a idade calculada
    ##print("Você tem " + str(idade), "anos")
    print (name+", você tem ", idade, " anos")
    
