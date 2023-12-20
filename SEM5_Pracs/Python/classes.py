# simple class and a object
# class Student:
#     a = 10

# kreena = Student()
# print(kreena.a)

# __init__ , self
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def printName(self):
#         print(self.name)
#     def printAge(self):
#         print(self.age)

# person1 = Person("Kreena",20)
# print(person1.name)
# print(person1.age)
# person1.printName()
# person1.printAge()

# Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printName(self):
        print(self.name)
    def printAge(self):
        print(self.age)

class Student(Person):
    def __init__(self,name,age,cake):
        super().__init__(name,age)
        self.cake = cake

x = Student("kreena",20,"chocolate")
print(x.name)
print(x.age)
print(x.cake)
x.printName()
x.printAge()
