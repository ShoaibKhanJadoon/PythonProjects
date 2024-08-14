class myClass:

  def __init__(self, value):
    self.nbr = value
    print(self.value)

  def show(self):
    print(self.nbr)

  @property  #getter
  def value(self):
    return self.nbr

  @value.setter  #setter
  def setter(self, value):
    self.nbr = value


obj = myClass(10)
#obj.show()
print(obj.value)
obj.setter = 20
obj.show()
print(obj.value)
obj.setter = 30
obj.show()
