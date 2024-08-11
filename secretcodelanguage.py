import random

string = "Note: If you get stuck, you can reach out to us in one of our communication channels."
randomalp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
words = string.split(" ")
encoded = ""
for alphabet in words:
  #print(alphabet)
  if len(alphabet) >= 3:
    alphabet = list(alphabet)
    removed = alphabet.pop(0)
    alphabet.append(removed)
    for i in range(3):
      alphabet.insert(0, randomalp[random.randint(0, len(randomalp) - 1)])
    encode = "".join(alphabet)
    #print(encode)
    encoded = encoded + " " + encode

  else:
    endoded = encoded + " " + alphabet
print(encoded)

decoded = ""
encoded = encoded.split()
for alphabet in encoded:
  if len(alphabet) >= 3:
    alphabet = list(alphabet)
    for i in range(3):
      removed = alphabet.pop(0)
    last = alphabet.pop(-1)
    alphabet.insert(0, last)
    decode = "".join(alphabet)
    #print(encode)
    decoded = decoded + " " + decode

  else:
    endoded = decoded + " " + alphabet
print(decoded)
