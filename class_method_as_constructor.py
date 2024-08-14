
class person:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def show(self):
    print(f"The name of employee is {self.name} and id is {self.id}")

  @classmethod
  def from_string(cls,string):
    name=string.split("-")[0]
    id=int(string.split("-")[1])
    return cls(name,id)

p1=person(name="shoaib",id=125)
p1.show()

p2=person.from_string("shoaib-125")
p2.show()






