class Error(Exception):
    pass  # use this to add empty code


# Every exception class have Error suffix, by convention
# A personalized exception class must inherit from another error class that inherits from Exception
class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Type a number between 0 and 10: '))
        print(x)
        if x > 10:
            raise InputError('Number cannot be greater than 10')
        if x < 0:
            raise InputError('Number cannot be shorter than 0')
        break
    except ValueError:
        print('This is not a number')
    except InputError as exception:
        print(exception)

# try, except, finally, raise
