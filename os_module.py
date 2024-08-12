import os

print(os.getcwd())


def create_folder():
  if (not os.path.exists("data")):
    os.mkdir("data")
  for i in range(0, 100):
    os.mkdir(f"data/file{i+1}")


def rename():
  for i in range(0, 100):
    os.rename(f"data/file{i+1}", f"data/file{i+1}.txt")


if __name__ == "__main__":
  #create_folder()
  #rename()
  print(dir(os))
