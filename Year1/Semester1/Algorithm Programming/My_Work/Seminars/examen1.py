# S1
# Ex1

# a = int(input("a = "))
# b = int(input("b = "))
# a = a ^ b
# b = a ^ b
# a = a ^ b
# print(f"a = {a}",f"b = {b}")

# Ex2

# import math
#
# n = int(input("n = "))
# if n & (n-1) == 0:
#     k = int(math.log2(n))
#     print(k)
# else:
#     print("n nu e putere a lui 2")

# Ex3

# n = int(input("n = "))
# k = 0
# while n != 0:
#     n = n & (n-1)
#     k += 1
# print(k)

# Ex4

# n = int(input("n = "))
# k = 0
# while n != 0:
#     n = n & (n << 1)
#     k += 1
# print(k)

# Ex5

# 100 -7 20 20 1 -7 1 3 100

# L = [int(x) for x in input("L = ").split()]
# v = 0
# for x in L:
#     v = v ^ x
# print(v)

# Ex6

# n = int(input("n = "))
# if n == 1:
#     print("1")
# else:
#     print("0")

# Ex7

# L = [int(x) for x in input("L = ").split()]
# sumL = sum(L)
# aux = max(L)
# aux2 = (aux * (aux + 1))//2
# print(aux2 - sumL)

# sau

# n = int(input("n = "))
# x = 0
# for i in range(1,n):
#     v = int(input("v = "))
#     x = x ^ v ^ i
# x = x ^ n
# print(x)

# S1 Tema

# Ex1

# L = [int(x) for x in input("L = ").split()]
# v = 0
# for x in L:
#     v = v ^ x
# print(v)

# Ex2

# n = int(input("n = "))
# if n == 1:
#     print("1")
# else:
#     print("0")

# Ex3

# x = int(input("x = "))
# y = int(input("y = "))
# x = x ^ y
# k = 0
# while x > 0:
#     x = x & (x-1)
#     k += 1
# print(k)

# Ex4

# x = int(input("x = "))
# k = 1
# if x & (x-1) == 0:
#     print(x)
# else:
#     while x != 0:
#         x = x >> 1
#         k = k << 1
#     print(k)

# Ex5

# n = int(input("n = "))
# k = 1
# x = n
# while x != 0:
#     x = x >> 1
#     k = k << 1
# k -= 1
# n = n ^ k
# k = 0
# while n != 0:
#     n = n & (n-1)
#     k += 1
# print(k)

# S2
# Ex1

# s = "abccabcababcc"
# t = "abc"
# for i in range (len(s)-len(t)):
#     if t in s[i:i+len(t)]:
#         print(i, end = " ")

# Ex2

# w = "mere"
# p = 2
# rima = w[-p:]
# L = ["pere","teste","programare"]
# for i in L:
#     if rima == i[-p:]:
#         print(i)
#
# # sau
# for i in L:
#     if i.endswith(rima):
#         print(i)

# Ex3

# L = "Ana are prune și gutui verzi, dar mai multe prune decât gutui!"
# separatori = ",.:;?!"
# for x in separatori:
#     L = L.replace(x, " ")
# D = {}
# crt = 0
# for x in L.strip().split():
#     if x not in D:
#         D[x] = len(x)
#         if len(x) > crt:
#             crt = len(x)
# for x in D.keys():
#     if D[x] == crt:
#         print(x)

# Ex4

# L1 = "where are WE GOING to?"
# L2 = "GOING To California By My Car"
# L3 = "by my SIDE, at The SeaSide"
# L4 = "walking over the rainbow"
# EX = ["a", "an", "by", "on", "in", "at", "to", "for", "ago", "the", "past", "over", "into", "onto"]
#
# rez = ""
# L = L4.split()
# q = len(L)-1
# cnt = 0
# for x in L:
#     x = x.lower()
#     separatori = ",.:;?!"
#     for y in separatori:
#         q = x.replace(y, " ")
#     if cnt == 0:
#         x = x.capitalize()
#     if cnt == q:
#         x = x.capitalize()
#     if len(q) >= 5:
#         x = x.capitalize()
#     if len(q) <= 4 and q not in EX:
#         x = x.capitalize()
#     L[cnt] = x
#     cnt += 1
# L = " ".join(L)
# print(L)

# Ex5

# s = "abcabcabc"
# n = len(s)
# for d in range(1, n//2 + 1):
#      if n % d == 0:
#         t = s[:d] * (n//d)
#      if t == s:
#          print("t = ", s[:d], "\nk = ", n//d)
#          break
# else:
#     print("Imposibil!")

# Ex6

