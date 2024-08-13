a = 10
b = "10"

print(a == b)  #compare values
print(a is b)  #compare exact location of object in memory

a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a == b)  #values are same but return true
print(a is b)  # location is different two different list return false

a = (1, 2, 3)
b = (1, 2, 3)
print(a == b)  #true value is same
print(
    a is b
)  #true location is same because python dont reseve memory for same value create single memory location for same value
a = 3
b = 3
print(a == b)  #true value is same
print(
    a is b
)  #true location is same because python dont reseve memory for same value create single memory location for same value
