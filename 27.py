# 27. feladat
import numpy as np

sor = 5
oszlop = 5
m = np.random.randint(0, 100, (sor, oszlop))
print(m)


def oszlopbanlegnagyobb(m):
    legnagyobb = 0
    s = 0
    while s <= 4:

        for j in range(oszlop):
            if m[j, s] > legnagyobb:
                legnagyobb = m[j, s]
        print(f"{legnagyobb} a legnagyobb az {s}. oszlopban")
        s += 1
        legnagyobb = 0


#print(oszlopbanlegnagyobb(m))


def sorbanlegnagyobb(m):
    legnagyobb = 0
    s = 0

    while s <= 4:

        for i in range(oszlop):
            if m[s, i] > legnagyobb:
                legnagyobb = m[s, i]
        print(f"{legnagyobb} a legnagyobb az {s}. sorban")
        s += 1
        legnagyobb = 0


#print(sorbanlegnagyobb(m))


def osszeg1(m):
    legnagyobb = 0
    s = 0
    ossz=[]
    while s <= 4:

        for j in range(oszlop):
            if m[j, s] > legnagyobb:
                legnagyobb = m[j, s]

        ossz.append(legnagyobb)
        s += 1
        legnagyobb = 0
    return ossz

def osszeg2(m):
    legnagyobb = 0
    s = 0
    ossz=[]
    while s <= 4:

        for i in range(oszlop):
            if m[s, i] > legnagyobb:

                legnagyobb = m[s, i]

        ossz.append(legnagyobb)
        s += 1
        legnagyobb = 0
    return ossz


def osszeg(m):
    ossz=0
    for i in osszeg1(m):
        ossz+=i
    for j in osszeg2(m):
        ossz+=j
    print('Ezek összege: {}'.format(ossz))

def osszefuz(m):
    print(oszlopbanlegnagyobb(m))
    print(sorbanlegnagyobb(m))
    print(osszeg(m))

#print(osszeg1(m))
#print(osszeg2(m))
#print(osszeg(m))
print(osszefuz(m))