# L = "Astăzi am cumpărat 5 kg de mere cu 2.30 RON kilogramul și 2 pâini a câte 5 lei bucata."
# L = L.strip().split()
# L2 = []
# s = 0
# for i in L:
#     if i[0].isnumeric():
#         if "." in i:
#             L2.append(float(i))
#         else:
#             L2.append(int(i))
# for i in range(0,len(L2),2):
#     s += L2[i]*L2[i+1]
# print(s)

# S2 Tema

# # Ex1
#
# w = "mere"
# L = ["pere", "teste", "mure"]
# w = len(w)
# for i in L:
#     if len(i) == w:
#         print(i)

# Ex2

# L = "Ana are prune și gutui verzi, dar mai multe prune decât gutui!"
# separatori = ".,?!:;"
# for x in separatori:
#     L = L.replace(x, " ")
# L = set(L.strip().split())
# print(len(L))

# Ex3

# L = "Ana are prune și gutui verzi, dar mai multe prune decât gutui!"
# L = L.replace(" ", "")
# L = L.strip()
# print(len(L))

# Ex4

# L = "Ana are prune și gutui verzi, dar mai multe prune decât gutui!"
# k = int(input("k = "))
# L2 = []
# for i in L:
#     if i.isalpha():
#         i = ord(i)
#         if "a" <= chr(i) <= "z":
#             i -= ord('a')
#             i += k
#             i = i % 26
#             i += ord('a')
#         if "A" <= chr(i) <= "Z":
#             i -= ord('A')
#             i += k
#             i = i % 26
#             i += ord('A')
#         i = chr(i)
#         L2.append(i)
#     else:
#         L2.append(i)
# L2 = "".join(L2)
# print(L2)

# S3

# Ex1

# with open("S3.1.1.txt","r") as f:
#     L = f.readline().strip().split()
#     x = 0
#     for i in L:
#         x += int(i)
#     g = len(L) + 1
#     s = (g*(g+1))//2 - x
# print(s)

# Ex2

# with open("S3.2.1.txt","r") as f:
#     D = {}
#     init = f.readline().strip().split()
#     for item in init:
#         D[item] = 1
#     for lista in f.readlines():
#         for key in D:
#             if key not in lista.strip().split():
#                 D[key] = 0
# for item in D:
#     if D[item] != 0:
#         print(item, end = " ")

# Ex3

# try:
#      f = open("S3.3.1.txt")
#      text = f.read().lower()
#      f.close()
# except FileNotFoundError:
#      print("Fisier inexistent!")
#      exit(0)
# for c in ",.:;?!":
#      text = text.replace(c, " ")
# d = {}
# for cuvant in text.split():
#      litere = frozenset(cuvant)
#      if litere in d:
#         d[litere].add(cuvant)
#      else:
#         d[litere] = set([cuvant])
# aux = [("".join(sorted(k)), sorted(v)) for (k,v) in d.items()]
# def cheieLitere(t):
#     return -len(t[0]), t[0]
# aux = sorted(aux, key=cheieLitere)
# f = open("S3.3.2.txt", "w")
# for p in aux:
#     f.write("Literele " + p[0] + ": " + ", ".join(p[1]) + "\n")
# f.close()

# Ex4

# s = "emerit"
# t = "treime"
# if len(t) == len(s):
#     D1 = {}
#     D2 = {}
#     for i in s:
#         if i not in D1:
#             D1[i] = 1
#         else:
#             D1[i] = D1[i] + 1
#     for i in t:
#         if i not in D2:
#             D2[i] = 1
#         else:
#             D2[i] = D2[i] + 1
#     if D1 == D2:
#         print("Da, sunt anagrame")
#     else:
#         print("Nu, nu sunt anagrame")
# else:
#     print("Nu, nu sunt anagrame")

# S3 Tema

# Ex 1

# s = "emerit"
# t = "treime"
# v = [0] * 26
# for i in s:
#     v[ord(i) - ord('a')] += 1
# for i in t:
#     v[ord(i) - ord('a')] -= 1
# for i in v:
#     if i != 0:
#         print("Nu sunt anagrame")
#         break
# else:
#     print("Sunt anagrame")

# Ex 2

s = "emerit"
# t = "treime"
# v = [0] * 26
# for i in s:
#     v[ord(i) - ord('a')] += 1
# for i in t:
#     v[ord(i) - ord('a')] -= 1
# for i in v:
#     if i != 0:
#         print("Nu sunt anagrame")
#         break
# else:
#     L = [[i + 1 for i in range(len(s))],[]]
#     for i in range(len(s)):
#         if s[i] in t:
#             L[1].append(t.index(s[i])+1)
#             t = t[:(t.index(s[i]))] + "." + t[(t.index(s[i])+1):]
#             print(t)
#     print(L[0],L[1],sep="\n")

