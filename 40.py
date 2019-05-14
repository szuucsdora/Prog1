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