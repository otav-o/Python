a=[2, 5, 9, 1]
a[2] = 3   #[2, 5, 3, 1]

a.append(8)  #[2, 5, 3, 1, 8]  só adiciona um de cada vez

a.sort() #[1, 2, 3, 5, 8]

a.sort(reverse = True) #[8, 5, 3, 2, 1]

# append: adiciona ao final da lista => x.append("oi")
# insert: adiciona em uma posição => x.insert(3, "oi")
        # inserir em uma posição que extrapola a lista faz o elemento
        # ... ocupar a posição seguinte à da lista (última + 1).

a.insert(0, 7) #[7, 8, 5, 3, 2, 1]

a.insert(155, 0) #[7, 8, 5, 3, 2, 1, 0]

# o que acontece se eu inserir uma string e depois ordenar a lista?

a.append("oi")
#a.sort() #deu erro

#três maneiras de remover um item: del x [2] -> remove na posição
#                                  x.pop() -> remove o último ou na posição
#                                  x.remove("oi") -> remove o elemento

a.remove("oi")
a.sort(reverse = True) #[8, 7, 5, 3, 2, 1, 0]

del a [2] #[8, 7, 3, 2, 1, 0]

a.insert(2, 5) #[8, 7, 5, 3, 2, 1, 0]

a.pop(2) #[8, 7, 3, 2, 1, 0]

a.pop() #[8, 7, 3, 2, 1]

a.append(8) #[8, 7, 3, 2, 1, 8]

a.remove(8) #[7, 3, 2, 1, 8]

if 5 in a:
    a.remove(5)
else:
    print("Não tem 5 para remover")

print("O tamanho dessa lista é de " + str(len(a))+ " elementos. ")

print(a)




#
##
###

#criar uma lista

valores = []

valores.append(2)
valores.append(5)
valores.append("s") #ok

#valores.insert("oi",2) #erro, aparentemente não aceita str

for v in valores:
    print(v)
    
print(valores)















