a = int(input('Type first integer: '))
b = int(input('Second number: '))
sum = a + b
sub = a - b
mult = a * b
divi = a / b

# print('Sum: ' + sum)  # error
print('Sum: ' + str(sum))
print('Sum: {}'.format(sum))  # converts and concatenates automatically
print(type(divi))
print(type(int(divi)))
print(sub)
print(mult)
print(divi)
print(int(divi))

print('Sum: {}. Subtraction: {}'.format(sum, sub))
print('Sum: {summ}. Subtraction: {subs}'.format(subs=sub, summ=sum))


