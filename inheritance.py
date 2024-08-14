
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def show(self):
    print(f"The name is {self.name} and age is {self.age}")

class Employee(Person):
  def __init__(self,name,id,age):
    super().__init__(name,age)
    self.__id = id

  def showdetails(self):
    print(f"The name of Employee: {self.name} id is {self.__id}")

e=Employee("shoaib khan",125,22)
#print(e.__id) #private variable donot accessible directly
#print(e._Employee__id) #you can access them using Name Mangling
e.show()
e.showdetails()