# Ex3

# with open("S3.tema.3.1.txt","r") as f:
#     x = f.read()
#     separatori = ".,?!:;"
#     for c in separatori:
#         x = x.replace(c,"")
#     D = {}
#     for cuv in x.strip().split():
#         if len(cuv) not in D:
#             D[len(cuv)] = [cuv.lower()]
#         else:
#             D[len(cuv)].append(cuv.lower())
# with open("S3.tema.3.2.txt","w") as g:
#     L = []
#     for i in sorted(D.keys(),reverse=True):
#         L.append((i,D[i]))
#     for i,v in L:
#         g.write("Lungime "+str(i)+": "+", ".join(v)+"\n")

# Ex3 V1

# with open("S3.tema.4.txt","r") as f:
#     L = []
#     for line in f.readlines():
#         for nr in line.strip().split():
#             for i in nr:
#                 L.append(i)
#     L.sort(reverse=True)
#     nrmax = "".join(L)
#     L.sort()
#     if L[0] == "0":
#         for i in L:
#             if i != "0":
#                 L.remove(i)
#                 L.insert(0,i)
#                 break
#     nrmin = "".join(L)
#     print(f"nrmax = {nrmax}")
#     print(f"nrmin = {nrmin}")

# S4

# Ex1

# def m_triunghi(n):
#     M = [[i] for i in range(1,n+1)]
#     lmax = 0
#     for i in range(n-1,0,-1):
#         M[n-1].append(i)
#     for i in range(n-2,0,-1):
#         for j in range(1,i+1):
#             M[i].append(M[i+1][j-1]+M[i][j-1]+M[i+1][j])
#             if len(str(M[i][j])) > lmax:
#                 lmax = len(str(M[i][j]))
#     return M,lmax
#
# n = int(input("n = "))
# M,lmax = m_triunghi(n)
# for i in range(len(M)):
#     for j in range(len(M[i])):
#         x = str(M[i][j])
#         print(x.rjust(lmax+1),end="")
#     print()

# Ex2

# def liste(*L,nr):
#     M = []
#     for i in range(len(L)):
#         if nr in L[i]:
#             M.append([i,L[i]])
#     return M
# L1 = [1, 4, 7, 3, 9, 10]
# L2 = [1, 4, 8, 7, 9, 10, 22]
# L3 = [7, 3, 5, 1]
# L4 = [1, 4, 7, 6, 9, 10]
# x = int(input("x = "))
# M = liste(L1,L2,L3,L4, nr = x)
# for i in M:
#     print(f"Lista {i[0]+1} : {i[1]}")

# Ex3

# def citire(fis):
#     L = []
#     with open(fis, 'r') as f:
#         for line in f.readlines():
#             nume, grupa, note = line.split(",",maxsplit=2)
#             nume = nume.strip()
#             grupa = int(grupa.strip())
#             note = note.strip().split(",")
#             for i in range(len(note)):
#                 note[i] = int(note[i].strip())
#             L.append((nume, grupa, note))
#     return L
#
# def promovare(L):
#     D = {True:[], False:[]}
#     for t in L:
#         if 0 in t[2]:
#             D[False].append(t)
#         else:
#             D[True].append(t)
#     return D
#
# def fsort1(L):
#     L2 = []
#     for t in L.keys():
#         for i in range(len(L[t])):
#             L2.append(L[t][i])
#     L2.sort(key=lambda x: (x[1],x[0]))
#     return L2
#
# def fsort2(L):
#     L2 = []
#     L2.append(L[True])
#     L2.append(L[False])
#     L2[0].sort(key=lambda x: x[0])
#     L2[1].sort(key=lambda x: x[0])
#     return L2
#
# def fsort3(L):
#     L2 = []
#     for t in L.keys():
#         for i in range(len(L[t])):
#             L2.append(L[t][i])
#     L2.sort(key=lambda x: (-sum(x[2]),x[1],x[0]))
#     return L2
#
# fis = "S4.3.1.csv"
# L = citire(fis)
# D = promovare(L)
# L = fsort1(D)
# for i in L:
#     print(i)
# print()
# L = fsort2(D)
# for i in L:
#     print(*i)
# print()
# L = fsort3(D)
# for i in L:
#     print(i)
# print()

# Ex4

