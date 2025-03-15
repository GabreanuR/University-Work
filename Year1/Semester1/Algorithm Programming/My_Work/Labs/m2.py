#%%
#Ex1
def modifica_salariu(D,nume_angajat,nou_salariu):
    L = []
    D[nume_angajat][1] = nou_salariu
    for i in D.keys():
        L.append([i,D[i][1]])
    return L
def angajati_functie(D,functie):
    L = []
    for i in D.keys():
        if D[i][0] == functie:
            L.append([i,D[i][2]])
    return L
def adaugare_angajati(D,nume,func,sal,*prog):
    D[nume] = [func,sal,prog]
    return D
def calcul_total(D):
    L = []
    sumsal = 0
    sumore = 0
    nr_ang = 0
    for i in D.keys():
        nr_ang += 1
        sumsal += D[i][1]
        os = D[i][2][0].split(":")
        of = D[i][2][1].split(":")
        sumore += int(of[0])
        sumore -= int(os[0])
    sumsal = sumsal // nr_ang
    L.append([sumsal,sumore])
    return L
with open("m2.1.txt","r") as f:
    D = {}
    for linie in f:
        nume,func,sal,prog = linie.strip().split("%")
        nume = nume.strip()
        func = func.strip()
        sal = int(sal.strip())
        prog = prog.strip().split()
        D[nume] = [func,sal,prog]
print(modifica_salariu(D,"Popescu Ion",10000))
print()
print(angajati_functie(D,"Programator"))
print()
print(adaugare_angajati(D,"Razvan","ITist",20000,"09:00", "17:00"))
print()
print(calcul_total(D))
#%%
#Ex2
def sterge_nota_elev(D,idelev,materie):
    L = []
    if materie == "romana":
        D[idelev][1][0] = None
    if materie == "matematica":
        D[idelev][1][1] = None
    if materie == "informatica":
        D[idelev][1][2] = None
    L = D[idelev][1]
    return L
def medie_clasa_materie(D,materie):
    medie = 0
    nr_elevi = 0
    if materie == "romana":
        idmat = 0
    if materie == "matematica":
        idmat = 1
    if materie == "informatica":
        idmat = 2
    for i in D.keys():
        if D[i][1][idmat] != None:
            nr_elevi += 1
            medie += int(D[i][1][idmat])
    medie = medie / nr_elevi
    return medie
with open("m2.2.txt","r") as f:
    D = {}
    for linie in f:
        idelev,nume,note = linie.strip().split("%")
        idelev = int(idelev.strip())
        nume = nume.strip()
        rom,mate,info = note.strip().split()
        D[idelev] = [nume,[rom,mate,info]]
print(sterge_nota_elev(D, 2, "matematica"))
print(D)
print()
print(medie_clasa_materie(D,"romana"))
print(medie_clasa_materie(D,"matematica"))
print(medie_clasa_materie(D,"informatica"))
#%%
#Ex3
def citeste_informatii_banci(fisier):
    D = {}
    with open(fisier,"r") as f:
        for linie in f:
            idbanca,nume,numar,capital = linie.strip().split("%")
            idbanca = int(idbanca.strip())
            nume = nume.strip()
            numar = int(numar.strip())
            capital = float(capital.strip())
            D[idbanca] = [nume,numar,capital]
    return D
def sterge_banca(D,nume):
    L = []
    for i in D.keys():
        if D[i][0] == nume:
            del D[i]
            break
    for i in D.keys():
        L.append([D[i][0],D[i][1],D[i][2]])
    print(L)
    return D
def media_clienti_banca(D):
    medie = 0
    nrban = 0
    for i in D.keys():
        nrban += 1
        medie += D[i][1]
    medie = medie // nrban
    return medie
fis = "m2.3.txt"
D = citeste_informatii_banci(fis)
print(D)
print()
nume = "BRD"
D = sterge_banca(D, nume)
print()
print(D)
print()
print(media_clienti_banca(D))
#%%
#Ex4
def citeste_informatii_masini(fisier):
    D = {}
    with open(fisier,"r") as f:
        for linie in f:
            id_masina,marca,cap,nrkil = linie.strip().split("#")
            id_masina = int(id_masina.strip())
            marca = marca.strip()
            cap = float(cap.strip())
            nrkil = int(nrkil.strip())
            D[id_masina] = [marca,cap,nrkil]
    return D
def adauga_masina(D,id_masina,marca,cap,nrkil):
    L = []
    D[id_masina] = [marca,cap,nrkil]
    for i in D.keys():
        L.append([D[i][0],D[i][1],D[i][2]])
    return L
def media_kilometri_masina(D):
    medie = 0
    nrmas = 0
    for i in D.keys():
        nrmas += 1
        medie += D[i][2]
    medie = medie // nrmas
    return medie
fis = "m2.4.txt"
D = citeste_informatii_masini(fis)
print(D)
print()
L = adauga_masina(D,7,"Dacia",1.0,10000)
print(L)
print(D)
print()
print(media_kilometri_masina(D))
