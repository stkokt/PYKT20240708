# Aufgabe 1:
# Nutze die pop-Methode, um die Eingangsliste in die Ausgangsliste umzuformen:

eingangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]
ausgangsliste = [52, 4, 61, 67, 3]
print(ausgangsliste.index(61))
liste=[]
liste.insert(0, ausgangsliste.pop(ausgangsliste.index(61)))
print(liste, ausgangsliste)

# Füge hier eine Reihe von pop-Methodenaufrufen ein:
# eingangsliste.pop(...)
# eingangsliste.pop(...)
# ...

# Anfang Lösung
eingangsliste.pop(0)
eingangsliste.pop(0)
eingangsliste.pop(1)
eingangsliste.pop(1)
eingangsliste.pop(3)
# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")



# Aufgabe 2:
# Nutze die insert-Methode, um die Eingangsliste in die Ausgangsliste umzuformen:

eingangsliste = [52, 4, 61, 67, 3]
ausgangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]

# Füge hier eine Reihe von pop-Methodenaufrufen ein:
# eingangsliste.insert(0, 68)
# eingangsliste.insert(index, wer0)
# ...

# Anfang Lösung
eingangsliste.insert(0, 68)
eingangsliste.insert(1, 44)
eingangsliste.insert(3, 92)
eingangsliste.insert(4, 11)
eingangsliste.insert(7, 69)
# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")



# Aufgabe 3:
# Ersetze Elemente der Eingangsliste mittels Zuweisungsoperatior (=), bis die Eingangsliste der Ausgangsliste gleicht:

eingangsliste = [68, 30, 52, 92, 54, 4, 61,  9, 67, 1]
ausgangsliste = [68, 44, 52, 92, 11, 4, 61, 69, 67, 3]

# Füge hier eine Reihe von Zuweisungsoperationen ein:
# eingangsliste[1] = 44
# eingangsliste[index] = wert
# ...

# Anfang Lösung
eingangsliste[1] = 44
eingangsliste[4] = 11
eingangsliste[7] = 69
eingangsliste[9] = 3
# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")


# Aufgabe 4:
# Nutze die pop-Methode und insert-Methode um die Eingangsliste in die Ausgangsliste umzuformen:
# Verwende so wenig wie mögliche Methodenaufrufe.

eingangsliste = [68, 52, 92, 60, 54, 4, 50, 9, 67]
ausgangsliste = [68, 30, 52, 92, 54, 4, 61, 67, 1]

# Füge hier eine Reihe von pop- und/oder insert-Methodenaufrunfen ein:
# eingangsliste.insert(index, wert)
# eingangsliste.pop(index)
# ...

# Anfang Lösung
eingangsliste.insert(1,30)
eingangsliste.pop(4)
eingangsliste.pop(6)
eingangsliste.insert(6,61)
eingangsliste.pop(7)
eingangsliste.insert(8,1)
# Ende Lösung

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")



# Aufgabe 5:
# Listen können ebenso wie Strings konkatiniert werden:
#beispiel_liste1 = [1,2,3]
#beispiel_liste2 = [4,5,6]
#beispiel_zusammengesetzte = beispiel_liste1 + beispiel_liste2
#beispiel_zusammengesetzte == [1,2,3,4,5,6]
#print(zusammengesetzte_liste)

liste1 = [68, 30, 52]
liste2 = [60,  4, 61]
liste3 = [40, 92, 54]
liste4 = [61, 67,  1]

# Konkatiniere die Listen in der richtigen Reihenfolge zu einer Eingangsliste und entferne alle störenden Elemente mittels der pop-Methode, bis die Eingangsliste der Ausgangsliste gleicht:
# Füge hier die Operationen ein:
# eingangsliste = liste1_4 + liste1_4 + ... + liste1_4
# eingangsliste.pop(index)
# ...

# Anfang Lösung
eingangsliste = liste1 + liste3 + liste2 + liste4
eingangsliste.pop(3)
eingangsliste.pop(5)
eingangsliste.pop(6)
# Ende Lösung

ausgangsliste = [68, 30, 52, 92, 54, 4, 61, 67, 1]

print(f"Eingangsliste: {eingangsliste}")
print(f"Ausgangsliste: {ausgangsliste}")

if eingangsliste == ausgangsliste:
    print("Listen sind identisch! Geschafft!")
else:
    print("Noch entspricht die Eingangsliste nicht der Ausgangsliste")


# Zusatzaufgaben

# Zusatz 1
"""
Muster aus Zahlen ausgeben:
Schreibe ein Programm, das folgendes Muster ausgibt:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
Verwende eine Schleife, um das Muster zu erstellen.
"""

cnt=1
triangle=[]
while(cnt<6):    
    triangle.append(cnt)
    print(triangle)
    cnt+=1

print("\n")

# Zusatz 2
# Sortiere die Liste so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.
liste1=[x for x in range(1, 101)] # Liste von 1 - 100
# liste5=liste1[int(((len(liste1))/2)):int(len(liste1))]+liste1[0:int((len(liste1)/2))] #liste1[((len(liste1))/2):len(liste1)]+
liste_vertauscht=liste1[int(((len(liste1))/2)):]+liste1[:int((len(liste1)/2))] # sparsame Variante liste[50:]+liste[:50]
print("Aufgabe 5\n")
print(liste_vertauscht, "\n")

# Zusatz 3
# Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate.
a = [1,2,3,4,5]
b = [8,7,6,5,4]
c=a+b
# c_ohneDuplikate=list(set(c)) # Variante1: Konvertieren der Liste in ein Set, Reihenfolge wird nicht beibehalten
c_ohneDuplikate=list(dict.fromkeys(c)) # Variante2: fromkeys- Methode des Dictionary nutzen und danach wieder in  eine Liste wandeln
print(c_ohneDuplikate, "\n")
print((dict.fromkeys(c)))
# Zusatz 4
# Schreibe einen Algorithmus zum Lotto spielen (6 aus 49). Dazu soll es eine Liste geben, die den Tip
# darstellt (z.B. [5,18,29,45,37,7]). Der Algorithmus soll dann eine Anzahl von Ziehungen machen,
# jeweils mit dem Tip vergleichen und die Dreier bis Sechser zählen.
# Nutze dazu die Methode sample() aus dem Random- Modul (import random bzw. from random import sample)

import random


lotto=[x for x in range(1, 50)]
tip = [5,18,29,45,37,7]
t3=0
t4=0
t5=0
t6=0
for n in range(1000000):
    ziehung=random.sample(lotto, 6)
    treffer = 0
    for zahl_t in tip:
            if zahl_t in ziehung:
                  treffer+=1
    match treffer:
        case 3:
            t3+=1
        case 4:
            t4+=1
        case 5:
            t5+=1
        case 6:
            t6+=1
print(f"Dreier: {t3}, Vierer: {t4}, Fünfer: {t5}, Sechser: {t6}")
