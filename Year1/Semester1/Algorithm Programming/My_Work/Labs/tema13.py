# with open("L13.3.1.txt","r") as f:
#     m, n = [int(x) for x in f.readline().split()]
#     M = [[int(x) for x in linie.split()] for linie in f]
#
# print(m,n)
# print(M)
#
# Smax = [[0]*n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if i == 0 and j == 0:
#             Smax[i][j] = M[i][j]
#         elif i == 0:
#             Smax[i][j] = Smax[i][j-1] + M[i][j]
#         elif j == 0:
#             Smax[i][j] = Smax[i-1][j] + M[i][j]
#         else:
#             Smax[i][j] = max(Smax[i-1][j], Smax[i][j-1]) + M[i][j]
# print()
# for linie in Smax:
#     print(*linie)
# L_traseu =[(m-1,n-1)]
# i = m-1
# j = n-1
# while i>0 and j>0:
#     if i>0 and (j == 0 or Smax[i-1][j] >= Smax[i][j-1]):
#         i -= 1
#     else:
#         j -= 1
#     L_traseu.append((i,j))
# print(L_traseu)
#
# with open("L13.3.2.txt","w") as g:
#     g.write(f'Suma este {Smax[-1][-1]}.\n')
#     g.writelines([f'{i+1} {j+1}\n'for i, j in L_traseu[::-1]])


## Problema 4

with open("L13.4.1","r") as f:
    L = [int(x) for x in f.readline().split()]
print(*L)

Smax = [0 for x in range(len(L))]
Smax[0] = L[0]
for i in range(1,len(L)):
    Smax[i] = max(L[i],Smax[i-1]+L[i])
    #sau
    # Smax[i] = L[i] + max(0,Smax[i-1])
print(*Smax)

suma_max = max(Smax)
poz_ultimul = Smax.index(suma_max)
poz_primul = poz_ultimul
while L[poz_primul] != Smax[poz_primul]:
    poz_primul -= 1
print(poz_primul,poz_ultimul)

with open("L13.4.2","w") as g:
    g.write(f"Suma este {suma_max}\n")
    g.write(" ".join([str(x) for x in L[poz_primul:poz_ultimul+1]]))