# def numarare(colectie, proprietate):
#      contor = 0
#      for element in colectie:
#         if proprietate(element) == True:
#             contor = contor + 1
#      return contor
#
# def nrpar(i):
#     if i%2 == 0:
#         return True
#     else:
#         return False
#
# def nrvoc(i):
#     if i in "aeiouAEIOU":
#         return True
#     else:
#         return False
#
# def nrper(i):
#     if i[0] == i[1]:
#         return True
#     else:
#         return False
#
# def nrlen(i):
#     if len(i) == k:
#         return True
#     else:
#         return False
#
# L = [1, 4, 8, 7, 9, 10, 22]
# s = "Ana are mere si pere"
# L2 = [(1,1),(3,4),(5,5),(7,8),(9,10),(11,11),(12,13)]
# L3 = ["ana","merge","si","pere","are"]
# cnt = numarare(L, nrpar)
# print(cnt)
# cnt = numarare(s, nrvoc)
# print(cnt)
# cnt = numarare(L2, nrper)
# print(cnt)
# k = int(input("k = "))
# cnt = numarare(L3, nrlen)
# print(cnt)

# S4 Tema

# Ex1

# def mpat(n):
#     M = [[]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             M[i].append(0)
#     for i in range(n):
#         M[i][n-1] = 1
#     for i in range(n):
#         M[n-1][i] = 1
#     for i in range(n-2, -1, -1):
#         for j in range(n-2, -1, -1):
#             M[i][j] += M[i+1][j] + M[i][j+1]
#     return M
#
# n = int(input("n = "))
# M = mpat(n)
# lmax = len(str(M[0][0]))
# for i in range(n):
#     for j in range(n):
#         print(str(M[i][j]).rjust(lmax), end=" ")
#     print()

# Ex2

# def pozitie(col,prop):
#     L = []
#     for i in range(len(col)):
#         if prop(col[i]) == True:
#             L.append(i)
#     return L
#
# def poz(i):
#     return i>0
#
# def nan(i):
#     if i.isalnum():
#         return False
#     elif i == " ":
#         return False
#     else:
#         return True
#
# T = (1, -1, 9, 4, 0, -3)
# L = pozitie(T,poz)
# print(L)
# s = "Ana, Mihai, Ella si Andrei merg la magazin."
# L = pozitie(s,nan)
# print(L)

# colov

# with open("colcv.txt","r") as f:
#     s = 0
#     cnt = 0
#     for line in f:
#         cod, nota = line.split()
#         s += float(nota)
#         cnt += 1
#     s /= cnt
#     print(s)

# MODEL TEST DE LABORATOR

# Ex1

# with open("ex1.1.txt","r") as f:
#     M = []
#     for line in f:
#         M.append(line.strip().split())
#     for i in range(len(M)):
#         for j in range(len(M[i])):
#             M[i][j] = int(M[i][j])
#         M[i].remove(max(M[i]))
#         M[i].remove(max(M[i]))
#     for i in range(len(M)):
#         for j in range(len(M[i])):
#             M[i][j] = str(M[i][j])
# with open("ex1.2.txt","w") as g:
#     for m in M:
#         g.write(" ".join(m) + "\n")

# Ex2

# with open("ex2.1.txt","r") as f:
#     D = {}
#     for line in f.readlines():
#         for word in line.split():
#             word2 = word.lower()
#             if word2 not in D:
#                 D[word2] = 1
#             else:
#                 D[word2] += 1
#     D2 = {}
#     for word in D.keys():
#         if D[word] not in D2:
#             D2[D[word]] = [word]
#         else:
#             D2[D[word]].append(word)
#     L = [x for x in D2.items()]
#     L.sort(key=lambda x:x[0], reverse=True)
# with open("ex2.2.txt","w") as g:
#     for line in L:
#         frecv, words = line
#         g.write("Frecventa " + str(frecv) + ": " + ", ".join(words) + "\n")

# Ex3

# a)

# def sterge_ore(D,cinema,film,*ore):
#     ore = ore[0]
#     for i in range(len(D[cinema])):
#         if film in D[cinema][i]:
#             for j in ore:
#                 if j in D[cinema][i][film]:
#                     D[cinema][i][film].remove(j)
#     L = D[cinema]
#     return L
#
# def cinema_film(D, *cinematografe, ora_minima, ora_maxima):
#     L = []
#     cinematografe = cinematografe[0]
#     for i in cinematografe:
#         for j in D[i]:
#             print(j)
#     return L
#
# with open("ex3.1.txt","r") as f:
#     D = {}
#     for line in f:
#         nume_cinematograf, nume_film, ore_de_difuzare = line.strip().split("%")
#         nume_cinematograf = nume_cinematograf.strip()
#         nume_film = nume_film.strip()
#         ore_de_difuzare = ore_de_difuzare.strip().split()
#         if nume_cinematograf not in D:
#             D[nume_cinematograf] = [{nume_film: ore_de_difuzare}]
#         else:
#             D[nume_cinematograf].append({nume_film: ore_de_difuzare})
#
# c = "Cinema 2"
# f = "Minionii 2"
# o = ["15:00", "20:30"]
# L = sterge_ore(D,c,f,o)
# print(L)
# print(D)
# cinematografe = ["Cinema 1", "Cinema 2", "Cinema 3"]
# omin = "10:00"
# omax = "18:00"
# L = cinema_film(D,cinematografe,ora_minima=omin,ora_maxima=omax)
# print(L)

