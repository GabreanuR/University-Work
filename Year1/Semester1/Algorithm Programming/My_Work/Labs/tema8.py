#%%
#1
#str.maketrans()

s = input()
#table = str.maketrans(".,;:","    ")#!!!METODA STATICA
separatori = ".,:;?!"
table = str.maketrans(separatori, " "*len(separatori))

print(table,type(table))#dictionar de coduri ascii
s=s.translate(table)
print(s)
#%%
#2 si 3
s = input()
vocale = "aeiou"
vocale1 = "".join([chr(ord(x)+1) for x in vocale])
print(vocale1)
#table = "".maketrans("aeiou","bfjpv")
#table = "".maketrans(vocale,vocale1)
table = "".maketrans(vocale,vocale1,",.:;")
print(table)
s=s.translate(table)
print(s)
#%%
#4
s = input()
d = {"1": "unu", "2": "doi", "3": "trei", "4": "patru"}
table = str.maketrans(d)
print(table)
s = s.translate(table)
print(s)
#%%
import re
print(re.search(r"gr[ee]n","green"))
#%%
import re
def parola(sir):
    a = re.search(r"^[a-z]{1,5}$",sir)
    A = re.search(r"^[A-Z]{1,5}$",sir)
    c = re.search(r"^[0-9]{1,5}$",sir)
    print(a,A,c,sep="\n")
    if a or A or c:
        print(f"parola {sir} este slaba!")
parola("AA")
#%%
import re
def parola(sir):
     a = re.search(r"[a-z]",sir)
     A = re.search(r"[A-Z]",sir)
     c = re.search(r"[0-9]",sir)
     d = re.search(r"[a-zA-Z0-9]{6,9}",sir)  
     print(a,A,c,d,sep="\n")
     if a and A and c and d:
         print(f"parola {sir} este medie!")
parola("anaAr9&")