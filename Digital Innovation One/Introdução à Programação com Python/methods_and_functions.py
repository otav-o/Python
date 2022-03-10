class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2


if __name__ == "__main__":
    calc = Calculator(10, 2)
    print(calc.num1, calc.num2)
    print(calc.sum(), calc.subtraction())


class Calculator2:
    # def __init__(self):
    #     pass

    def sum(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b


if __name__ == '__main__':
    calc2 = Calculator2()
    print(calc2.sum(20, 5))
    print(calc2.subtraction(20, 5))


def test_method():
    return 'Test 1'


def test_method2(a):
    return 'Test 2 {}'.format(a)
