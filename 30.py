import sys






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

        if '1' <= str <= '9':

            return True
        else:
            return False


def paratlanszamok(a):
    if szamok(a)==True:
        for i in a:
            i=int(i)
            if i%2 != 0:

                return True
            else:
                return False


def parosszamok(a):
    if szamok(a)==True:
        for i in a:
            i=int(i)
            if i%2 == 0:

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
    ls2=[]
    ls3=[]
    ls4=[]
    ls5=[]
    for i in a:
        if kisbetu(i) == True:
            ls.append(i)
            ls=sorted(ls)
    for i in a:
        if nagybetu(i)==True:
            ls1.append(i)
            ls1=sorted(ls1)
    for i in a:
        if parosszamok(i) == True:
            ls2.append(i)
            ls2=sorted(ls2)
    for i in a:
        if paratlanszamok(i) == True:
            ls3.append(i)
            ls3=sorted(ls3)
    for i in a:
        if csaknulla(i) == True:
            ls4.append(i)
            ls4=sorted(ls4)
    ls5=ls+ls1+ls2+ls3+ls4
    return ls5


print(ujlista(sys.argv[1:]))
