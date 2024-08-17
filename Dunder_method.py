class Employee:

  def __init__(self, name, id):
    self.name = name
    self.id = id

  def __len__(self):
    return len(self.name)

  def __str__(self):
    return f"The name of employee is {self.name} and id is {self.id}"

  def __repr__(self):
    return f"Employee('{self.name},{self.id}') "
  def __call__(self):
    print("Hey I am good")

e = Employee(name="shoaib", id=125)
print(len(e))
print(e)  #withoout __str__ method give error
#if str not found than jump to repr method
print(str(e))
print(repr(e))
e() #cal method calls the object as method


