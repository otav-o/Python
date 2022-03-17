list = [1, 10, 4]
file = open('text.txt', 'r')

try:
    division = 10 / 1
    number = list[2]
    x = a
except ZeroDivisionError:
    print('It\'s not possible to divide by zero')
except IndexError:
    print('There is a problem with your index')
except BaseException as ex:
    print('Unknown error: {}'.format(ex))
else:
    print('Else executes when there is no exception')
finally:
    print('This is always executed')
    file.close()
# This is a tree, and you should start from specific to general exceptions

# https://docs.python.org/3/library/exceptions.html
