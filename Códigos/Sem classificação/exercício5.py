#Take two lists, say for example these two:

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#and write a program that returns a list that contains
#only the elements that are common between the lists
#(without duplicates). Make sure your program works on
#two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you
#can’t figure this out at this point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elemento in a:
    if elemento in b:
        c.append(elemento)
print(c, "são os elementos comuns a 'a' e 'b'")

#até aqui, perfeito: "[1, 1, 2, 3, 5, 8, 13] são os elementos comuns a 'a' e 'b'"
#mas há a repetição do número 1

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elemento in a:
    if elemento in b:
       if elemento not in c: #resolvida a repetição
          c.append(elemento)


print(c, "são os elementos comuns a 'a' e 'b'")




#tentando o extra
     
import random
a1 = random.sample(range(1,25),7)
a1.sort()
a2 = random.sample(range(2,35),10)
a2.sort()
a1a2 = []

if len(a1)> len(a2):
    for elemento in a1:
        if elemento in a2:
            a1a2.append(elemento)
else:
    for elemento in a2:
        if elemento in a1:
            a1a2.append(elemento)

print("A primeira lista aleatória é", a1)
print("A outra é:", a2)

if len(a1a2) == 1:
    print(a1a2, "é o elemento comum")
else:
    print(a1a2, "são os elementos comuns") 


#não fiz em uma só linha
#fim
            