# Ex1


# # b)
#
# def modifica_salariu(D,nume_angajat,nou_salariu):
#     L =[]
#     D[nume_angajat]["salariu"] = nou_salariu
#     for i in D.keys():
#         L.append([i,D[i]["salariu"]])
#     return L
#
# # c)
#
# def angajati_funcție(D, functie):
#     L = []
#     for x in D.keys():
#         if functie in D[x]["functie"]:
#             L.append([x,D[x]["salariu"],D[x]["program_de_lucru"]])
#     L.sort(key=lambda x:x[0])
#     return L
#
# # a)
#
# with open("ex4.1.txt","r") as f:
#     D = {}
#     for linie in f.readlines():
#         nume_angajat, functie, salariu, program_de_lucru = linie.split("%")
#         nume_angajat = nume_angajat.strip()
#         functie = functie.strip()
#         salariu = int(salariu.strip())
#         program_de_lucru = program_de_lucru.strip().split()
#         D[nume_angajat] = {"functie": functie, "salariu": salariu, "program_de_lucru": program_de_lucru}
#
# L = modifica_salariu(D,"Marin Alexandru",10000)
# print(L)
# L = angajati_funcție(D, "Programator")
# print(L)

# Ex1

# def min_max(L):
#     return min(L), max(L)
#
# def incarca_fisier(fisier):
#     L = []
#     j = 0
#     with open(fisier, "r") as f:
#         for linie in f.readlines():
#             L.append(linie.strip().split())
#             for i in range(len(L[j])):
#                 L[j][i] = int(L[j][i])
#             j += 1
#     return L
#
# L = [3, -3, 1, 7, 3, 2]
# minL, maxL = min_max(L)
# print(minL, maxL)
# L = incarca_fisier("ex5.1.txt")
# print(L)
#
# fisier = "ex5.1.txt"
# with open("ex5.1.2.txt", "w") as g:
#     with open(fisier, "r") as f:
#         q = 0
#         for linie in f.readlines():
#             L = linie.strip().split()
#             for i in range(len(L)):
#                 L[i] = int(L[i])
#             ok = False
#             if len(L) > 0:
#                 x = L[0]
#                 ok = True
#             for i in range(len(L)):
#                 if L[i] != x:
#                     ok = False
#                     break
#             if ok is True:
#                 g.write(str(q) + "\n")
#             q += 1
#
# L = incarca_fisier(fisier)
# ming = None
# maxg = None
# for i in range(len(L)):
#     minl, maxl = min_max(L[i])
#     if ming is None:
#         ming = minl
#     elif minl < ming:
#         ming = minl
#     if maxg is None:
#         maxg = maxl
#     elif maxl > maxg:
#         maxg = maxl
# print(ming, maxg)

# Ex2

# def deviruseaza(prop):
#     L = prop.strip().split()
#     L1 = []
#     for i in range(len(L)-1,-1,-1):
#         L1.append(L[i])
#     for i in range(len(L1)):
#         L1[i] = list(L1[i])
#         L1[i][0], L1[i][len(L1[i])-1] = L1[i][len(L1[i])-1], L1[i][0]
#         L1[i] = "".join(L1[i])
#     L = " ".join(L1)
#     return L
#
# prop = "aorectc aropozitip este aceasta"
# prop = deviruseaza(prop)
# print(prop)
#
# def prime(n, numar_maxim = 0):
#     L = []
#     if numar_maxim != 0:
#         ok = numar_maxim
#     if n == 2:
#         L = [2]
#         return L
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             L.append(i)
#             if numar_maxim != 0:
#                 ok -= 1
#                 if ok == 0:
#                     break
#     return L
#
# n = 20
# L = prime(n)
# print(L)
#
# with open("ex7.1.txt","r") as f:
#     with open("ex7.2.txt","w") as g:
#         cnt = 1
#         for linie in f.readlines():
#             linie = linie.strip()
#             if cnt in prime(cnt):
#                 linie = deviruseaza(linie)
#             g.write(linie + "\n")
#             cnt += 1

