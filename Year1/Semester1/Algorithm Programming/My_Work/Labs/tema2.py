#%%
#Problema 1
n=int(input("n= "))
ogl=0
cn=n
while n:
    ogl=ogl*10+n%10
    n//=10
if cn==ogl:
    print(f"{cn} este palindrom")
else:
    print(f"{cn} nu este palindrom")
#%%
#Problema 2
L1,L2=input("L1 si L2 sunt: ").split()
L1,L2=int(L1),int(L2)
aux1,aux2=L1,L2
while aux2!=0:
     r=aux1%aux2
     aux1=aux2
     aux2=r
nr=(L1*L2)//(aux1*aux1)
print(f"Placile au latura de lungime {aux1} si le folosim intr-un numar de {nr}")
#%%
#Problema 3
a,b=input("a si b sunt: ").split()
a,b=int(a),int(b)
f1=0
f2=1
f3=0
while f3<a:
    f3=f1+f2
    f1=f2
    f2=f3
if f3<=b:
    print(f"Cel mai mic numar Fibonacci din intervalul [{a},{b}] este {f3}")
else: 
    print(f"Nu exista niciun numar Fibonacci din intervalul [{a},{b}] este {f3}")
#%%
#Problema 4
a,b=input("a si b sunt: ").split()
a,b=int(a),int(b)
for i in range(0,96,5):
    if a<=i<=b:
        continue
    print(f"{i}",end=" ")
print()
for i in range(95,-1,-5):
    if a<=i<=b:
        continue
    print(f"{i}",end=" ")
#%%
#Problema 5
n=int(input("n= "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#%%
#Problema 6
n=int(input("n= "))
nmax=0
nmin=0
for i in range (9,-1,-1):
    k=0
    aux=n
    while aux:
        if aux%10==i:
            k+=1
        aux//=10
    for j in range (k):
        nmax=nmax*10+i
for i in range (1,10):
    k=0
    aux=n
    while aux:
        if aux%10==i:
            k+=1
        aux//=10
    for j in range (k):
        nmin=nmin*10+i
        if 0<nmin<10:
            y=0
            aux2=n
            while aux2:
                if aux2%10==0:
                    y+=1
                aux2//=10
            for q in range (y):
                nmin=nmin*10
print(f"Numarul maxim posibil este {nmax}")
print(f"Numarul minim posibil este {nmin}")
#%%
#Problema 7
n=int(input("n= "))
nmin=None
for i in range(n):
    s=int(input("s= "))
    if nmin==None:
        nmin=s
        k=1
    elif s<nmin:
        s=nmin
        k=1
    elif s==nmin:
        k+=1
print(f"Cea mai mica valoare este {nmin} si apare de {k} ori")
#%%
#Problema 8
n=int(input("n= "))
nmax1=None
nmax2=None
for i in range(n):
    s=int(input("s= "))
    if nmax1==None and nmax2==None:
        nmax1=s
    elif nmax2==None and nmax1<s:
        nmax2=nmax1
        nmax1=s
    elif nmax2==None and nmax1>s:
        nmax2=s
    elif nmax2==None and nmax1==s:
        continue
    elif s>nmax1:
        nmax2=nmax1
        nmax1=s
    elif nmax2<s<nmax1:
        nmax2=s
if nmax1==None or nmax2==None:
    print("Eroare")
else:
    print(f"Cea mai mare valoare este {nmax1} si a doua cea mai mare valoare este {nmax2}")
#%%
#Problema 9
a,b=input("a si b sunt: ").split()
a,b=int(a),int(b)
x=2
while x<a:
    x=x*2
while x<=b:
    print(x,end=" ")
    x=x*2
#%%
#Problema 10
n=int(input("Introduceti numarul studentilor: "))
a,b=input("Primul interval: ").split()
a,b=int(a),int(b)
for _ in range (n-1):
    a2,b2=input("Alt interval: ").split()
    a2,b2=int(a2),int(b2)
    a,b=max(a,a2),min(b,b2)
    if a>=b:
        print("Studentii nu sunt simultan prezenti")
        break
else: 
    print(f"Intervalul orar este {a} si {b}")
#%%
#Problema 11
n=int(input("Introduceti marimea vectorului: "))
p=int(input("Introduceti indicele creasta: "))
x=int(input("Introduceti elementul 0: "))
for i in range(1,n):
    y=int(input(f"Introduceti elementul {i}: "))
    if i<=p:
        if x<y:
            pass
        else:
            print("Vectorul nu contine creasta de indice p")
            break
    else:
        if x>y:
            pass
        else:
            print("Vectorul nu contine creasta de indice p")
            break
    x=y
else:
    print("Vectorul contine creasta de indice p")
#%%
#Problema 12
n=int(input("n= "))
while n>9:
    aux=0
    while n:
        aux+=n%10
        n=n//10
    n=aux
print(f"cifra de control este {n}")
#%%
#Problema 12 nr 2
n=int(input("n= "))
r=n%9
if n==0:
    cc=0
elif r==0: 
    cc=9
else:
    cc=r
print(f"cifra de control este {cc}")
#%%
#Problema 13
n=int(input("n= "))
if n&(n-1)==0:
    while n>1:
        print(n,n-1,end=" ")
        n//=2
else:
    print(n,end=" ")
    n+=1
    n//=2
    while n>1:
        print(n,n-1,end=" ")
        n//=2
#%%
#Problema 14
n=int(input("n= "))
i=1
nr=0
while i*i<=n:
    if n%i==0:
        if i*i==n:
            nr+=1
        else:
            nr+=2
    i+=1
print(f"Numarul {n} are {nr} divizori")
#%%
#Problema 15
n=int(input("n= "))
y=0
z=0
for j in range(1,n+1):
    i=1
    nr=0
    while i*i<=j:
        if j%i==0:
            if i*i==j:
                nr+=1
            else:
                nr+=2
        i+=1
    if y<nr:
        y=nr
        z=j
print(f"Numarul {z} ...")
#%%
#Problema 16
n=int(input("n= "))
i=1
nr=0
while i*i<=n:
    if n%i==0:
        if i*i==n:
            nr+=1
        else:
            nr+=2
    i+=1
if nr==3:
    print(True)
else:
    print(False)
#%%
#Problema 17
a,b=input("a si b sunt: ").split()
a,b=int(a),int(b)
y=min(a,b)
i=1
nr=0
while i<=y//2:
    if a%i==0 and b%i==0:
        nr+=1
    i+=1
print(f"Numarul de divizori comuni este {nr}")
#%%
#Problema 18
n=int(input("n= "))
p=5
s=0
while p<=n:
    s+=n//p
    p*=5
print(f"Numarul de zerouri din coada factorialului este {s}")
#%%
#Problema 19
