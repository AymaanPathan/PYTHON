# __init_  is basically a constructor

class Person:
    def __init__(self,name):  # constructor
        self.name = name
        self.age =12
    def info(self):  # function
        print(f"{self.name} is a {self.age} Old" )
    

person1 = Person("Aymaan")
person2 = Person("bob")
person1.info()
person2.info()