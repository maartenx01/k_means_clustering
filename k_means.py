import random
import math

X = []

x1 = [2,3]
x2 = [3,1]
x3 = [4,2]
x4 = [11,5]
x5 = [12,4]
x6 = [12,6]
x7 = [7,5]
x8 = [8,4]
x9 = [8,6]

X.append(x1)
X.append(x2)
X.append(x3)
X.append(x4)
X.append(x5)
X.append(x6)
X.append(x7)
X.append(x8)
X.append(x9)

print("X")
print(X)


k = 2

zLst = []
for i in range(k):
    index = math.floor(random.random() * len(X))
    val = X[index]
    new_val = val[:]
    zLst.append(new_val)

print("Initial centroids")
print(zLst)

def assign(observation, centroidLst):
    distLst = []
    for i in range(len(centroidLst)):
        dsplcmnt = 0
        for j in range(len(centroidLst[i])):
            dsplcmnt = dsplcmnt + (observation[j] - centroidLst[i][j])**2
        distLst.append(math.sqrt(dsplcmnt))
    val, idx = min((val, idx) for (idx, val) in enumerate(distLst))
    return (val,idx)

def equality(lst1, lst2):
    for element in range(len(lst1)):
        for attribute in range(len(lst1[element])):
            if lst1[element][attribute] != lst2[element][attribute]:
                return False
    return True

count = 0
clusterLst = []
clusterObjFunc = []

while True:

    print("lap", count)

    clusterLst = []
    clusterObjFunc = []

    for i in range(k):
        lst = []
        init = 0
        clusterLst.append(lst)
        clusterObjFunc.append(init)

    for i in range(len(X)):
        val, group = assign(X[i], zLst)
        clusterLst[group].append(X[i])
        clusterObjFunc[group] = clusterObjFunc[group] + val

    zLst_old = zLst

    zLst = []

    for group in range(len(clusterLst)):
        z = []
        for attribute in range(len(clusterLst[0][0])):
            total = 0
            for element in range(len(clusterLst[group])):
                total = total + clusterLst[group][element][attribute]
            denom = max(len(clusterLst[group]),1)
            z.append(total/denom)
        zLst.append(z)

    if equality(zLst_old, zLst):
        break

    count = count + 1

objective = 0

for i in range(len(clusterObjFunc)):
    objective = objective + clusterObjFunc[i]

print("Clusters")
print(clusterLst)
print("Terminal centroids")
print(zLst)
print("Objective function by cluster")
print(clusterObjFunc)
print("Objective function")
print(objective)


