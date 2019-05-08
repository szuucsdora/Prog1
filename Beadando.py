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



#30-as
import sys
import string



#for i in range(1,len(sys.argv)-1):
  #  for j in range(i+1,len(sys.argv)):
   #     if a[i]>a[j]:
    #        a[i],a[j]=a[j],a[i]
     #       print(a)

def kisbetu(a):
    for str in a:
        if 'a' <= str <= 'z':
            return True
        else:
            return False
def nagybetu(a):
    for str in a:
        if 'A' <= str <= 'Z':
            return True
        else:
            return False


def szamok(a):

    for str in a:
        #sz = []
        if '1' <= str <= '9':
            #sz.append(str)
        #for i in sz:
            #if i % 2 == 0:
            return True
        else:
            return False


def paratlanszamok(a):
    if szamok(a)==True:
        for i in a:
            i=int(i)
            if i%2 != 0:
                i.__str__()
                return True
            else:
                return False


def parosszamok(a):
    if szamok(a)==True:
        for i in a:
            i=int(i)
            if i%2 == 0:
                i.__str__()
                return True
            else:
                return False



def csaknulla(a):
    for str in a:
        if '0' == str :
            return True
        else:
            return False

def ujlista(a):
    ls=[]
    ls1=[]
    for i in a:
        if kisbetu(i) == True:
            ls.append(i)

            ls=sorted(ls)
    for i in a:
        if nagybetu(i)==True:
            ls.append(i)
            #tmp=ls1
            #tmp=sorted(tmp)
            #print(tmp)

            #for j in tmp:
            #print(j)
                #ls.append(j)
    for i in a:
        if parosszamok(i) == True:
            ls.append(i)
    for i in a:
        if paratlanszamok(i) == True:
            ls.append(i)
    for i in a:
        if csaknulla(i) == True:
            ls.append(i)
    return ls


print(ujlista(sys.argv[1:]))
