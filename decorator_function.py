def decorator(function1):

  def wraper(
      *args, **kwargs
  ):  #*args take all the arguments as tuple and **kwargs take all the arguments as dictionary
    print("welcome")
    function1(*args, **kwargs)
    print("executed")

  return wraper


#usnig notation
#@decorator
def hello():
  print("hello world")


def add(a, b):
  print(a + b)


#manually called
decorator_hello = decorator(hello)
decorator_hello()
#hello()

addition = decorator(add)(12, 12)
