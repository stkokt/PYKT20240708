"""
Aufgabe 1)

Personen innerhalb einer Liste suchen

Vorgegeben:
	Liste mit Namen (Max Mustermann) vorgeben

Hinweis:
	for-Schleife
	if-Bedingung
	String-Methode: startwith(...)
	Variablen

Aufgabenteil a:
	Eingabe: Exakter Name
	Ausgabe: Alle Einträge die passen
	
Aufgabenteil b:
	Eingabe: Anfang eines Namens
	Ausgabe: Alle Einträge die passen
	
Aufgabenteil c:
	Eingabe: Anfang eines Namens
	Ausgabe: Maximal die ersten drei passenden Einträge
	
	
-----------------------------
"""
namen = ["Levi Schneider","Lina Schmitt","Emil Weber","Liam Fischer","Lia Krause","Emilia Hartmann","Anton Meyer",
         "Theo Wagner","Emma Koch","Paul Becker","Leano Schulz","Elias Richter","Jakob Hofmann","Ella Herrmann",
         "Ida Schröder","Samuel Braun","Laura Stein"]

# Aufgabenteil a:

search = "Paul Becker"

for name in namen:
    if name.startswith(search):
        print(f"Name {name} in Liste gefunden.")


# Aufgabenteil b:

search1 = "Li"

for name in namen:
    if name.startswith(search1):
        print(f"Name {name} in Liste gefunden.")

# Aufgabenteil c:

zaehler = 1
for name in namen:
    if name.startswith(search1):
        print(f"Name {name} in Liste gefunden.")
        zaehler += 1

    if zaehler == 3:
        break

# Alternative
"""
search2 = "E"
search2list=[]
for name in namen:
    if name.startswith(search2):
        search2list.append(name)
for i in range(3):
    print(search2list[i], end="\t")

print(search2list)
"""

# Während die Methode startswith geeignet ist, nach Vornamen zu filtern
# ist die Methode endswith geeignet, nach Nachnamen zu filtern

"""
AUFGABE 2)

Standardabweichung berechnen (Stichprobe)

https://datatab.de/tutorial/standardabweichung-varianz-spannweite
Abschnitt: Streuungsmaße mit DATAtab berechnen

Vorgegeben:
	Liste mit Zahlen: 1, 3, 10, 5, 6, 1, -3, 12

Hinweis:
	for-Schleife
	Quadratwurzel ziehen: import math, math.sqrt()

Aufgabenteil a: 
	Mittelwert E berechnen: 1+3+10+...+12 / length
	
Aufgabenteil b: 
	M = (E-x1)^2 + (E-x2)^2 + (E-x2)^2 .... 
	
Aufgabenteil c:
	Standardabweichung: math.sqrt( M / (length-1) ) 

Vergleichsrechnung zur Probe hier:
https://www.standarddeviationcalculator.io/de/standard-deviation-calculator
-----------------------------
"""
zahlen =[1, 3, 10, 5, 6, 1, -3, 12]

summe = 0
for zahl in zahlen:
    summe += zahl

E = summe/len(zahlen)
# Alternativ: E=sum(zahlen)/len(zahlen)


M=0
for zahl in zahlen:
    M+=(zahl-E)**2

from math import sqrt
print("Standardabweichung ist: ",sqrt(M/(len(zahlen)-1)))



"""
Aufgabe 3)

Neue Listen aus bestehender Liste erzeugen

Vorgegeben:
	Liste mit Zahlen
	
Hinweis:
	for-Schleife
	Listen-Methode: append
	Vergleichsoperatoren
	Modulo-Operator

Aufgabenteil a:
	Zwei neue Listen erstellen
	Liste 1: mit allen positiven Zahlen
	Liste 2: mit allen negativen Zahlen
	
Aufgabenteil b:
	Zwei neue Listen erstellen
	Liste 1: mit allen Zahlen die geraden index haben
	Liste 2: mit allen Zahlen die ungeraden index haben
	
Aufgabenteil c:
	Vier neue Listen erstellen
	Liste 1: enthält die Zahlen mit index 0, 4, 8,  ...
	Liste 2: enthält die Zahlen mit index 1, 5, 9,  ...
	Liste 3: enthält die Zahlen mit index 2, 6, 10, ...
	Liste 4: enthält die Zahlen mit index 3, 7, 11, ...
	
Aufgabenteil d:
	Neue Liste die jeweils immer vier aufeinanderfolgende Zahlen der Liste aufsummiert enthält
	Beispiel Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11]
	Beispiel Neuliste = [ 0+1+2+3, 4+5+6+7, 8+9+10+11 ]
	
Aufgabenteil e:
	Beispiel Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
	Beispiel Neuliste = [0, 1+2, 3+4+5, 6+7+8+9, 10+11+12+13+14]


-----------------------------
"""


# Aufgabenteil a:

zahlenliste=[1,-6,5,8,45,-62,51,22,-35,11,-25,18]
positiv=[]
negativ=[]

