#def double(x):
#  return x*2


def appl(fx, value):
  return 6 + fx(value)


double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3
apply = lambda x, y, z: x(z) + y(z)
print(double(5))
print(cube(5))
print(avg(3, 5, 10))
#print(appl(lambda x:x*x,2))
print(appl(cube, 10))
print(apply(cube, double, 10))

#map function


def cube(x):
  return x * x * x


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#map(function,iterable)
#newl=map(cube,l)
newl = map(lambda x: x * x * x, l)
print(list(newl))


def filter_data(x):
  return x > 4


#newl=filter(filter_data,l)
newl = filter(lambda x: x > 4, l)
print(list(newl))

#reduce function
from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]  #sum all the values to a single value
sum = reduce(lambda x, y: x + y, l)
print(sum)
