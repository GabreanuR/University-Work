#%%
#Problema1
s = input("s= ").lower()
L = [cuvant for cuvant in s.split() if cuvant[0] in "aeiou"]
print(L)
#%%
#Problema2
s = input("s= ").lower()
k = int(input("k= "))
L = [(chr(((ord(lit)-ord("a")+k)%26)+ord("a")) if lit.isalpha() else lit) for lit in s]
L = "".join(L)
print(L)
#%%
#Problema3
s = input("s= ").lower()
L = [(c+"p"+c if c in "aeiou" else c) for c in s ]
L = "".join(L)
print(L)
#%%
#Problema3_2
s = input("s= ").lower()
L = "".join([(f"{c}p{c}" if c in "aeiou" else c) for c in s ])
print(L)
#%%
#Problema4
L = "".join([chr(c + ord("a")) for c in range(26)])
print(L)
#%%
#Problema5
n = int(input("n= "))
L = [(i if i%2==1 else -i) for i in range(1,n+1)]
print(L)
#%%
#Problema6
L = [1,2,3,4,5,6]
L = [L[i] for i in range(len(L)) if L[i]%2==1 ]
print(L)
#%%
#Problema7
L = [1,2,3,4,5,6]
L = [L[i] for i in range(len(L)) if i%2==1 ]
print(L)
#%%
#Problema8
L = input("L= ").split()
L = [int(L[i]) for i in range(len(L)) if int(L[i])%2==i%2]
print(L)
#%%
#Problema8_2
L = [4,5,6,7]
L = [nr for poz, nr in enumerate(L) if poz%2==nr%2]
print(L)
#%%
#Problema9
L = [1,2,3,4,5,6,7]
L2 = [(L[i],L[i+1]) for i in range(0,len(L)-1,2)]
print(L2)
#%%
#Problema9_2
L = [1,2,3,4,5,6,7]
L2 = [(L[i],L[i+1]) for i in range(len(L)-1)]
print(L2)
#%%
#Problema10
sir = "abcde"
L= [sir[i:] + sir[:i] for i in range(len(sir))]
print(L)
#%%
#Problema11
L1 = list(range(0,11))
L2 = list(range(10,21))
L1[::2] = L2[::2]
print(L1)
print(L2)
#%%
#Problema12
L = [1,2,3,4,5,6,7,8,9,10]
k = int(input("k= "))
L[:k]=[]
print(L)
#%%
#Problema12_2
L = [1,2,3,4,5,6,7,8,9,10]
k = int(input("k= "))
del L[:k]
print(L)
#%%
#Problema12_3
L = [1,2,3,4,5,6,7,8,9,10]
k = int(input("k= "))
for i in range(k):
    L.pop(0)
print(L)
#%%
#Problema12_4
L = [1,2,3,4,5,6,7,8,9,10]
k = int(input("k= "))
while k:
    L.pop(0)
    k-=1
print(L)
#%%
#Problema12_5
L = [1,2,3,4,5,6,7,8,9,10]
k = int(input("k= "))
for i in range(k-1,-1,-1):
    L.pop(i)
print(L)
#%%
#Problema13
L = [5,8,0,3,4,0,7,9,0,4,5,0,2]
if L.count(0) >= 2:
    p1 = L.index(0)
    p2 = L.index(0,p1+1)
    L[p1:p2+1] = []
print(L)
#%%
#Problema14
L = [5,8,0,3,4,0,7,9,0,4,5,0,2]
for i in range(L.count(0)):
    L.remove(0)
print(L)
#%%
#Problema14_2
L = [5,8,0,3,4,0,7,9,0,4,5,0,2]
while 0 in L:
    L.remove(0)
print(L)
#%%
#Problema15
L = [5,8,0,0,0,3,4,0,7,9,0,4,5,0,2]
k = int(input("k= "))
smin = sum(L[:3])
for i in range(1,len(L)-k+1):
    s=sum(L[i:i+k])
    if s<smin:
        smin=s
        cnt=i
print(cnt)
#%%
#Problema16
L = [0,1,3,3,3,4,5,6,6,7,8,9,9]
i = 0
while i < len(L):  
    if L[i] == L[i-1]:
        del L[i]
        i-=1
    i+=1
print(L)
#%%
#Problema17
L = [0,1.3,3,-3,4,-5,6,6,7,-8,9,9]
i = 0
while i < len(L):  
    if L[i] < 0:
        L[i+1:i+1] = [0]
    i+=1
