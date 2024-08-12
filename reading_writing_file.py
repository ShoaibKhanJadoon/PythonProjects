#Reading a file
file = open('myfile.txt', 'r')
text = file.read()
print(text)
file.close()

with open('myfile.txt', 'r') as file:
  text = file.read()
  print(text)

#Writing a file

file = open('myfile.txt', 'a', newline='\n')
#print(open('myfile.txt', '+a').__doc__)
file.write("shoaib khan3324\n")

file.close()

with open('myfile.txt', 'a', newline='\n') as file:
  file.write("shoaib khan3324\n")


def readline():
  """Read lines"""
  with open('marks.txt', 'r') as f:
    i = 0
    while True:
      i = i + 1
      line = f.readline()
      if not line:
        break
      else:
        m1 = line.split(" ")[0]
        m2 = line.split(" ")[1]
        m3 = line.split(" ")[2]
        print(f"line {i} math  ={m1}")
        print(f"line {i} english  ={m2}")
        print(f"line {i} urdu  ={m3}")


with open('marks.txt', 'w') as f:
  lines = ["line1\n", "line2\n", "line3\n"]
  f.writelines(lines)

with open('marks.txt', 'w') as f:
  lines = ["line1", "line2", "line3"]
  for line in lines:
    f.writelines(line + "\n")

with open("marks.txt", "r") as f:
  print(f.read())
