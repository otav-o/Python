# A import does not have file extension (.py)
# import classes
# tv = classes.Television()

# from classes import Television
# tv = Television()


from classes import Television
from methods_and_functions import Calculator, test_method, test_method2

if __name__ == '__main__':
    tv1 = Television()
    print(tv1.on)
    tv1.power()
    print(tv1.on)

    calc = Calculator(10, 25)
    print(calc.sum())

    print(test_method())
    print(test_method2(2))

# lambda = anonymous funcion
char_counter = lambda list: [len(x) for x in list]

animals_list = ['dog', 'cat', 'elephant']
print(char_counter(animals_list))

sum = lambda a, b: a + b
sub = lambda a, b: a - b

calculator = {  # dictionary of lambda functions
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mult': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

print(type(calculator))
print(calculator['sub'](10, 40))
mult = calculator['mult']
print(mult(1, 2))
