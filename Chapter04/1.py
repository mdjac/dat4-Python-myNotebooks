import numpy as np
print("Class Exercise: table")
a = np.arange(10, 30).reshape(4, 5)


print(a)

yellow = a[0,0]
print("Yellow is: ",yellow)

red = a[0,1:4]
print("Red is: ",red)

green = a[0:3,2]
print("Green is: ",green)

blue = a[0:-1:2,-1]
print("Blue is: ",blue)

teal = a[::,1:-1:2]
print("Teal is: ",teal)

print("END")