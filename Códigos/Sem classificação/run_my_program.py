
import myprogram3

anoatual = 2019
pode_parar = False

lista_nomes=[]
lista_idades=[]

while pode_parar==False:
    nome = myprogram3.name_question()
    if nome=="parar":
        pode_parar=True
    else:
        lista_nomes.append(nome)
        lista_idades.append(myprogram3.pergunta_idade(anoatual))
        #lista_idades.append(idade)
    
print(nome)
print(lista_nomes)
print(lista_idades)
