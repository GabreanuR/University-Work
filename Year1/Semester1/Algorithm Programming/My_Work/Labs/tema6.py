#%%
#---

L = [4,6,13,173,2,142,189,2222]

L.sort()
print(L)


#%%
#---

L = [4,6,13,173,2,142,189,2222]

L2 = sorted(L, reverse = True)
print(L2)

#%%
#Ex1a

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = str))

#%%
#Ex1b

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda x: str(x)[::-1] ))

#%%
#Ex1c

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda x: len(str(x)) , reverse=True ))

#%%
#Ex1c_2

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda x: -len(str(x)) ))

#%%
#Ex1d

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda x: len(set(str(x)))  ))


#%%
#Ex1e

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda x: (len(str(x)), -x)  ))

#%%
#Ex1f

L = [4,6,13,173,2,142,189,2222]

print(sorted(L, key = lambda n: (1, -n) if n % 2 == 0 else (0, n)))
#%%
#Ex1g

s1 = input("Propozitie= ").split()
cuvinte_sort = sorted(s1, key=lambda cuv: len(cuv), reverse=True)
s2 = " ".join([cuv for cuv in cuvinte_sort if len(cuv) >= 2])
print(s2)
#AAAAAAAAAAAAAAAAAAAAAAA MOOOOOOOOOOOOOOOOOOOOOOOOR
#%%
#Ex1h

v =  [11, 45, 20, 810, 179, 81, 1000]
print(sorted(v, key = lambda x: (sum(int(y) for y in str(x)), -x) ))
#%%

d = {} #dictionar vid
m = set() #multimea vida

#%%
#Ex2a

f = open("pb2_elevi.in", "r")
d = {}
for linie in f:
    # cnp, nume, prenume, *note = linie.split() #note egal liste de str-uri
    # cnp, nume, prenume, note = linie.split(" ", 3)
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, note]
    
f.close()    
print(d)

#%%
#Ex2b
f = open("pb2_elevi.in", "r")

for linie in f:
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, L_note]
    
def creste_nota(cnp,d):
    if cnp not in d:
        return None
    d[cnp][2][0] += 1
    return d[cnp][2][0]

cnp = int(input("CNP: "))
print(creste_nota(cnp, d))
print(d)

f.close() 
#%%
#Ex2c

f = open("pb2_elevi.in", "r")

for linie in f:
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, L_note]
    
def adauga_nota(cnp,L,d):
    if cnp in d:
        #d[cnp][2] += L
        d[cnp][2].extend(L)
        return d[cnp][2]

cnp = int(input("CNP: "))
print(adauga_nota(cnp,[10, 8], d))
print(d)

f.close() 

#%%
#Ex2d

f = open("pb2_elevi.in", "r")

for linie in f:
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, L_note]
    
def del_info(cnp,d):
    if cnp in d:
        del d[cnp]

cnp = int(input("CNP: "))
print(del_info(cnp, d))
print(d)

f.close() 

#%%
#Ex2e

f = open("pb2_elevi.in", "r")

for linie in f:
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, L_note]
    
Lrez = sorted(d.values(), key = lambda L: (-sum(L[2])/len(L[2]), L[0]))



g = open("pb2_elevi.out", "w")
for elev in Lrez:
    g.write(str(elev)+"\n")

g.close()
f.close() 

#%%
#Ex2f

import random
import string

f = open("pb2_elevi.in", "r")

for linie in f:
    cnp, nume, prenume, note = linie.split(maxsplit = 3) # note este str
    
    cnp = int(cnp)
    L_note = [int(x) for x in note.split()]
    
    d[cnp] = [nume, prenume, L_note]
    
def genereaza_coduri(d):
    for cnp in d:
        cod = "".join(random.choices(string.ascii_letters, k=3) 
                      + random.choices("0123456789", k=3))
        d[cnp].append(cod)
        #sau
        #d[cnp] += [cod]
        #sau
        #d[cnp].extend([cod])


print(genereaza_coduri(d))
print(d)

f.close() 
#%%
#Ex3
f = open("pb3.in", "r")

L_cuv = f.read().split()

f.close()

p = 2
d = {}

for cuv in L_cuv:
    sufix = cuv[-p:]
    if sufix not in d:
        d[sufix] = [cuv]
    else:
        d[sufix].append(cuv)
        
Lrez = sorted(d.values(), key = lambda L_cuv: -len(L_cuv))

g = open("rime.txt", "w")

for L_cuv in Lrez:
    g.write(" ".join(sorted(L_cuv, reverse = True)) + "\n")
    
g.close()

#%%
#Ex4