# Ex3

# def cifra_control(n):
#     r = n % 9
#     if r == 0:
#         return 9
#     else:
#         return r
#
# def insereaza_cifra_control(L):
#     for i in range(len(L)):
#         L[i] = [L[i],cifra_control(L[i])]
#
# def egale(*L):
#     L = list(L)
#     q = L[0]
#     for i in range(1,len(L)):
#         if L[i] != q:
#             return False
#     else:
#         return True
#
# n = 20
# print(cifra_control(n))
# L = [10, 78, 8051, 91]
# L1 = [10, 78, 8051, 91]
# L2 = [10, 78, 8051, 91]
# insereaza_cifra_control(L)
# print(L)
# L = [10, 78, 8051, 91]
# print(egale(L,L1,L2))

#############################################

# Ex1

# def insereaza_legatura(D,pct1,pct2,culoare,eticheta):
#     for i in D.keys():
#         if D[i][0] == pct1 and D[i][1] == pct2:
#             return False
#     D[eticheta] = [pct1,pct2,culoare]
#     return True
#
# def vecini(D,*puncte):
#     L = []
#     puncte = list(puncte)
#     for i in D.keys():
#         if D[i][0] in puncte:
#             if D[i][0] == puncte[0]:
#                 L.append(D[i][1])
#         if D[i][1] in puncte:
#             if D[i][1] == puncte[0]:
#                 L.append(D[i][0])
#     L.sort(key=lambda x: -x[1])
#     return L
#
# with open("ex6.1.txt","r") as f:
#     D = {}
#     for linie in f.readlines():
#         pct1, pct2, culoare, eticheta = linie.strip().split(" ",maxsplit=3)
#         pct1 = pct1.replace("[","")
#         pct2 = pct2.replace("[", "")
#         pct1 = pct1.replace("]", "")
#         pct2 = pct2.replace("]", "")
#         pct1 = pct1.split(",")
#         pct2 = pct2.split(",")
#         pct1[0], pct1[1] = int(pct1[0]), int(pct1[1])
#         pct2[0], pct2[1] = int(pct2[0]), int(pct2[1])
#         D[eticheta] = [pct1, pct2, culoare]
#     print(D)
#
# print(insereaza_legatura(D,[1,3],[2,7],"negru","legatura noua"))
#
# for i in D.keys():
#     print(*D[i],i)
#
# L = vecini(D,[2,7],[1,2])
# print(L)

# GREEDY

# EX1

# t = [7, 6, 3, 10, 6, 3]
# L = []
# for i in range (len(t)):
#     L.append((i+1,t[i]))
# L.sort(key=lambda x: x[1])
# scrt = 0
# stot = 0
# for i in range (len(L)):
#     scrt = scrt + L[i][1]
#     stot = stot + scrt
# print(stot/len(L))

# EX2

# with open("ex8.1.txt","r") as f:
#     L = []
#     cnt = 1
#     for linie in f.readlines():
#         s,f = linie.strip().split("-")
#         L.append([cnt,s,f])
#         cnt += 1
#
# L.sort(key=lambda x: x[2])
# S = [L[0]]
# for i in range(1, len(L)):
#     if L[i][1] >= L[i-1][2]:
#         S.append(L[i])
# with open("ex8.2.txt","w") as g:
#     g.write(f"Numarul maxim de spectacole: {len(S)}\n")
#     g.write("\n")
#     g.write("Spectacole programate: \n")
#     for i in range(len(S)):
#         g.write(f"{S[i][1]}-{S[i][2]} Spectacol {S[i][0]}\n")

# EX3

# import queue
#
# with open("ex9.1.txt","r") as f:
#     L = []
#     cnt = 1
#     for linie in f.readlines():
#         s,f = linie.strip().split("-")
#         L.append((cnt,s,f))
#         cnt += 1
#     L.sort(key=lambda x: x[1])
#
# sali = queue.PriorityQueue()
# sali.put((L[0][2],list((L[0],))))
#
# for k in range(1,len(L)):
#     min_timp_final = sali.get()
#     if L[k][1] >= min_timp_final[0]:
#         min_timp_final[1].append(L[k])
#         sali.put((L[k][2], min_timp_final[1]))
#     else:
#         sali.put(min_timp_final)
#         sali.put((L[k][2], list((L[k],))))
#
# with open("ex9.2.txt","w") as g:
#     g.write("Numar minim de sali: " + str(sali.qsize()) + "\n")
#     scrt = 1
#     while not sali.empty():
#         sala = sali.get()
#         print(sala)
#         g.write("\nSala " + str(scrt) + ":\n")
#         for sp in sala[1]:
#             g.write("\t" + sp[1] + "-" + sp[2] + " Spectacol " + str(sp[0]) + "\n")
#             scrt += 1

