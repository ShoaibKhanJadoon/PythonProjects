def name(name=""):
  """
    Print the Name
    user defined module
  """
  if name == "":
    print("welcome")
  else:
    print(f"welcom {name}")
def print_name():
  print(__name__)
if __name__=="__main__":
  name()