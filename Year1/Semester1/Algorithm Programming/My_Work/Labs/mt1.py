#%%
#Ex1
with open("mt1.1.in","r") as f:
    M = []
    i = 0
    g = open("mt1.1.out","w")
    for linie in f:
        L = linie.strip().split()
        M.append([])
        for elem in L:
            M[i].append(int(elem))
        M[i].remove(max(M[i]))
        M[i].remove(max(M[i]))
        for j in range(len(M[i])):
            M[i][j] = str(M[i][j])
        for j in range(len(M[i])):
            R = " ".join(M[i])
        g.write(R)
        g.write("\n")
        i += 1
#%%
#Ex2
with open("m1.2.txt","r") as f:
    D = {}
    fmax = 0
    for linie in f:
        L = linie.strip().split()
        for cuv in L:
            if cuv.lower() not in D:
                D[cuv.lower()] = 1
                if D[cuv.lower()] > fmax:
                    fmax = D[cuv.lower()]
            else:
                D[cuv.lower()] += 1
                if D[cuv.lower()] > fmax:
                    fmax = D[cuv.lower()]
    D2 = {}
    for i in range(fmax):
        D2[i+1] = []
    for i in D.keys():
        D2[D[i]].append(i)
    for i in range(fmax,0,-1):
        L = " ".join(D2[i])
        L = L.strip().split()
        L.sort()
        L = ", ".join(L)
        print(f"Frecventa {i}: " + L)
#%%
#Ex3
def sterge_ore(D,cinema,film,ore):
    L = [] 
    if cinema not in D.keys():
        return L
    else:
        for i in D[cinema]:
            if film in i:
                for j in i[1]:
                    if j in ore:
                        i[1].remove(j)
                if i[1] == []:
                    D[cinema].remove(i)
        L = D[cinema]
        return L
def cinema_film(D,*cinematografe,ora_minima,ora_maxima):
    return
with open("m1.3.txt","r") as f:
    D = {}
    for linie in f:
        s,f,o = linie.strip().split("%")
        s = s.strip()
        f = f.strip()
        o = o.split()
        if s not in D.keys():
            D[s] = []
        D[s].append([f,o])
f = input("nume film = ")
c = input("cinema = ")
o = input("ore = ")
o = o.split()
L = sterge_ore(D,c,f,o)
print(L)
print(D)
cinematografe = ["Cinema 1","Cinema 2"]
o1 = "14:00"
o2 = "22:00"
R = cinema_film(D,cinematografe,ora_minima = o1, ora_maxima = o2)
print(R)
#%%
#Ex3c
def cinema_film(D,*cinematografe,ora_minima,ora_maxima):
    L = []
    ominh,ominm = ora_minima.strip().split(":")
    ominh = int(ominh)
    ominm = int(ominm)
    omaxh,omaxm = ora_maxima.strip().split(":")
    omaxh = int(omaxh)
    ominh = int(ominh)
    for cinema in cinematografe:
        if cinema in D.keys():
            for film,ore in D[cinema]:
                O = []
                for ora in ore:
                    ogenh,ogenm = ora.split(":")
                    ogenh = int(ogenh)
                    ogenm = int(ogenm)
                    if ominh < ogenh < omaxh:
                        O.append(ora)
                    elif ominh == ogenh and ominm <= ogenm:
                        O.append(ora)
                    elif ogenh == omaxh and ogenm < omaxm:
                        O.append(ora)
                if O != []:
                    L.append((film,cinema,O))
    L.sort(key = lambda t : (t[0],-len(t[2])))
    return L
with open("m1.3.txt","r") as f:
    D = {}
    for linie in f:
        s,f,o = linie.strip().split("%")
        s = s.strip()
        f = f.strip()
        o = o.split()
        if s not in D.keys():
            D[s] = []
        D[s].append([f,o])
o1 = "14:00"
o2 = "22:00"
R = cinema_film(D,"Cinema 1","Cinema 2",ora_minima = o1, ora_maxima = o2)
print(R)