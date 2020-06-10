#Create a program that asks the user to
#enter their name and their age. Print out
#a message addressed to them that tells them
#the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking
#the user for another number and printing
#out that many copies of the previous message.
#(Hint: order of operations exists in Python)
#Print out that many copies of the previous
#message on separate lines. (Hint: the string
#"\n is the same as pressing the ENTER button)




nome = str(input("Qual é o seu nome? "))
idade = int(input ("Quantos anos você tem? "))
ano_nascimento = 2019 - idade
ano100 = ano_nascimento + 100
print("Olá "+nome+", você tem "+str(idade)+" anos e, no ano "+str(ano100)+", sua idade será 100 anos")

número = int(input("Agora diga um número "))
print((" "+nome)*número)


#excelente!!
