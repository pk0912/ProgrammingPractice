class Overloading:
    def __init__(self):
        self.a = 5

    def method1(self):
        print("method1 without args")

    def method1(self, b):  # This can result in error
        print(self.a)
        print(b)


overloading = Overloading()
overloading.method1()  # TypeError: method1() missing 1 required positional argument: 'b'
overloading.method1(10)
