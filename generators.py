def generators():
  for i in range(100):
    yield i


gen = generators()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

