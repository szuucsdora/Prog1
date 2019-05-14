#27. feladat
import numpy as np
#def sorbanlegnagyobb():
M=5
N=5
m=np.random.randint(0,100,(N,M))
print(m)
#min = 0
ossz=0
for i in range(0,N):
    #print(i)

  #  if m[i,0] > min1:
   #     min1=i
    #    print( min1)
#min2 = 0
    #for j in range(0,i+1):
    #print(j)

        #if m[i,0] > min:
            #min = m[i,j]
            #print(min)

    for j in range(0,M):
        ossz += m[i][0]
print(ossz)