# EX4

# with open("ex10.1.txt","r") as f:
#     G = float(f.readline())
#     L = []
#     crt = 1
#     for linie in f.readlines():
#         g,c = linie.strip().split()
#         L.append((crt,float(g),float(c)))
#         crt += 1
#
# V = []
# for i in range(0,len(L)):
#     V.append((L[i][2]/L[i][1],L[i]))
#
# V.sort(key=lambda x:x[0],reverse=True)
#
# cmax = 0
# n = len(V)
# S = []
# for i in range(0,len(V)-1):
#     if G > 0:
#         if V[i][1][1] <= G:
#             G -= V[i][1][1]
#             cmax += V[i][1][2]
#             S.append((V[i][1], "100.00%"))
#         elif V[i][1][1] >= G:
#             cmax += V[i][0]*G
#             x = (V[i][0]*G*100)/V[i][1][2]
#             x = int(x)
#             x = str(x) + ".00%"
#             S.append((V[i][1], x))
#             G = 0
#     else:
#         break
#
# with open("ex10.2.txt","w") as g:
#     g.write("Castigul maxim: " + str(cmax) + "\n")
#     g.write("\n")
#     g.write("Obiectele incarcate: \n")
#     for i in range(0,len(S)):
#         g.write("Obiecte " + str(S[i][0][0]) + ": " + S[i][1] + "\n")

# EX5

# L = [2,4,6,8,10,12,14]
# print(sum(L))
#
# def DI(L,st,dr):
#     if st == dr:
#         #conditia de oprire
#         return L[st]
#     else:
#         #etapa divide
#         mij = (st+dr)//2
#         solst = DI(L,st,mij)
#         soldr = DI(L,mij+1,dr)
#     #etapa impera
#     return solst+soldr
#
#
# print(DI(L,0,len(L)-1))

# EX6
# L = [2,4,6,8,10,12,14]
# x = 2
#
# def cautare(L,x,st,dr):
#     if st > dr:
#         return -1
#     mij = (st+dr)//2
#     if L[mij] == x:
#         return mij
#     elif x < L[mij]:
#         return cautare(L,x,st,mij-1)
#     else:
#         return cautare(L, x, mij + 1, dr)
#
# print(cautare(L,x,0,len(L)-1))

# EX7

# L = [7, 6, 6, 10, 3, 3]
#
# def interclasare(L,st,mij,dr):
#     i = st
#     j = mij + 1
#     aux = []
#     while i <= mij and j <= dr:
#         if L[i] <= L[j]:
#             aux.append(L[i])
#             i += 1
#         else:
#             aux.append(L[j])
#             j += 1
#     aux.extend(L[i:mij + 1])
#     aux.extend(L[j:dr + 1])
#     L[st:dr + 1] = aux[:]
#
# def mergesort(L,st,dr):
#     if st < dr:
#         mij = (st+dr)//2
#         mergesort(L,st,mij)
#         mergesort(L,mij+1,dr)
#         interclasare(L,st,mij,dr)
#
# mergesort(L,0,len(L)-1)
# print(L)

# EX8

# import random
#
# A = [10, 7, 25, 4, 3, 4, 9, 12, 7]
#
# def quickselect(A, k, f_pivot=random.choice):
#     pivot = f_pivot(A)
#     L = [x for x in A if x < pivot]
#     E = [x for x in A if x == pivot]
#     G = [x for x in A if x > pivot]
#
#     if k < len(L):
#         return quickselect(L, k, f_pivot)
#     elif k < len(L) + len(E):
#         return E[0]
#     else:
#         return quickselect(G, k - len(L) - len(E), f_pivot)
#
# print(quickselect(A, 0))

# EX9

# def divizori(*n):
#     D = {}
#     for elem in n:
#         D[elem] = []
#         for i in range(2,elem+1):
#             if elem % i == 0:
#                 ok = 1
#                 for j in range(2,i):
#                     if i % j == 0:
#                         ok = 0
#                         break
#                 if ok == 1:
#                     D[elem].append(i)
#     return D
#
# print(divizori(50,21))
#
# L = [chr(x) for x in range(ord('a'), ord('a')+10)]
# print(L)

# EX10

