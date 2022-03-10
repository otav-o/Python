class Television:
    def __init__(self):
        self.on = False
        self.channel = 0

    def power(self):
        if self.on:
            self.on = False
        else:
            self.on = True

    def increase_channel(self):
        self.channel += 1

    def decrease_channel(self):
        if self.channel > 0:
            self.channel -= 1


print(__name__)  # __name__ is the module that calls execution.

if __name__ == '__main__':
    tv = Television()
    print(tv.on)
    tv.power()  # method, not function
    print(tv.on)
    tv.power()
    print(tv.on)

    print(tv.channel)
    tv.increase_channel()
    print(tv.channel)
