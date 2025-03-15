#%%f
f = open("pb1.in", "r")
text = f.read()
f.close()

g = open("pb1.out", "w")
g.write(text)
g.close()
#%%v2
f = open("pb1.in", "r")
g = open("pb1.out", "w")
while True:
    linie = f.readline()
    if linie == "":
        f.close()
        g.close()
        break
    g.write(linie)
#%%v3
# f = open("pb1.in", "r")
# L_linii = f.readlines()
# f.close()

# while open("pb1.out", "w") as g:
#     # g.writelines(L_linii)
#     g.write("".join(L_linii))
#%%
#Problema2
f = open('text.in', 'r')
g = open('text.out', 'w')
nota = 1
for linie in f:
    aux, rez = linie.split('=')
    x, y = aux.split('*')
    x, y, rez = int(x), int(y), int(rez)
    if x*y == rez:
        nota += 1
        g.write(f'{linie.strip()} corect\n')
    else:
        g.write(f'{linie.strip()} gresit\n')
        
g.write(f'Nota: {nota}')
g.close()
f.close()
#%%
#Problema3
m, n = [int(x) for x in input("m, n= ").split()]
matr = [[int(x) for x in input(f"Linia {i}: ").split()] 
        for i in range(m)]
# for linie in matr:
#     for x in linie:
#         print(x, end=" ")
#     print()
for linie in matr:
    print(*linie)
L_maxime = [max(linie) for linie in matr]
print(L_maxime)
#%%
#Problema4
f = open("pb.in","r")
m,n = [int(x) for x in f.readline().split()]
matr = [[int(x) for x in linie.split()] for linie in f]

k = int(input("k = "))

#matr.insert(k+1,[0 for _ in range()])
matr.insert(k+1,[0]*n)

print(*matr,sep="\n")
print()
#%%
#Problema4_2
f = open("pb.in","r")
m,n = [int(x) for x in f.readline().split()]
matr = [[int(x) for x in linie.split()] for linie in f]

k = int(input("k = "))

#matr[k+1:k+1] = [[0]*n]

#print(*matr,sep="\n")
#print()

g = open("pb4.out","w")
# g.writelines([' '.join([str(x) for x in linie]) + '\n'
#               for linie in matr])

g.write('\n'.join([' '.join([str(x) for x in linie])
              for linie in matr]))
g.close()
#%%
#Problema5

f = open("pb5.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
f.close()

# print(eval(f"{3}*{4}*{2}"))

L_prod = [eval('*'.join([str(x) for x in linie]))
          for linie in matr]

print(L_prod)

rez = L_prod.count(max(L_prod))

print(rez)
#%%
#Problema6

f = open("pb7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()

k = int(input("k = "))

# L = [1,2,3,4,5,6,7]
# k = 2 => [6,7,1,2,3,4,5]

matr2 = [linie[-k:] + linie[:-k] for linie in matr]

print(*matr2, sep="\n")
print()

#%%
#Problema7

f = open("pb7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()

nr_linii = len(matr)
nr_coloane = len(matr[0])

matr2 = [[matr[i][j] for i in range(nr_linii)]
         for j in range(nr_coloane)]

print(*matr2,sep='\n')
#%%
#Problema8
f = open("pb7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()

lista_par = [x for linie in matr for x in linie if not x%2]

print(lista_par)
print(f'Matricea contine {len(lista_par)} numere pare ,iar suma lor este {sum(lista_par)}')
#%%
#Problema9
f = open("pb7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()

L_sume = [sum(linie)-max(linie) for linie in matr]

print(L_sume)
#%%
#Problema10
f = open("pb7.in")
matr = [[int(x) for x in linie.split()] for linie in f]
print(*matr, sep="\n")
print()
f.close()

matr2 = [(matr[i] if not i%2 else matr[i][::-1])
           for i in range(len(matr))]

print(matr2)
#%%
#OBSERVATIE
L = [1, 2, 3, 4, 5, 6]
# # for x in L:
# #     if x % 2 == 0:
# #         x = -x ## NU se modifica lista
# # print(L)

for i in range(len(L)):
    if L[i] % 2 == 0:
        L[i] = -L[i] ## se modifica lista
print(L)
#%%
#Problema11
f = open("L5.ex11.txt", "r")
matr = [[int(x) for x in linie.split()] for linie in f]
cnt = 0
for i in range(len(matr)):
    for j in range(len(matr[i])):
        if matr[i][j]<0:
            cnt += 1 
print(cnt)
#%%
#Problema12
n,m = input("n,m = ").split()
n,m = int(n), int(m)
matr = []
cntg = 0
for i in range(0,n):
    matr.append([])
    ok = 1
    for j in range(m):
        matr[i].append(int(input(f"matr[{i}][{j}] = ")))
    cnt = matr[i][0]
    for j in range(1,m):
        if matr[i][j] != cnt:
            break
    else:
        cntg += 1
print(cntg)
#%%
#Problema13
f = open("L5.ex13.txt", "r")
m,n = 4, 6
matr = [[int(x) for x in linie.split()] for linie in f]
print(sorted(matr,key=sum))
#%%
#Problema14
n = int(input("n = "))
L = [1, 1]
i = 2
matr = []
while i < n*n:
    L.append((L[i-1]+L[i-2])%10)
    i += 1 
i = 0
while i < n:
    matr.append([])
    j = 0
    while j < n:
        matr[i].append(L[i*n+j])
        j += 1
    i += 1
print(matr)
#%%
#Problema15
n = int(input("n = "))
f = open("L5.ex15.txt", "r")
matr = [[int(x) for x in linie.split()] for linie in f]
L = []
for i in range(n):
    for j in range(n):
        if i > j and (i+j > n-1):
            L.append(matr[i][j])
d = {}
for i in range(len(L)):
    if L[i] not in d:
        d[L[i]] = 1 
    else:
        d[L[i]] += 1
M = [x for x in d.keys() if d[x]>1]
print(M)
#%%
#Problema16
n = int(input("n = "))
f = open("L5.ex16.txt", "r")
matr = [[int(x) for x in linie.split()] for linie in f]
for i in range(n):
    for j in range(i,n):
        matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
for i in range(n):
    matr[i] = matr[i][::-1]
print(matr)
#%%
#Problema17
T = [[" "," "," "],[" "," "," "],[" "," "," "]]
P = 0
while True:
    print()
    for i in range(3):
        print(T[i])
    print()
    if P == 0:
            mx, my = input("Player A: ").split()
            mx, my = int(mx), int(my)
            try:
                T[mx][my] = "X"
                P = 1
            except:
                print()
                print("Wrong values")

    else:
        try:
            mx, my = input("Player B: ").split()
            mx, my = int(mx), int(my)
            try:
                T[mx][my] = "O"
                P = 0
            except:
                print()
                print("Wrong values")
        except:
            print()
            print("Wrong amount of values")
#%%
#Problema18
#%%
#Problema19