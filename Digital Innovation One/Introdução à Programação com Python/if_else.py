a = int(input('First value: '))
b = int(input('Second value: '))
c = int(input('Third value: '))

if a > b and a > c:  # and, not &&
    print('Higher number is {}'.format(a))
elif b > a and b > c:
    print('Higher number is {}'.format(b))
else:
    print('Higher number is {}'.format(c))

print('End of execution')


# ---

a = int(input('Type a number: '))
b = int(input('Type another number: '))

remainder_a = a % 2
remainder_b = b % 2

if remainder_a == 0 or remainder_b == 0 or not remainder_b > 0:
    print('An even number was typed!')
else:
    print('There is not an even number here')
