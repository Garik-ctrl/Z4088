"""
Hodina
29.01.2025
Skupina Z4088
"""

"""
Příklad č.1 Počet slov
vstupu: větu 
výstup: počet slov

Ahoj, jak se máš?
výstup: Věta obsahuje 4 slova
"""
veta = input() # zadavam vetu
slova_pocet = len(veta.split()) # .split rozdeli vetu na prvky a len ich spocita

print(f"Veta obsahuje {slova_pocet} slova")

#2. řešení
veta="Ahoj, jak se máš?"
counter=0
for pismeno in veta:
    if pismeno==" ":
        counter+=1
print(f"Veta obsahuje {counter+1} slova")

#3. řešení
print(f"Veta obsahuje {veta.count(" ")+1} slova")

"""
Dictionary (slovník)
klíč:hodnota
"""
osoba={
    "jmeno":"Garik",
    "vek":31,
    "mesto": "Ostrava"
}
print(osoba)
print(osoba["jmeno"])
print(osoba["mesto"])
print(osoba.get("povolani")) #pokud klíč není v dictionary, pak nevyhodí KeyError, ale None
osoba["vek"]=32 #přepis hodnot v dictionary
print(osoba)
osoba["povolani"]="lektor"
print(osoba)

# volání klíčů
for klic in osoba:
    print(klic)

# volání hodnot
for hodnota in osoba.values():
    print(hodnota)
# volání obojího
for klic,hodnota in osoba.items():
    print(f"{klic}:{hodnota}")

# odstranění klíče
del osoba["vek"]
print(osoba)

#2. možnost
osoba.pop("povolani")
print(osoba)



osoba2=[{
    "jmeno":"Garik",
    "vek":31,
    "mesto": "Ostrava"
},
{
    "jmeno":"Samuel",
    "vek":31,
    "mesto": "Ostrava",
    "povolani": "datový vědec"
}
]
print(osoba2[1]["jmeno"])
"""
Příklad 2 Počet slov a výskyt
vstup: věta
výstupu: slovo:počet

Vstup: Pes pes pes kocka kocka
Výstup: 
pes:3
kocka:2
"""

text="Pes pes pes kocka kocka zvire pes"
slova=text.lower().split() #rozděluje text podle daného rozdělovače
slovnik={}
for slovo in slova:
    if slovo in slovnik:
        slovnik[slovo]+=1
    else:
        slovnik[slovo] = 1

for klic,hodnota in slovnik.items():
    print(f"{klic}:{hodnota}")

"""
Funkce 
def nazev_funkce(paramtery):
    Telo funkce
    return vysledek
"""

def soucet(a, b):
    return a + b

print(soucet(5, 55))

def soucin(a,b):
    c=1
    mezi_vysledek=a*b*c
    return mezi_vysledek
vysledek=soucin(3,5)
print(vysledek)

"""
Příklad
funkce: aritmetický průměr ze tří čísel
"""
def priemer(a,b,c):
    return round(((a+b+c)/3),2)

print(priemer(5, 8, 4))

def kalkulacka(a,b):
    # Altgr+Q - nový řádek \n
    return print(f"Součet těchto čísel je {soucet(a,b)}.\nSoučin těchto čísel je {soucin(a,b)}.")

kalkulacka(5,3)

def priemer2(a,b,c=0,d=100): #nepovinný argument c
    return round(((a+b+c)/3),2)

print(priemer2(5, 8))

import math

print(math.factorial(5)) #5*4*3*2*1

#rekurzivní funkce
def faktorial(cislo):
    if cislo<0:
        return "neděl nulou"
    else:
        if cislo==1 or cislo==0:
            return 1
        else:
            return cislo*faktorial(cislo-1)
"""
cislo=5 -> return 5*faktorial(4) -> 5*faktorial(4)*faktorial(3)*faktorial(2)*faktorial(1)
cislo=4 -> return 4*faktorial(3)
cislo=3 -> return 3*faktorial(2)
cislo=2 -> return 2*faktorial(1)
cislo=1 -> return 1
5*4*3*2*1

"""
print(faktorial(5))

"""
Globální x lokální proměnné
"""

def test():
    print(globalni_promenna)
    lokalni_promenna="AHOJ"
    print(lokalni_promenna)

globalni_promenna="Streda"
test()
print(lokalni_promenna)
print(globalni_promenna)


"""
Příklad
funkce prvocislo
vstup: cislo od uzivatele
vystup: Je prvočíslo/není prvočíslo
"""
def prvocislo(cislo):
    if cislo < 2:
        return "Není prvočíslo"
    for cislo in range(2, 1000000000000000000000000000000000000000000000000000000000000000):
        if cislo % cislo-1 == 0:
            return "Není prvočíslo"
    return "Je prvočíslo"

# Získání čísla od uživatele
cislo = int(input("Zadejte číslo: "))


vysledek = je_prvocislo(cislo)
print(vysledek)

#2.řešení
def prvocislo2(cislo):
    if cislo < 2:
        return "Není prvočíslo"
    for delitel in range(2,cislo):
        if cislo % delitel==0:
            return "Není prvočíslo"
    return "Je to prvočíslo"
print(prvocislo2(10007))

"""
Příklad Přestupný rok
pokud je rok dělitelný 4 beze zbytku -> pak je přestupný
pokud je rok dělitelný 100 beze zbytku -> pak není přestupný
pokud je rok dělitelný 400 beze zbytku -> pak je přestupný

2000 -> je přestupný
1900 -> není přestupný (je dělitelný 100, ale ne 400)
2024 -> je přestupný
2023 -> není přestupné
"""
def Priestupny_rok(rok):
    if rok % 400 == 0:
        return(f"{rok} je priestupny")
    elif rok % 100 == 0:
        return (f"{rok} je nepriestupny")
    elif rok % 4 == 0:
        return (f"{rok} je priestupny")

def Priestupny_rok2(rok):
    if rok % 400 == 0 or (rok % 4 == 0 and rok % 100 != 0):
        return(f"{rok} je priestupny")
    else:
        return (f"{rok} je nepriestupny")

rok = int(input("Zadaj rok "))
aky_rok = Priestupny_rok2(rok)
print(aky_rok)

