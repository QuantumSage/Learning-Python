import math
def closestSchool(x,y,L):
    rs=[x,y]
    n=len(L)
    l1=[]
    for i in range(n):
        l1.append(math.sqrt((math.pow(L[i][0]-rs[0],2)+math.pow(L[i][1]-rs[1],2))))
    l2=[]
    min=0
    for i in range(n):
        if(l1[i]<l1[min]):
            min=i
    for i in range(n):
        if(l1[i]==l1[min]):
            l2.append(i)
    for i in l2:
        print(L[i])
x, y = map(int, input().split())

n = int(input())
L = []
for i in range(n):
    l = list(map(int, input().split()))
    L.append(l)
closestSchool(x, y, L)