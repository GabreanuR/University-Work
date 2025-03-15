#%%
#Problema 2
s = input("sirul este: ")
i = 0
while len(s) - 2 * i > 0:
    print(s[i:len(s)-i].center(len(s), "*"))
    i += 1
#%%
#Problema 3
s = input("sirul este: ")
t = input("subsirul este: ")
poz = s.find(t)
if poz==-1:
    print(f"Subsirul '{t}' nu a fost gasit in sirul \"{s}\" ")
else:
    while poz != -1:
        print(poz,end=" ")
        poz=s.find(t,poz+len(t))
#%%
#Problema 3_2
s = input("sirul este: ")
t = input("subsirul este: ")
poz = -len(t)
gasit = False
while True:
    try:
        poz=s.index(t,poz+len(t))
        print(poz,end=" ")
        gasit=True
    except ValueError:
        print("Gata Cautarea")
        break
if not gasit:
    print(f"Subsirul '{t}' nu a fost gasit in sirul \"{s}\" ")
#%%
#Problema 4
prop = input("sirul este: ")
s = input("corect este: ")
t = input("gresit este: ")
prop2=prop.replace(t,s)
print(prop2)
#%%
#Problema 4_2
prop = input("sirul este: ")
s = input("corect este: ")
t = input("gresit este: ")
nr_inlocuiri=int(input("nr_inlocuiri = "))
nr_aparitii = prop.count(t)
prop2=prop.replace(t,s,nr_inlocuiri)
print(prop2)
if nr_aparitii > nr_inlocuiri:
    print(f"textul contine prea multe greseli, doar {nr_inlocuiri} au fost corectate")
else: 
    print("Toate greselile au fost corectate")
#%%
#Problema 5
prop = "Mancare Ana are mere si mancare sau are"
s = "are"
t = "VREA"
poz = prop.find(s)
while poz != -1:
    if (poz == 0 or prop[poz-1]==" " in " .?::!,") \
        and (poz+len(s)==len(prop) or prop[poz+len(s)]==" "):
        prop = prop[:poz] + t + prop[poz+len(s):]
        poz = prop.find(s,poz+len(t))
    else:
        poz = prop.find(s,poz+len(s))
print(prop)
#%%
print(ord("A"))
print(chr(65))
text="da"
ord(text[0])
#%%
#Problema 6
text = input("text= ")
k = int(input("k= "))
text2 = ""
for x in text:
    if x.isalpha():
        if x.isupper():
            y=(ord(x)-ord("A")+k)%26+ord("A")
            text2 = text2 + chr(y)
        else:
            y=(ord(x)-ord("a")+k)%26+ord("a")
            text2 = text2 + chr(y)
    else:
        text2 += x
print(text2)
#%%
#Problema 6_2
text = input("text= ")
k = int(input("k= "))
text2 = ""
for x in text:
    if x.isalpha():
        if x.isupper():
            y=(ord(x)-ord("A")-k)%26+ord("A")
            text2 = text2 + chr(y)
        else:
            y=(ord(x)-ord("a")-k)%26+ord("a")
            text2 = text2 + chr(y)
    else:
        text2 += x
print(text2)
#%%
#Problema 7
text = input("text= ")
text2 = ""
for x in text:
    if x in "aeiouAEIOU":
        text2 += x + "p" + x.lower()
    else:
        text2 += x
print(text2)
#%%
#Problema 7_2
text = input("text= ")
text2 = ""
for i in range(len(text)):
    if text[i]=="p":
        if ord(text[i-1])==ord(text[i+1]) or abs(ord(text[i-1])-ord(text[i+1]))==abs(ord("A")-ord("a")):
            continue
        else:
            text2 += text[i]
    elif text[i] in "AEIOUaeiou":
        if text[i-1]=="p" and (text[i]==text[i-2] or abs(ord(text[i])-ord(text[i-2]))==abs(ord("A")-ord("a"))):
            continue
        else:
            text2 += text[i]
    else:
        text2 += text[i]
print(text2)
#%%
#Problema 8
text = input("text= ")
t = 0
i = 0 
while i < len(text):
    x = 0
    while text[i].isdigit():
        x = x*10+int(text[i])
        i += 1
        continue
    t += x
    i += 1
print(t)
#%%
for i in range(5):
    print(i)
    i+=1
#VAI DE VIATA MEA CE E ASTA
#%%
#Problema 9
text = input("text= ")
text2 = ""
i = 0
while i < len(text):
    if text[i].isupper() and (text[i-1]==" " or i==0):
        text2 += text[i]
    i += 1
print(text2)
#%%
#Problema 10
x = input("x= ")
y = input("y= ")
i = 0
s = ""
while i < len(x):
    if (x[i] in "aeiou" ) and (y[i] in "aeiou"):
        s += "*"
    elif (x[i] not in "aeiou" ) and (y[i] not in "aeiou"):
        s += "#"
    else:
        s += "?"
    i += 1
print(s)
#%%
#Problema 11
text = input("x= ")
i = 0
while i < len(text):
    aux = text[:i]
    aux2 = text[-i-1:]
    if aux[:]==aux[::-1]:
        pref = text[:i]
    if aux2[:]==aux2[::-1]:
        suf = text[-i-1:]
    i += 1
print(pref)
print(suf)
#%%
#Problema 12
text = input("x= ")
i = 0
cnt = 0
l = 0
text2 = ""
while i < len(text):
    while True and (i < len(text)):
        if text[i] == " ":
            break
        cnt += 1
        i += 1
    if cnt > l:
        l = cnt
    cnt = 0
    i += 1
i = 0
cnt = 0
while i < len(text):
    while True and (i < len(text)):
        if text[i] == " ":
            break
        cnt += 1
        i += 1
    if cnt == l:
        aux = text[i-l:i]
        for j in range(len(aux)):
            if aux[j].isalpha():
                ok = 1
                break
            else:
                ok = 0
        if ok == 1:
            text2 += aux[::-1] + " "
        else:
            text2 += aux + " "
    else:
        aux = text[i-cnt:i]
        text2 += aux + " "
    cnt = 0
    i += 1
print(text2)
#%%
#Problema 13
text = input("x= ")
aux = text[::-1]
i = 0
nr = 0
while i < len(text):
    nr += (26**i) * (ord(aux[i])-ord("a"))
    i += 1
print(nr)
#%%
#Problema 14
text = input("x= ")
i = 0
aux = ""
ok = 1
j = 0
nr = 0
while i < len(text):
    while True and (i < len(text)):
        while text[i] == " ":
            nr += 1
            i += 1
            ok = 0
        if ok == 0:
            break
        cnt += 1
        i += 1
    if i == len(text):
        aux += text[j:i-nr]
    if ok == 0:
        aux += text[j:i-nr] + " " * nr
        j = i
        ok = 2
    if ok == 2:
        if text[i-nr-1] != text[j]:
            print(aux)
            aux = ""
    nr = 0
    i += 1
#%%
#Problema 15
s1 = input("s1= ")
s2 = input("s2= ")
i = 0
ok = 0
while i < len(s1):
    while True and (i < len(s1)):
        if s1[i] != s2[i]:
            ok = 1
            break
        i += 1
    if ok == 1:
        break
j = 0
aux1 = s1[::-1]
aux2 = s2[::-1]
ok = 0
while j < len(aux1):
    while True and (j < len(aux1)):
        if aux1[j] != aux2[j]:
            ok = 1
            break
        j += 1
    if ok == 1:
        j -= 1
        break
if (j + i) == len(s1):
    print(True)
else:
    print(False)