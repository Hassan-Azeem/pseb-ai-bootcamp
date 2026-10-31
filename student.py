class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hi, I am", self.name)
        print("My age is", self.age)

    def set_age(self, age):
        self.age = age

s = Student("Hassan", 22)
s.greet()
