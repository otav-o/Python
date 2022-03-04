# for, while, range

for x in range(100):
    print(x)

for x in range(50, 60):  # prints 50-59
    print(x)


# ---

def isPrime(number):
    div = 0
    for n in range(1, number + 1):
        remainder = number % n
        if remainder == 0:
            div += 1

    if div == 2:
        return True
    else:
        return False


a = int(input('Enter a number: '))

if isPrime(a):
    print('Number {} is prime'.format(a))
else:
    print('Number {} is NOT prime'.format(a))

# ---

primes = []
print('Prime numbers 0-100:')
for num in range(101):
    if isPrime(num):
        primes.append(num)

print(primes)