# def bkt(k):
#     global s,n
#     for v in range(1,n+1):
#         s[k] = v
#         print(s)
#         if s[k] not in s[:k]:
#             if k == n:
#                 print(*s[1:], sep=",")
#             else:
#                 bkt(k + 1)
#
# n = int(input("n = "))
# # o soluție s va avea n elemente
# s = [0] * (n + 1)
# print("Toate permutările de lungime " + str(n) + ":")
# bkt(1)

# EX11 ARANJAMENTE

# def bkt(k):
#     global s,n,m
#     for i in range(1,n+1):
#         s[k] = i
#         if s[k] not in s[:k]:
#             if k == m:
#                 print(*s[1:],sep=",")
#             else:
#                 bkt(k+1)
#
# n = int(input("n = "))
# m = int(input("m = "))
# s = [0]*(m+1)
# bkt(1)

# EX11 COMBINARI

# def bkt(k):
#     global s,n,m
#     for i in range(1,n+1):
#         s[k] = i
#         if s[k] not in s[:k] and s[k-1] < s[k]:
#             if k == m:
#                 print(*s[1:],sep=",")
#             else:
#                 bkt(k+1)
#
# n = int(input("n = "))
# m = int(input("m = "))
# s = [0]*(m+1)
# bkt(1)

# EX11 COMBINARI 2

# def bkt(k):
#     global s,n,m,cnt
#     for v in range(s[k-1]+1,n+1):
#         s[k] = v
#         if k == m:
#             cnt += 1
#             print(str(cnt).rjust(3) + ". ", end="")
#             print(*s[1:],sep=",")
#         else:
#             bkt(k+1)
#
# n = int(input("n = "))
# m = int(input("m = "))
# s = [0]*(m+1)
# cnt = 0
# bkt(1)

# EX12

# def bkt(k):
#      global s, n, cuv, cuv_dist
#      for v in range(1, n+1):
#          s[k] = v
#          if s[k] not in s[1:k]:
#              if k == n:
#                  aux = "".join([cuv[s[i]-1] for i in range(1, n+1)])
#                  cuv_dist.add(aux)
#              else:
#                  bkt(k+1)
# cuv = input("Cuvantul: ")
# n = len(cuv)
# cuv_dist = set()
# s = [0] * (n+1)
# bkt(1)
# print("Anagramele distincte ale cuvântului " + cuv + ": ")
# print(*cuv_dist, sep="\n")

# EX13

# def bkt(k):
#     global s, n
#     for v in range(1, n-k+2):
#         s[k] = v
#         scrt = sum(s[:k+1])
#         if scrt <= n:
#             if scrt == n:
#                 print(*s[1: k + 1], sep="+")
#             else:
#                 bkt(k+1)
#
#
# n = int(input("n = "))
# s = [0]*(n+1)
# bkt(1)

# EX14

# def bkt(k):
#     global s, P, v, n
#     # s[k] = numarul de monede cu valoarea v[k] utilizate
#     for m in range(0, P // v[k] + 1):
#         s[k] = m
#         scrt = sum([s[i] * v[i] for i in range(k+1)])
#         if scrt <= P:
#             if scrt == P and k == n:
#                 for i in range(1, n+1):
#                     if s[i] != 0:
#                         print(s[i], "x", v[i], "$ + ", end="")
#                 print()
#             else:
#                 if k < len(v[1:]):
#                     bkt(k+1)
# P = int(input("Suma de plată: "))
# aux = [int(x) for x in input("Valorile monedelor: ").split()]
# v = [0]
# v.extend(aux)
# n = len(v[1:])
# s = [0]*(len(v))
# print("Toate modalitățile de plată:")
# bkt(1)

# def numere(*n):
#     D = {}
#     for i in n:
#         aux = str(i)
#         aux = list(aux)
#         lungime = len(aux)
#         for j in range(len(aux)):
#             aux[j] = int(aux[j])
#         aux = sum(aux)
#         med = aux/lungime
#         if med not in D.keys():
#             D[med] = [i]
#         else:
#             D[med].append(i)
#     return D
#
# D = numere(82375,201,51,73,3456,2855,1021,90,153)
# print(D)

# L = [x for x in range(100,1000) if (x//100 < (x//10)%10 < x%10)]
# print(L)

def cifre_comune(*n,x=135579):
    D = {}
    x = str(x)
    x = list(x)
    x = set(x)
    for i in x:
        D[i] = []
    n = list(n)
    for i in range(len(n)):
        n[i] = str(n[i])
        for j in D.keys():
            if j in n[i]:
                D[j].append(n[i])
    return D

D = cifre_comune(54572,9559,2024,75917)
print(D)