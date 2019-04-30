#27. feladat
import numpy as np
m=np.random.randint(0,100,(5,5))
min1 = 0
for i in range(0,m.shape[0]):
    print(i)

    if i > min1:
        min1=i
        print( min1)
min2 = 0
for j in range(0,m.shape[1]):
    print(j)

    if i > min2:
        min2 = i
        print(min2)

print(m)
