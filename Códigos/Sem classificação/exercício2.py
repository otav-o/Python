#Ask the user for a number. Depending on whether the number is
#even or odd, print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when
#divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num)
#and one number to divide by (check). If check divides evenly
#into num, tell that to the user. If not, print a different
#appropriate message.

numero = int(input("Digite um número: "))
resto = numero%2
if resto == 0:
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")

#desafio extra
    
num = int(input("Digite outro: "))
check = int(input("Insira um número para dividir o anterior: "))

resto == num%check
if resto == 0:
    frase = " é"
else:
    frase = " não é"

print(str(num)+frase+" divisível por "+str(check))

#concluído!

        
