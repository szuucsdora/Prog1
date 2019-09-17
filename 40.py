import numpy as np

m=np.empty([2,2])

for i in range(2):
    for j in range(2):
        m[i,j]=np.random.randint(1, 100)

det=(m[0,0]*m[1,1])-(m[0,1]*m[1,0])

while True:
    if det >= 10 and det <= 20:
        break
    else:
        m = np.empty([2, 2])

        for i in range(2):
            for j in range(2):
                m[i,j] = np.random.randint(1, 100)

        det = (m[0, 0] * m[1, 1]) - (m[0, 1] * m[1, 0])

print(m)
print('Determináns értéke:',det)





import math



# class Ember:
#     def __init__(self,nev,kor,nem):
#         self.nev = nev
#         self.kor = kor
#         self.nem = nem
#
#     def idos_e(self):
#         return self.kor > 65
#
#
# e = Ember("Béla",20,True)
# print("Név: ",e.nev)
# print("e idős-e?",e.idos_e())

#1. feladat python osztály amelyben a hatványozás s az abszolút érték műveletet tudjuk implementálni
"""
Szám:
    adattagjai:
    1. x
    2. n
    metódusai:
    1. pow(x,n) - hatványozás
    2. abs(n)
"""
class Szam:

    def __init__(self,x,n):
        self.x=x
        self.n=n

    #self.x ^ self.n
    def pow(self):
        p=1
        for i in range(self.n):
            p*=self.x
        return p

    def abs(self):
        if self.n >= 0:
            return self.n
        else:
            return -self.n


szam1 = Szam(-3,4) #példányositottam egy Szam típusú objektumot
# print(szam1.pow())
# print(szam1.abs())

#2. Feladat python osztály kör néven, egy adattag: kör sugara, 2 metódus, ami K-t és T-t számol a körnek

class Circle:
    def __init__(self,r):
        self.r=r

    def kerulet(self):
        return 2*self.r*math.pi


    def terulet(self):
        return (self.r**2)*math.pi


karika=Circle(3)
# print(karika.kerulet(),karika.terulet())

#3. feladat  téglalap kerület terület

class Teglalap:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def terul(self):
        return self.a*self.b

    def kerul(self):
        return 2*(self.a+self.b)

t=Teglalap(2,4)
# print(t.terul(),t.kerul())

#4. feladat

class Szting:
    def __init__(self):
        self.s=""

    def get_String(self):
        self.s=input("Adjon emg egy sztinget: ")

    def print_String(self):
        print(self.s.upper())

sztring1=Szting()
sztring1.get_String()
sztring1.print_String()

class Ember:
    def __init__(self,nev,kor,nem):
        self.nev = nev
        self.kor = kor
        self.nem = nem

    def idos_e(self):
        return self.kor > 65

    @staticmethod
    def legidosebb(lista):
        li = 0

        for i in lista:
            if i.kor > li:
                li = i.kor
                neve = i.nev
        return neve

e = Ember("Béla",20,True)
print("Név: ",e.nev)
print("e idős-e?",e.idos_e())

lista=[]
lista.append(e)
lista.append(Ember("AB",21,False))
lista.append(Ember("DE",22,False))
lista.append(Ember("IJK",20,True))

# Legidősebb ember nevét kiirni


# li=0
#
# for i in lista:
#     if i.kor>li:
#         li=i.kor
#         neve=i.nev
# print(li,neve)


#osztálymetódus hívás
print("Legidősebb: ",Ember.legidosebb(lista))
