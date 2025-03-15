#%%
#Ex1
def citire():
    with open("lab9ex1.txt","r") as f:
        L = [(i+1, int(t)) for i,t in enumerate(f.readline().split())]
        return L
def Greedy(L):
    L.sort(key = lambda t: t[1])
    G = []
    suma_t_servire = 0
    suma_t_asteptare = 0
    for poz,t_servire in L:
        suma_t_servire += t_servire
        suma_t_asteptare += suma_t_servire
        G.append((poz,t_servire,suma_t_servire))
    TMA = suma_t_asteptare/len(L)
    return G,TMA
def afisare(G,TMA):
    print(f"{'nr_persoana'.ljust(11)}"
          f"\t{'t_servire'.center(9)}"
          f"\t{'t_asteptare'.rjust(11)}")
    for poz, t_servire, t_asteptare in G:
        print(f"{poz:<11}\t{t_servire:^9}\t{t_asteptare:>11}")
    print(f"TMA este {TMA:.2f}")
L = citire()
G,TMA = Greedy(L)
afisare(G,TMA)
#%%
#Ex2
def citire():
    with open("lab9ex2.1.txt","r") as f:
        L = []
        for linie in f:
            ore, nume = linie.strip().split(maxsplit=1)
            inceput, sfarsit = ore.split('-')
            L.append((inceput,sfarsit,nume))
        return L
def Greedy(L):
    L.sort(key = lambda t: t[1])
    G = [L[0]]
    for i in range(1, len(L)):
        if L[i][0] >= G[-1][1]:
            G.append(L[i])
    return G

def afisare(G):
    with open("lab9ex2.2.txt","w") as g:
        for inceput, sfarsit, nume in G:
            g.write(f"{inceput}-{sfarsit} {nume}\n")
L = citire()
G = Greedy(L)
afisare(G)
#%%
#Ex3
def citire():
    with open("lab9ex3.1.txt","r") as f:
        L = []
        f.readline()
        for linie in f:
            l,c = linie.strip().split()
            L.append((int(l),c))
        return L
def Greedy(L):
    L.sort(key = lambda t: t[0], reverse = True)
    G = [L[0]]
    h = L[0][0]
    for i in range(1, len(L)):
        if L[i][1] != G[-1][1]:
            G.append(L[i])
            h += L[i][0]
    return G,h
def afisare(G,h):
    with open("lab9ex3.2.txt","w") as g:
        for l,c in G:
            g.write(f"{l} {c}\n")
        g.write("\n")
        g.write(f"Inaltime totala: {h}")
L = citire()
G,h = Greedy(L)
afisare(G,h)
#%%
#Ex4
def citire():
    with open("lab9ex4.1.txt","r") as f:
        L = [int(b) for b in f.readline().split()]
        L.sort(reverse = True)
        n = int(f.readline())
        return L,n
def Greedy(L,n):
    G = []
    for i in L:
        if n//i != 0:
            G.append((i,n//i))
            n = n%i
    return G
def afisare(G,n):
    with open("lab9ex4.2.txt","w") as g:
        g.write(f"{n}: {G[0][0]}*{G[0][1]} ")
        for i in range(1, len(G)):
            g.write(f"+ {G[i][0]}*{G[i][1]} ")
L,n = citire()
G = Greedy(L,n)
afisare(G,n)
#%%
#Ex5
def citire():
    with open("lab9ex5.txt","r") as f:
        f.readline()
        h = int(f.readline())
        L = [int(i) for i in f.readline().split()]
        L.sort()
        return L,h
def Greedy(L,h):
    i = 1
    nr = 0
    while i < len(L):
        if L[i]-L[i-1]<=h:
            nr += 1
            i += 2
        else:
            i += 1
    return nr
L,h = citire()
nr = Greedy(L,h)
print(nr)