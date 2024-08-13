

class myClass:
  def __init__(self,value):
    self.value=value
    print(self.value)
  def show(self):
    print(self.value)
  @property #getter
  def getter(self):
    return self.value
  @getter.setter
  def setter(self,value):
    self.value=value

obj =myClass(10)
#obj.show()
print(obj.getter)
obj.setter=20
obj.show()
print(obj.getter)
obj.setter=30
obj.show()