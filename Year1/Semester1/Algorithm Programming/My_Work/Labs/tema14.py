#Ex1
#a)
# with open("L14.1.1.txt", "r") as f:
#     L = f.readline().strip().split()
#
# # lungMax[i] = lungimea maxima a subsirului care se termina cu cuvantul i
# # pred[i] = pozitia cuvantului predecesor in subsir fata de cuvantul i
#
# lungMax = [1]*len(L)
# pred = [-1]*len(L)
#
# for i in range(1, len(L)):
#     for j in range(i):
#         if L[j][-2:] == L[i][:2]:
#             if lungMax[i] < lungMax[j] + 1:
#                 lungMax[i] = lungMax[j] + 1
#                 pred[i] = j
#
# print(lungMax)
# print(pred)
#
# sol = []
# pozLungMax = lungMax.index(max(lungMax))
# poz = pozLungMax
# while poz  != -1:
#     sol.append(L[poz])
#     poz = pred[poz]
#
# print(sol)
#
# with open("L14.1.2.txt", "w") as g:
#     g.write('\n'.join(sol[::-1]))

#Ex2
# s = 'SUBSIR'
# t = 'RUSTICE'
#
# M = [[0]*(len(t)+1) for _ in range(len(s)+1)]
#
# for i in range(1,len(s)+1):
#     for j in range(1,len(t)+1):
#         if s[i-1] == t[j-1]:
#             M[i][j] = 1 + M[i-1][j-1]
#         else:
#             M[i][j] = max(M[i-1][j], M[i][j-1])
#
# for linie in M:
#     print(*linie)
#
# sol = []
# i = len(s)
# j = len(t)
#
# while i != 0 and j != 0:
#     if s[i-1] == t[j-1]:
#         sol.append(s[i-1])
#         i -= 1
#         j -= 1
#     else:
#         if M[i-1][j] > M[i][j-1]:
#             i -= 1
#         else:
#             j -= 1
#
# print(sol)
# print("".join(sol[::-1]))

#Ex3

# with open("L14.3.1.txt","r") as f:
#     n = int(f.readline())
#     L = f.readline().split()
#     M = int(f.readline())
# for i in range(n):
#     L[i] = int(L[i])
#
# d = {}  #suma platibila : ultimul numar adaugat la suma
#
# for x in L:
#     for s in list(d):
#         if x+s not in d and x+s <= M:
#             d[x+s] = x
#     if x not in d and x <= M:
#         d[x] = x
# print(d)
# sol = []
# s = M
# while s != d[s]:
#     sol.append(d[s])
#     s = d[s]
# print(sol)
# with open("L14.3.2.txt","w") as g:
#     g.write(" ".join(str(x) for x in sol))

#Ex5
with open("L14.5.1.txt","r") as f:
    n = int(f.readline())
    L = []
    for linie in f:
        L.append(linie.strip().split())
for i in range(n):
    L[i][0] = int(L[i][0])
L.sort()
print(L)
#hMax[i] = inaltimea maxima a turnului care se termina cu cubul i
#pred[i] = pozitia cubului anterior in turn cubului i
#nrTurnuri[i] = numar de turnuri de lungime maxima care se termina cu cubul i
hMax = [cub[0] for cub in L]
pred = [-1]*len(L)
nrTurnuri = [1]*len(L)
for i in range(1,len(L)):
    for j in range(i):
        if L[i][1] != L[j][1] and L[i][0] > L[j][0]:
            if hMax[i] < hMax[j] + L[i][0]:
                hMax[i] = hMax[j] + L[i][0]
                pred[i] = j
                nrTurnuri[i] = nrTurnuri[j]
            elif hMax[i] == hMax[j] + L[i][0]:
                nrTurnuri[i] += nrTurnuri[j]
print(hMax,pred,nrTurnuri,sep='\n')

pozhMax = hMax.index(max(hMax))
poz = pozhMax
sol = []

while poz != -1:
    sol += L[poz]
    poz = pred[poz]

print(sol,nrTurnuri[pozhMax])