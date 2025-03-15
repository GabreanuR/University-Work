#%%
#Problema 1 

x=int(input("x = "))
y=int(input("y = "))
suma=x+y
prod=x*y
print(suma, prod)
print(suma, prod, sep=",")
print(suma, prod, sep="\n")
print(f"suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y}")

#print("suma numerelor {x} si {y} este {x+y}, iar produsul este {x*y}")

#%%
#Problema 2

a,b,c=input("introduceti 3 numere: ").split()
#print(a,b,c)
#print(type(a))
a,b,c=int(a),int(b),int(c)
#print(a,b,c)
#print(type(a))
if 0<=a<24 and 0<=b<60 and 0<=c<60:
    print(f"{a:.02f}:{b:02d}:{c:02d}")
else:
    print("Date invalide")

#%%
#Problema 3

z=int(input("zi="))
l=int(input("luna="))
a=int(input("an="))
ok=True

if l in [1,3,5,7,8,10,12]:
    #31 de zie
    if 0<z<31:
        z+=1
    elif z==31:
        z=1;
        if l==12:
            l=1
            a+=1
        else:
            l+=1
    else:
        ok=False
elif l in [4,6,9,11]:
    #30 de zile
    if 0<z<30:
        z+=1
    elif z==30:
        z=1;
        l+=1
    else:
        ok=False
elif l==2:
    #februarie
    if a%4==0 and a%100!=0 or a%400==0:
        #an bisect 29 zile
        if 0<z<29:
            z+=1
        elif z==29:
            z=1;
            l+=1
        else:
            ok=False
    else:
        #anul nu e bisect 28 zile
        if 0<z<28:
            z+=1
        elif z==28:
            z=1;
            l+=1
        else:
            ok=False
else:
    ok=False

if ok==False:
    print("Date incorecte")
else:
    print(f"{z:02d}:{l:02d}:{a:04d}")
#%%

nr=34.2327
nr=int(nr*1000)
print(f"{(nr/1000)}")
#%%
#Problema 4

x,op,y=input("scrie o expresie cu 2 temeni: ").split()
x,y=float(x),float(y)
if op=="+":
    r=x+y
    print(f"{r:.3f}")
elif op=="-":
    r=x-y
    print(f"{r:.3f}")
elif op=="*":
    r=x*y
    print(f"{r:.3f}")
elif op=="/":
    r=x/y
    print(f"{r:.3f}")
elif op=="//":
    r=x//y
    print(f"{r:.3f}")
else:
    print("Eroare")
#%%
#Problema 5

a,b,c,d,e,f=input("scrie o expresie cu 6 temeni: ").split()
a,b=int(a),int(b)
c,d=float(c),float(d)
print(a,b,c,d,e,f,sep=" ")
print(a,c,e,b,d,f,sep=" ")
print(a,b,c,d,e,f,sep="\n")
print((a,b),(c,d),(e,f),sep="\n")
#%%
#Problema 6

z=int(input("Cate zile? "))
b=float(input("Curs astazi: "))
m=0
for x in range(1,z):
    a=b
    b=float(input("Curs astazi: "))
    d=b-a
    if d>m:
        m=d
        z1=x
        z2=x+1
print(f"Cea mai mare crestere a fost de {m:.2f} intre zilele {z1} si {z2}")
#%%
#Problema 7

s=float(input("Cat costa jucaria? "))
nrz=0
sc=0
while s>0:
    x=float(input("Cati bani a depus Gigel azi? "))
    s=s-x
    sc+=x
    nrz+=1
    m=sc/nrz
    print(f"Pana acum, Gigel a depus in medie {m:.3f} lei pe zi")
print(f"Gigel a strans banii in {nrz} zile, a mai ramas cu {-s} lei")
#%%
#Problema 8

a,b,c=input("introduceti 3 numere: ").split()
a,b,c=int(a),int(b),int(c)
y=max(a,b,c)
x=min(a,b,c)
print(y-x)

#%%
#Problema 9 

a,b,c=input("introduceti 3 numere: ").split()
a,b,c=int(a),int(b),int(c)
y=max(a,b,c)
x=min(a,b,c)
print(x,a+b+c-y-x,y)
