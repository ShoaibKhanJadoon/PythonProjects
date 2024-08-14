
class Math:
  def __init__(self,num):
    self.num = num
    print(self.num)
  def addtonum(self,n):
    self.num = self.num + n
    print(self.num)
  @staticmethod
  def add(a,b):
    return a+b

m=Math(10)
m.addtonum(10)
print(m.add(20,30))


print(Math.add(10,30))






