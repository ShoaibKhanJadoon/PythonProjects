import os


def clear_clutter(path, type):
  """Take path and type as input and clear the clutter type=.txt .pdf .png etc"""
  files = os.listdir(path)
  i = 1
  for file in files:
    if file.endswith(type):
      #print(f"{path}{file}", f"{path}filerenamed{i}{type}")
      os.rename(f"{path}{file}", f"{path}filerenamed{i}{type}")
      i = i + 1


clear_clutter("data/", ".txt")
