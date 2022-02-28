import numpy as np
print("Class Exercise: cube")
#z,y,x

a = np.arange(0, 27).reshape((3, 3, 3)) # = (z, y, x)

print(a)

first_exercise = a[1,1,::]
print("Slice out [12 13 14] from the above cube using only one slice. e.g: a[:,:,:]",first_exercise)

second_exercise = a[::,1:-1:2,0]
print("Slice out [3 12 21].",second_exercise)
print("Dimensions: ",second_exercise.ndim)


third_exercise = a[0,::,2]
print("Slice out all y-values where x is 2 and z is 0.",third_exercise)

print("END")