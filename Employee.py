class Employee:
    def __init__(self,name,salary,age):
        self.__name=name
        self.__salary=salary
        self.__age=age
    def setname(self,name):
        self.__name=name
    def getname(self):
        print(self.__name)
    def setsalary(self,salary):
        if salary>0:
            self.__salary=salary
        else:
            print("Error:Salary must be greater than 0.")
    def getsalary(self):
        print(self.__salary)
    def setage(self,age):
        if 18<=age<=100:
            self.__age=age
        else:
            print("Age must be between 18 and 100")
    def getage(self):
        print(self.__age)
emp=Employee("vinay",20000,20)
emp.setname("vinay")
emp.getname()
emp.setsalary(20000)
emp.getsalary()
emp.setage(18)
emp.getage()
