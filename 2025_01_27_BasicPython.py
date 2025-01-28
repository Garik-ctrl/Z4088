"""
Hodina Basic Python
27.01.2025
Skupina Z4088
"""
from traceback import print_tb

#AltGr+X - jednořádkový komentář
# 2. řádek
# 3. řádek


"""
1. řádek
2. řádek 
3. řádek
datové typy
"""
#string=text
print("Ahoj světe!")
print('Pondělí')
print('Jak se máš?')

#Windows/Linux část kódu shift+alt+E
#macOS Shift+Option+E

a="Ahoj světe2!"
print(a)

b=3 #integer->celé číslo
c=5
print(b)
print(c)
print(b+c)

d="Dnes je Pondělí"
print(a+" "+d+" Jak se máš?")

#zpět -> ctr+Z

jmeno=input("Zadej své jméno: ") # příkaz input žádá po uživateli vstup
mesto=input("Zadej z jakého města jsi: ") #vždy datový typ string
print("Ahoj " + jmeno + ", město " + mesto + " je nádherné!")

cislo1=3
cislo2="3"

print(cislo1, type(cislo1))
print(cislo2, type(cislo2))

#Datový typ Boolean - True/False

Boolean=False
print(Boolean, type(Boolean))

#Datový typ Float - desetinné číslo

desetinnne_cislo=1.1
print(desetinnne_cislo, type(desetinnne_cislo))

#kombinace datových typů integer a float
cislo3=3
cislo4=5.2

print(cislo3+cislo4, type(cislo3+cislo4))

#různé datové zápisy

print(3+2) #5
print("3"+2) #nepůjde
print("3"+"2") #32
print("3+2") #3+2

#základní matematické operace

print(3+2) #sčítání
print(3-2) #odčítání
print(3*2) #násobení
print(3/2) #dělení
print(3**2) #mocnina
print(3%2) #modulo
print(3//2) #dělení beze zbytku

string_cislo="55"
print(str(1)+string_cislo)

vek=int(input("Kolik je ti let? "))
print(vek, type(vek))

"""
ÚLOHA: Věk
vstupu: rok narození
výstup: "Je ti 30let"
"""
#VYpocet veku
Rok_string=input("Zadej Rok narozeni ")
Rok=int(Rok_string)
print("Je ti ", 2025-Rok,"let! Jsi mladik :D  ")

#2. možnost
Rok=int(input("Zadej Rok narozeni "))
print("Je ti " +  str(2025-Rok) + "let! Jsi mladik :D  ")

#3. možnost
Rok=int(input("Zadej Rok narozeni "))
pocet_let=2025-Rok
print("Je ti " +  str(pocet_let) + "let! Jsi mladik :D  ")

"""
If cyklus
If podmínka:
    udělej něco
else:
    udělej něco jiného 
    
podmínka- operátory >,>=,<,<=, ==, !=
"""

#Příklad 2 - maximum ze dvou čísel

cislo1=15
cislo2=20

if cislo1>cislo2:
    print("Maximum je " + str(cislo1))
else:
    print("Maximum je " + str(cislo2))
    print("Garik")

print("Garik2")
"""
Příklad 3 - zletilost
vstup: věk
výstupu: Jsi zletilý/Jsi nezletilý
"""
cislo1=int(input("Koľko máš rokov? "))

if cislo1<18:
    print("Si nezletilý")
    print("Ďakujeme za návštevu")
else:
    print("Si zletilý")
    print("Môžeš nakupovať alkohol")

"""
Přiklad 4 slovní ohodnocení známky
vstupu: známka
výstupu: hodnocení
"""

znamka=int(input("Zadej svojí známku z testu: "))

if znamka==1:
    print("Výborně")

if znamka==2:
    print("Chvalitebně")

#----------------------------------------------
znamka=int(input("Zadej svojí známku z testu: ")) #3

if znamka==1:
    print("Výborně")
elif znamka==2:
    print("Chvalitebně")
elif znamka==3:
    print("Dobře")
elif znamka==4:
    print("Dostatečně")
elif znamka==5:
    print("Nedostatečně")
else:
    print("Taková známka neexistuje")

"""
Logické operátory AND a OR 
"""

"""
Příklad 5 jméno a heslo
vstup: jméno a heslo
výstupem: vstup povolen/vstup odepřen 
"""

uzivatelske_jmeno=input("Zadej své uživatelské jméno: ")
uzivatelske_heslo=input("Zadej své uživatelské heslo: ")

admin_jmeno="ADMIN"
admin_heslo="ADMIN"

if uzivatelske_jmeno==admin_jmeno and uzivatelske_heslo==admin_heslo:
    print("Vstup povolen")
else:
    print("Vstup odepřen")

"""
Příklad 6 BMI index

vstup: BMI index
výstup: 
BMI do 18,5 -> podváha
BMI od 18,51 do 25 -> normální váha
BMI od 25,1 -> nadváha
-------
vstup: výška v metrech a váha
BMI= váha/(výška^2)
"""

výška=float(input("Napíš svoju výšku v metroch"))
váha=float(input("Napíš svoju váhu v kg"))
BMIindex= round((váha/(výška**2)),2)
if BMIindex<18.5:
    print("Tvoje BMI je " + str(BMIindex) + " a máš podváhu")
elif 18.51<=BMIindex<=25:
    print("Tvoje BMI je " + str(BMIindex) + " a máš normálnu váhu")
else:
    print("Tvoje BMI je " + str(BMIindex) + " a máš nadváhu")

"""
List
mesta=[mesto1, mesto2, mesto3]
mesta=[0,1,2]
"""

mesto1="Praha"
mesto2="Brno"
mesto3="Ostrava"

mesta=["Praha","Brno","Ostrava"]
print(mesta)
print(mesta[3])

cisla=[1,2,3,4,5]
print(cisla[1])

#altgr+F, altgr+G
mix=["Praha",3,3.15,True, ["Praha","Brno","Ostrava"]]
print(mix[4])

cisla=[1,2,3,4,5,6,7,8,9]
print(cisla[1])

#poslední prvek
print(cisla[-2])

#append - přidání jednoho čísla na konec
cisla.append(999)
cisla.append(-5)
print(cisla)

#extend - přidání více hodnot
cisla.extend([1,1.1,5,5,0])
print(cisla)

#insert - vložení hodnoty na konkrétní pozici
cisla.insert(0,-666)
print(cisla)

#pop - smazná dané pozice
cisla.pop(-1)
print(cisla)

#přepisování hodnot
cisla[0]=111
cisla[5]=111
print(cisla)

#tisknutí listu
# cisla[a:b:c], kde a je start, b je konec (bez b), c je skok
print(cisla[0:6])
print(cisla[::-1]) # tisknutí listu od konce
print(cisla[::-2]) # každý druhý prvek od konce
print(cisla)
print(cisla[::2]) # každý druhý prvek od začátku
print(cisla[1::2]) # každý druhý prvek od indexu 1
print(cisla[1:10:2]) # každý druhý prvek od indexu 1 do indexu 10 (bez 10)

"""
Příklad 7
na vstupu [2,4,6,8,10] a jeden uživatelský vstup
výstup list v opačném pořadí 
"""
seznam=[2,4,6,8,10]
cislo=int(input("Zadejte cislo: "))
seznam.insert(4, cislo)
print(seznam)
