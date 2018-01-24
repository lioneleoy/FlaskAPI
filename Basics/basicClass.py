class test:
    def __init__(self):
        self.name ="lionel"
        self.age = 25
        self.numbers= (1,2,3,4,5)

    def total(self):
        result = sum(self.numbers)
        return result


test1 = test()

print test1.total()