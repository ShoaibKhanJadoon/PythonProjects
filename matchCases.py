x = int(input("Enter Number Between 1 to 100 :"))

match x:
  case 0:
    print("x is zero")
  case 10:
    print("value is 10")
  case _ if x < 0:
    print("X is Negative")

  case _ if x > 100:
    print("X is Greater than 100")
