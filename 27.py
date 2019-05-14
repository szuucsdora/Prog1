#27. feladat
import numpy as np
#def oszlopbanlegnagyobb():
sor=5
oszlop=5
m=np.random.randint(0,100,(sor,oszlop))
print(m)

legnagyobb=0
s=0
while s<=4:

    for j in range(oszlop):
        if m[j,s] > legnagyobb:
            legnagyobb=m[j,s]
            #return legnagyobb
    print(f"{legnagyobb} a legnagyobb az {s}. oszlopban")
    s+=1
    legnagyobb=0
