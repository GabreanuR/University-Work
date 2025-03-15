#%%
#EX1a
def completare(M,i,j,d):
    global k
    if d == 1:
        M[i][j] = k
        k += 1
        return
    completare(M, i, j + d // 2, d // 2)
    completare(M, i + d // 2, j, d // 2)
    completare(M, i, j, d // 2)
    completare(M, i + d // 2, j + d // 2, d // 2)
k = 1
n = int(input("n = "))
M = [[0] * 2**n for _ in range(2**n)]
completare(M, 0, 0, 2**n)
dimMax = len(str(2**n * 2**n))

for linie in M:
    for elem in linie:
        print(str(elem).rjust(dimMax), end=" ")
    print()
#%%
#EX1b
def completare(M,i,j,dn,dm):
    global k
    if dn*dm == 1:
        M[i][j] = k
        k += 1
        return
    if dn == 1:
        for p in range(dm):
            M[i][j+p] = k
        k += 1
        return
    if dm == 1:
        for p in range(dn):
            M[i+p][j] = k
        k += 1
        return
    completare(M, i, j + dm // 2, dn // 2, dm // 2)
    completare(M, i + dn // 2, j, dn // 2, dm // 2)
    completare(M, i, j, dn // 2, dm // 2)
    completare(M, i + dn // 2, j + dm // 2, dn // 2, dm // 2)
k = 1
n = int(input("n = "))
m = int(input("m = "))
M = [[0] * 2**m for _ in range(2**n)]
completare(M, 0, 0, 2**n, 2**m)
dimMax = len(str(2**n * 2**n))

for linie in M:
    for elem in linie:
        print(str(elem).rjust(dimMax), end=" ")
    print()