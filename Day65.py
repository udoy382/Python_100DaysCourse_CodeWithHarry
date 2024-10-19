# Static Methods in Python


class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod # `self` not required if we use `staticmethod` in our function.
    def add(a, b):
        return a + b


# result = Math.add(1, 2)
# print(result) # Output 3


a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