print(L)
#%%
#Problema18
n = int(input("n= "))
L = list(range(2,n+1))
i = 0 
while i < len(L):
    j=i+1
    while j < len(L):
        if L[j]%L[i]==0:
            del(L[j])
        j+=1
    i+=1
print(L)
#%%
#Problema19
Vf = {}
L = [1,4,6,6,23,23,4,2,5,7,4,3,6]
s = 0
for i in L:
    if i in Vf:
        Vf[i]+=1 
    else:
        Vf[i]=1 
for key, value in Vf.items():
    if value > 1:
        s+= value//2
print(s)
#%%
#Problema20
L1 = [0,1,3,4,5,6,7,8,9]
L2 = [0,2,3,4,5,6,8,9,10]
L3 = []
i = j = 0 
while i < len(L1) and j < len(L2):
    if L1[i] < L2[j]:
        if L1[i] not in L3:
            L3.append(L1[i])
        i += 1
    else:
        if L2[j] not in L3:
            L3.append(L2[j])
        j += 1
while i < len(L1):
    if L1[i] not in L3:
        L3.append(L1[i])
    i += 1
while j < len(L2):
    if L2[j] not in L3:
        L3.append(L2[j])
    j += 1
print(L3)
#%%
#Problema20_2
L1 = [0,1,3,4,5,6,7,8,9]
L2 = [0,2,3,4,5,6,8,9,10]
L3 = []
i = j = 0 
while i < len(L1) and j < len(L2):
    if L1[i] == L2[j]:
        if L1[i] not in L3:
            L3.append(L1[i])
        i += 1
        j += 1
    elif L2[j] < L1[i]:
        j += 1
    elif L1[i] < L2[j]:
        i += 1
print(L3)
#%%
#Problema21
n = int(input("n= "))
L = [[0 for _ in range(i+1)] for i in range(n)]
L[0][0] = 1 
print(L[0][0])
L[1][0] = 1 
L[1][1] = 1 
print(L[1][0],L[1][1])
for i in range(2,n):
    j = 1 
    L[i][0] = 1
    while j < i:
        L[i][j] = L[i-1][j] + L[i-1][j-1]
        j += 1
    L[i][j] = 1
    for j in range(i+1):
        print(L[i][j],end=" ")
    print()
#%%
#Problema22
n = int(input("n= "))
L = []
for _ in range(n):
    x = int(input("x= "))
    L.append(x)
minL = min(L)
maxL = max(L)
x = L.count(maxL-minL)
print(x)
#%%
#Problema23
n = int(input("n= "))
v = [int(x) for x in input().split()]
i, j = 0, len(v) - 1
op = 0
while i < j:
    if v[i] == v[j]:
        i += 1
        j -= 1
    elif v[i] < v[j]:
        v[i + 1] += v[i]
        i += 1
        op += 1
    else:
        v[j - 1] += v[j]
        j -= 1
        op += 1
print(op)
#%%
#Problema24
n = int(input("n= "))
L1 = []
L2 = []
for _ in range(n):
    x = int(input("x= "))
    L1.append(x)
for _ in range(n):
    x = int(input("x= "))
    L2.append(x)
x = sum(L1)/sum(L2)
for i in L2:
    if i*x in L1:
        L1.remove(i*x)
if L1 == []:
    print("DA")
else:
    print("NU")
#%%
#Problema25
n = int(input("n= "))
L = []
for _ in range(n):
    x = int(input("x= "))
    L.append(x)
cnt = 1 
lmax = 1 
for i in range(1,len(L)):
    if L[i-1] < L[i]:
        cnt += 1 
        if cnt > lmax:
            lmax = cnt
    else:
        cnt = 1
print(lmax)
#%%
#Problema26
n = int(input("n= "))
L = []
for _ in range(n):
    x = int(input("x= "))
    L.append(x)
i = len(L)-1 
ok = 0
ok2 =0
while i > 0:
    if L[i-1] < L[i]:
        break
    else:
        ok2 = 1
        i -= 1
else:
    L = L[::-1]
    ok = 1
if ok == 0:
    a = L[i-1]
    L[i-1] = L[-1]
    L[-1] = a
    if ok2 == 1:
        L[i:] = L[-1:i-1:-1]
print(L)