f = open("L6.pb4.in", "r")
L_cuv = f.read().split()
f.close()


d = {}
for cuv in L_cuv:
    litere = frozenset(cuv)
    if litere not in d:
        d[litere] = [cuv]
    else:
        d[litere].append(cuv)


L_rez= [ sorted(L_cuv, reverse = True)
        for litere, L_cuv in sorted(d.items(), 
                key = lambda t: -len(t[0])) if len(L_cuv) >= 2]

g = open("L6.pb4.out", "w")

for L_cuv in L_rez:
    g.write(" ".join(sorted(L_cuv, reverse = True)) + "\n")
    
g.close()
#%%
#Ex5a
f = input("fisier 1: ")
g = input("fisier 2: ")

d = {}

def nrcuv(f,g):
    f = open(f, "r")
    g = open(g, "r")
    L_cuv1 = f.read().split()
    L_cuv2 = g.read().split()
    f.close()
    g.close()
    for cuv in L_cuv1:
        if cuv not in d:
            d[cuv] = 1 
        else:
            d[cuv] +=1
    for cuv in L_cuv2:
        if cuv not in d:
            d[cuv] = 1 
        else:
            d[cuv] +=1
    return d
print(nrcuv(f,g))
#%%
#Ex5b
f = input("fisier 1: ")
g = input("fisier 2: ")

d = {}

def nrcuv(f,g):
    f = open(f, "r")
    g = open(g, "r")
    L_cuv1 = f.read().split()
    L_cuv2 = g.read().split()
    f.close()
    g.close()
    for cuv in L_cuv1:
        if cuv not in d:
            d[cuv] = 1 
        else:
            pass
    for cuv in L_cuv2:
        if cuv not in d:
            d[cuv] = 1 
        else:
            pass
    k = [cuv for cuv in d.keys() if len(cuv)==1]
    for i in k:
        d.pop(i)
    T=sorted(d)
    for i in range(len(L_cuv1)):
        if len(L_cuv1[i])==1 and L_cuv1[i] in k:
            T.insert(i,L_cuv1[i])
            k.pop(0)
    T = " ".join(T)
    return T
print(nrcuv(f,g))
#%%
#Ex5c
f = input("fisier 1: ")

d = {}

def nrcuv(f):
    f = open(f, "r")
    L_cuv1 = f.read().split()
    f.close()
    for cuv in L_cuv1:
        if cuv not in d:
            d[cuv] = 1 
        else:
            d[cuv] +=1
    return d
T = nrcuv(f)
print(sorted(T.items(), key = lambda T: T[1], reverse=True))
#%%
#Ex5d
f = input("fisier 1: ")

d = {}

def nrcuv(f):
    f = open(f, "r")
    L_cuv1 = f.read().split()
    f.close()
    for cuv in L_cuv1:
        if cuv not in d:
            d[cuv] = 1 
        else:
            d[cuv] +=1
    return d
T = nrcuv(f)
rez = max(T.items(), key = lambda T: T[1])
print(rez[0])
#%%
#Ex5e

import math
f = input("fisier 1: ")
g = input("fisier 2: ")

d = {}

def nrcuv(f,g):
    f = open(f, "r")
    g = open(g, "r")
    L_cuv1 = f.read().split()
    L_cuv2 = g.read().split()
    f.close()
    g.close()
    for cuv in L_cuv1:
        if cuv not in d:
            d[cuv] = [1 , 0] 
        else:
            d[cuv][0] += 1
    for cuv in L_cuv2:
        if cuv not in d:
            d[cuv] =  [0 , 1]
        else:
            d[cuv][1] += 1
    return d
T = nrcuv(f,g)
def dcos(T):
    s1 = 0
    s2 = 0
    s3 = 0
    for i in T.keys():
        s1 += T[i][0]*T[i][1]
    for i in T.keys():
        s2 += T[i][0]*T[i][0]
    for i in T.keys():
        s3 += T[i][1]*T[i][1]
    return s1/(math.sqrt(s2)*math.sqrt(s3))
print(f"{dcos(T):.2f}")
#%%
#Ex6
import random
import string

f = input("fisier 1: ")
g = open("L6.ex6.2.txt", "w")
f = open(f, "r")

for linie in f:
    nume, prenume = linie.split()
    email = "".join(prenume.lower()+"."+nume.lower()
                    +"@s.unibuc.ro")
    parola = "".join(random.choices(string.ascii_uppercase, k=1)
                + random.choices(string.ascii_lowercase, k=3) 
                  + random.choices("0123456789", k=4))
    g.write(email + "," + parola + "\n")

f.close()
g.close()