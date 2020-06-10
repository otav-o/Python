#Take a list, say for example this one:

    # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the
#elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one,
#make a new list that has all the elements
#less than 5 from this list in it and print
#out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list
#that contains only elements from the original
#list a that are smaller than that number given
#by the user.



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #lista

#for element in a:
#    print(element)


#### print([aa for aa in a if aa < 5])  UAU

b = []
for element in a:
    if element < 5:
        #print(element)
        #b = []
        b.append(element)

print(b)

c = []
numero = int(input("Digite um número: "))
for element in a:
    if element < numero:
        #c = []
        c.append(element)
        print(c)



        
