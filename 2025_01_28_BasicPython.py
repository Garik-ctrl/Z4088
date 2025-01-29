"""
Hodina Basic Python
28.01.2025
Skupina Z4088
"""
import random

"""
Příklad 1 sudé číslo
vstup: číslo
výstup: Je sudé/je liché
"""
num=int(print("Dej mi číslo: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
num=2
print(f"{num} is even")
print(str(num) + " is even")
print(str(num),"is even")

print(f"Toto je číslo {num}")

"""
For cyklus
FOR projdi něco IN něčem:
    dělej něco
"""


mesta=["Praha","Brno","Ostrava"]

for mesto in mesta:
    print(f"Nejlepší město je {mesto}")

cisla=[0,1,2,3,4,5,6,7,8,9]
for cislo in cisla[::-1]:
    if cislo==0:
        print("START!")
    else:
        print(f"Start za {cislo} sekund!")

slovo="Garik"
print(slovo.upper()) # všechna písmena převede na velká písmena
print(slovo.lower()) # všechna písmena převede na malá písmena
print(slovo.capitalize()) # všechna první písmena převede na velká písmena
print(slovo.count("a")) # počet výskytů v textu
print(slovo.find("5")) # první výskyt v textu
print(slovo.endswith("ik")) # Končí to daným textem? True/False
vek=input("Zadej svuj vek")
if vek.isnumeric():
    print("toto je číslo")
else:
    print("Zadaný vstup není číslo!!!")

for pismeno in slovo:
    print(pismeno)


"""
Příklad 2 samohlásky - a,e,i,o,u
vstup: slovo
vystupu: slovo bez samohlasek
Python 
Pthn
"""
slovo=input("Zadej mi slovo/větu: ")

for pismeno in slovo:
    if pismeno.lower()!="a":
        if pismeno.lower()!="e":
            if pismeno.lower() != "i":
                if pismeno.lower()!="o":
                    if pismeno.lower()!="u":
                        if pismeno.lower() != "y":
                            print(pismeno)
#2. řešení
samohlasky=["a","e","i","y","o","u"]
slovo=input("Zadej mi slovo/větu: ")
slovnik=[]
# funkce IN mi ověřuje, zadli se hledaný výraz objevuje v dané struktuře. Např "P" in "Python" -> True
for pismeno in slovo:
    if (pismeno.lower() in samohlasky) == False:
        slovnik.append(pismeno)
print(slovnik)
print("".join(slovnik))

"""
While cyklus

"""
i=0

while i<5:
    print(i)
    i+=1 #i=i+1

"""
Příklad 3 
dělitelné třemi
"""
start=1
konec=100
delitelne_tremi=[]
while start<konec:
    if start%3==0:
        delitelne_tremi.append(start)
    start+=1
print(delitelne_tremi)

#2.řešení
delitelne_tremi=[]
for cislo in range(1,101):
    if cislo%3==0:
        delitelne_tremi.append(cislo)
print(delitelne_tremi)

"""
Příklad 4
vstup: seznam_cisel=[10,13,5,-4,2,6,9]
výstup: suma, rozdíl, součin
"""
seznam=[1,2,3]
suma=0
soucin=1
rozdil=0

for cislo in seznam:
    suma+=cislo
    soucin*=cislo
    rozdil-=cislo

print("Suma  je :",suma)
print("soucin je:", soucin)
print("Rozdil je:", rozdil)

"""
Příklad 5
hádáme číslo
Zadej cislo: 50
víc
Zadej cislo: 60
méně
Zadej cislo: 55
Vyhrál jsi
"""
import random as rn

cislo=rn.randint(1,101) #číslo, ktoré má užívateľ uhádnuť
uhodnul=False
while uhodnul==False:
    hadam_cislo=int(input("Hádaj číslo: "))
    print(hadam_cislo)
    if hadam_cislo>cislo:
        print("menej")
    elif hadam_cislo<cislo:
        print("viac")
    elif hadam_cislo==cislo:
        print("Uhádol si!")
        uhodnul=True


muj_list=[1,2,3,4,5,4,3,2,1]

print(f"Maximum je {max(muj_list)}")
print(f"Minimum je {min(muj_list)}")
print(f"Délka listu je {len(muj_list)}")
print(f"Suma je {sum(muj_list)}")
"""
SET
{}
"""
muj_set=set(muj_list)
print(muj_set)
muj_set2={1,2,2,2,5,4,-1,6,-90}
print(muj_set2)

muj_set2.add(-666) #přidání prvku
print(muj_set2)
muj_set2.update({0,1,2}) #přidání prvku
print(muj_set2)
muj_set2.remove(5) # odebrání prvku
print(muj_set2)
muj_set2.clear() #vyčistí aktuální set
print(muj_set2)

"""
Tuple
()
"""

muj_tuple=("jablka","pomeranče", "hrušky")
print(type(muj_tuple))
print(muj_tuple.count("jablka")) #spočítání prvků
muj_tuple=muj_tuple+("mandarinky",)
print(muj_tuple)

import math

print(math.sqrt(100))
print(math.gcd(100,50))
print(math.factorial(5))

import random as rn

muj_list=[1,2,3,4,5,4,3,2,1]
print(rn.choice(muj_list))

def soucet(a,b):
    return a+b

print(soucet(5,55))
