class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def getInfo(self):
        strin="Name: "+self.name+" Breed: "+self.breed
        return strin

class A:
    def __init__(self, i):
        self.age = i

    def getId(self):
        return str(self.age)

class B:
    def __init__(self, nam):
        self.name = nam

    def getName(self):
        return self.name

class C(A, B):
    def __init__(self,i, nam,empi):
        A.__init__(self, i)
        B.__init__(self, nam)
        self.empId = empi

    def getInfo(self):
        strin="Name: "+self.getName()+" Age: "+self.getId()
        return strin

class Person:
    def __init__(self, name):
        self.name = name
    def getPersoninfo(self):
        strin="Name: "+str(self.name)
        return strin
    

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def getEmployeeinfo(self):
        strin=self.getPersoninfo()+", Employee ID:"+str(self.employee_id)
        return strin
    
class Manager(Employee):
    def __init__(self, name,employee_id, department):
        super().__init__(name,employee_id)
        self.department = department

    def getManagerinfo(self):
        strin=self.getEmployeeinfo()+", departmentName:"+self.department
        return strin
        

print("Single Inheritance Example ")
d1 = Dog("coopy", "Golden Retriever")
print(d1.getInfo())
print("Multiple Inheritance Example")
c1 = C(28, "raju", 156)
print(c1.getInfo())
print("Multilevel Inheritance Example")
manager = Manager("loki",15,"insurance")
print(manager.getManagerinfo())
