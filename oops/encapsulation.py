class Person:
    __val = 5
    val = 6

    def __init__(self):
        self.name = 'Manjula'
        self.__lastname = 'Dube'

    def PrintName(self):
        return self.name + ' ' + self.__lastname


class Man(Person):
    def __init__(self):
        super().__init__()
        print(super().PrintName())
        print(super().val)


class Woman(Person):
    def __init__(self):
        super().__init__()
        print(super().val)


p = Person()
print(p._Person__lastname)
print(p._Person__val)
print(p.val)
m = Man()
w = Woman()