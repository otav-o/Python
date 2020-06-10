#Create a program that asks the user for a number
#and then prints out a list of all the divisors of
#that number. (If you don’t know what a divisor is,
#it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has
#no remainder.)

numero = int(input("Introduza um número: "))

y = []
x = list(range(1, numero))
for num in x:
    if numero%num==0:
        y.append(num)
y.append(numero) #fica fora do if para não gerar loop
                 #resolve o problema do 1

    
    #elif numero == 1:
        #y.append(numero)
        
if numero == 1:
    print("O único divisor do 1 é ele mesmo!")

else:
    print("Os divisores de", numero, "são:", y)
        


#pode usar tbm o range(1, numero+1)

#concluído!
