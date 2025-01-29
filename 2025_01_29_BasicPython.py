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