for zahl in zahlenliste:
    if zahl > 0:
        positiv.append(zahl)
    elif zahl==0:
        continue
    else:
        negativ.append(zahl)

# Alternative List Comprehension
"""
positiv = [x for x in zahlenliste if x > 0]
negativ = [x for x in zahlenliste if x < 0]
"""

print(positiv, negativ)


# Aufgabenteil b:

even_I = []
odd_I = []

for index, zahl in enumerate(zahlenliste):
    if index % 2 == 0:
        even_I.append(zahl)
    else:
        odd_I.append(zahl)

# Alternative 1: for range Loop
"""
for i in range(0, len(zahlenliste)):
    if i % 2 == 0:
        even_I.append(zahlenliste[i])
    else:
        odd_I.append(zahlenliste[i])
"""

# Alternative 2: List Slicing
"""
even_I = zahlenliste[::2]
odd_I = zahlenliste[1::2]
"""

print(even_I, odd_I)


# Aufgabenteil c:

L0_4=[]
L1_5=[]
L2_6=[]
L3_7=[]

liste = 0
for zahl in zahlenliste:
    match liste:
        case 0:
            L0_4.append(zahl)
        case 1:
            L1_5.append(zahl)
        case 2:
            L2_6.append(zahl)
        case 3:
            L3_7.append(zahl)

    liste += 1
    if liste == 4:
        liste = 0

# Alternative 1: for range Loop
"""
for i in range(0, len(zahlenliste), 4):
    L0_4.append(zahlenliste[i])
for i in range(1, len(zahlenliste), 4):
    L1_5.append(zahlenliste[i])
for i in range(2, len(zahlenliste), 4):
    L2_6.append(zahlenliste[i])
for i in range(3, len(zahlenliste), 4):
    L3_7.append(zahlenliste[i])

"""
# Alternative 2: List Slicing
"""
L0_4 = zahlenliste[0::4]
L1_5 = zahlenliste[1::4]
L2_6 = zahlenliste[2::4]
L3_7 = zahlenliste[3::4]
"""


print(L0_4, L1_5, L2_6, L3_7)


# Aufgabenteil d:

Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11]
NeueListe=[]
cnt=0
summe=0
for zahl in Ausgangsliste:
    cnt+=1
    summe+=zahl
    if cnt%4==0:
        NeueListe.append(summe)
        summe=0

print(NeueListe)


# Aufgabenteil e:

"""
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
_
  _ _
      _ _ _
            _ _ _ _
                    __ __ __ __ __
"""

Ausgangsliste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
NeueListe=[]

spannweite = 1
zaehler = 0
summe = 0

for zahl in Ausgangsliste:
    if zaehler < spannweite:
        summe += zahl
        zaehler += 1

    if zaehler == spannweite:
        zaehler = 0
        spannweite += 1
        NeueListe.append(summe)
        summe = 0

print(NeueListe) 

"""
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14
_ 0,1 (Ende=Start+i+1= 0+0+1, Start=Ende=1)
  _ _ 1,3 (Ende=Start+i*2+1= 1+1+1, Start=Ende=3)
      _ _ _ 3,6 (Ende=Start+i+1= 3+2+1, Start=Ende=6)
            _ _ _ _6,10 (Ende=Start+i+1= 6+3+1, Start=Ende=10)
                    __ __ __ __ __ 10,15 (Ende=Start+i+1= 10+4+1, Start=Ende=15)
"""
""" # Alternative 1, nicht belastbar beim Hinzufügen von Zahlen zur Liste

cnt=0
start=0
ende=0
summe=0

while start<len(Ausgangsliste):
    ende=start+cnt+1
    for i in range(start, ende):
        summe+=Ausgangsliste[i]
    NeueListe.append(summe)
    summe=0
    start=ende
    cnt+=1
print(NeueListe) """



"""
AUFGABE 4)

Taschenrechner simulator

Vorgegeben:
	Liste mit Zahlen und arithmetischen Operatoren(+,-,*,/): z.B. ["+", 4, "-", 7, "+", 11, "*", 8, "/", 2]

Hinweis:
	for-Schleife
	if-Bedingung
	Variablen

Aufgabenteil a:
	Du schaltest den Taschenrechner ein und es erscheint eine 0, dann gibst du nach und nach die Operatoren und Zahlen ein. Nach der Eingabe einer Zahl berechnet der Taschenrechner den neuen Betrag.
"""

eingaben = ["+", 4, "-", 7, "+", 11, "*", 8, "/", 2]

betrag = 0.0
operation = None

for eingabe in eingaben:
    if eingabe == "+" or eingabe == "-" or eingabe == "*" or eingabe == "/":
        operation = eingabe
    else:
        match operation:
            case "+":
                betrag += eingabe
            case "-":
                betrag -= eingabe
            case "*":
                betrag *= eingabe
            case "/":
                betrag /= eingabe   

print(f"Ergebnis: {betrag}")