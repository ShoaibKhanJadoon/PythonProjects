class vector:
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k

  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
  def __add__(self,x):
    return vector(self.i+x.i,self.j+x.j,self.k+x.k)

v=vector(1,2,3)
print(v)

v2=vector(1,2,3)
print(v2)
print(v+v2) #add function between vector class is overloded
