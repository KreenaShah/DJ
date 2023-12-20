# Classes: Employee, Developer, Tester, Manager.
# Developer, tester, Manager inherit Employee.
# Manager handles Developer, tester.
# Manager class: implement functions to add Developer/Tester and Remove Developer/ 
# Tester.
# Display to see the list of employees he manages.

class Employee:
    def __init__(self,name,id,type):
        self.name = name
        self.id = id
        self.type = type

class Manager(Employee):
    def __init__(self,name,id,type):
        super().__init__(name,id,type)

class Developer(Employee):
    def __init__(self,name,id,type):
        super().__init__(name,id,type)

class Tester(Employee):
    def __init__(self,name,id,type):
        super().__init__(name,id,type)

empObj = Employee("labdhi",1)
print(empObj.name)
print(empObj.id)
managerObj = Manager("labdhi",1)
print(managerObj.name)
print(managerObj.id)
