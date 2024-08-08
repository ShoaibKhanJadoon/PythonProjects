a = int(input("Enter Number 1:"))
opr = int(
    input("""
Enter 1 for addition
Enter 2 for subtration
Enter 3 for Multiplication
Enter 4 for division
::
"""))
b = int(input("Enter Number 2:"))


def add(a, b):
  return a + b


def sub(a, b):
  return a - b


def mul(a, b):
  return a * b


def div(a, b):
  return a / b


def invalid(a, b):
  return ("Invalid Input", a, b)


operations = {1: add, 2: sub, 3: mul, 4: div}
result = operations.get(opr, invalid)
print(result(a, b))
