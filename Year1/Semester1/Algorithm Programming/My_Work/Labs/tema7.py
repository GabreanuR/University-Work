#%%
#Problema1_a
def citire():
    n = int(input("n= "))
    L = []
    for i in range(0,n):
        L.append(int(input(f"Elementul {i} este: ")))
    return L
print(citire())
#%%
#Problema1_b
def citire():
    n = int(input("n= "))
    L = []
    for i in range(0,n):
        L.append(int(input(f"Elementul {i} este: ")))
    return L
def cautare(s,x,i=0,j=None):
    if j is None:
        j = len(s)
    for k in range(i,j):
        if s[k]>x:
            return k
    return -1
print(cautare(citire(),12,2,7))
#%%
#Problema1_c
def citire():
    n = int(input("n= "))
    L = []
    for i in range(0,n):
        L.append(int(input(f"Elementul {i} este: ")))
    return n,L
def cautare(s,x,i=0,j=None):
    if j is None:
        j = len(s)
    for k in range(i,j):
        if s[k]>x:
            return k
    return -1
n,L = citire()
for poz in range(n-1):
#    if cautare(L,L[poz],poz+1) != -1:  #j = valoarea default
    if cautare(L,L[poz],poz+1,poz+2) != -1:
        print("Nu")
        break
else: 
    print("Da")    
#%%
#Problema2_a
def cifmaxim(*numere):
    rez = int("".join([max(str(x)) for x in numere]))
    return rez
print(cifmaxim(23,567,89345,234))
#%%
#Problema2_b
def cifmaxim(*numere):
    rez = int("".join([max(str(x)) for x in numere]))
    return rez
def b2(a,b,c):
    if cifmaxim(a,b,c) == 111:
        return True
    else:
        return False
print(b2(1001,101,1))
#%%
#Problema3
def cautare_cuvant(cuv, nume_fis_out, *nume_fis_in):
    cuv = cuv.lower()
    with open(nume_fis_out, "w") as g:
        for nume in nume_fis_in:
            L = []
            with open(nume, "r") as f:
                for i,linie in enumerate(f):
                    L_cuvinte = [c.strip("!.,?:;") 
                            for c in linie.lower().replace("-"," ").split()]        
                    if cuv in L_cuvinte:
                        L.append(i+1)
            g.write(f"{nume} {'Cuvantul nu a fost gasit' if L == [] else ' '.join([str(x) for x in L]) }\n")
            
cautare_cuvant("Floare", "L7.ex3.rez.txt", "eminescu.txt", "paunescu.txt")
#%%
#Problema4_a

d = {}
def citire():
    with open("L7.cinema.in","r") as f:
        for linie in f:
            cinema,film,ore = linie.split(" % ")
            L_ore = ore.strip().split()
            if cinema not in d.keys():
                d[cinema] = {}
            d[cinema][film] = L_ore
    return d
print(citire())
#%%
#Problema4_b
d = {}
def citire():
    with open("L7.cinema.in","r") as f:
        for linie in f:
            cinema,film,ore = linie.split(" % ")
            L_ore = ore.strip().split()
            if cinema not in d.keys():
                d[cinema] = {}
            d[cinema][film] = L_ore
    return d
def sterge_ore(d,cinema,film,multime_ore):
    if cinema in d.keys():
        if film in d[cinema].keys():
            for poz in range(len(d[cinema][film]) -1, -1, -1):
                if d[cinema][film][poz] in multime_ore:
                    d[cinema][film].pop(poz)
            if len(d[cinema][film]) == 0:
                del d[cinema][film]
    return d[cinema].keys()
film = input("film= ")
cinema = input("cinema= ")
ora = input("hh:mm= ")
print(sterge_ore(citire(), cinema, film, {ora}))
print(d)

#%%
#Problema4_c
d = {}
def citire():
    with open("L7.cinema.in","r") as f:
        for linie in f:
            cinema,film,ore = linie.split(" % ")
            L_ore = ore.strip().split()
            if cinema not in d.keys():
                d[cinema] = {}
            d[cinema][film] = L_ore
    return d
d = citire()
def cinema_film(d, *cinematografe, ora_min, ora_max):
    rez = []
    for cinema in cinematografe:
        if cinema in d:
            for film in d[cinema]:
                aux_ore = []
                for ora in d[cinema][film]:
                    if ora_min <= ora <= ora_max:
                        aux_ore.append(ora)
                if aux_ore != []:
                    rez.append((film,cinema,aux_ore))
    rez.sort(key = lambda t: (t[0],-len(t[2])))
    return rez
print(cinema_film(d, "Cinema 1", "Cinema 2", ora_min = "14:00", ora_max = "22:00"))
#%%
#Module
def nr_cif(c):
    if c == 0:
        return 0
    else:
        return 1 + nr_cif(c//10)
def inv(c):
     if c == 0:   
         return 0
     else:
         return c%10 * (10 ** (nr_cif(c)-1)) + inv(c//10)
print(inv(432))
def cmmdc(a, b):
    if b == 0:
        return a;
    return cmmdc(b, a%b)

c = int(input("c = "))
def verif(c,*nr):
    cnt = 0
    for i in nr:
        if c == nr_cif(i):
            cnt += 1 
    return cnt
print(verif(c,15,19,234,1567))