class Student:
    def __init__(self,name,marks):
        self.__name =""
        self.__marks=0
    def setname(self, name):
        self.__name =name
    def getname(self):
        print(self.__name)
    def setmarks(self, marks):
        if 0<=marks<=100:
            self.__marks = marks
        else:
            print("Error:Marks should be between 0 and 100")
    def getmarks(self):
        print(self.__marks)
stu=Student("vinay",-45)
stu.setname("vinay")
stu.getname()
stu.setmarks(-45)
stu.getmarks()