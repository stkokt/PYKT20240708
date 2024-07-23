"""
1. Schreibe ein Programm, das den Benutzer 
nach einer Zahl fragt und dann überprüft, ob die Zahl gerade oder ungerade ist.

2. Schreibe ein Python-Programm, das den Benutzer 
nach seinem Geburtsdatum fragt und dann ausgibt, ob er/sie volljährig ist (d.h. 18 Jahre oder älter).
Nutze für das Geburtsdatum sowie das aktuelle Datum 
einen Datumsstring im Format dd-mm-yyyy.

3. Schreibe ein Python-Programm, das den Benutzer 
nach einer Jahreszahl fragt und dann ausgibt, ob es sich um ein Schaltjahr handelt.
"""

#1 

"""
zahl=input("Gebe eine ganze Zahl ein:\n")

if zahl.isdigit():                      # Prüfung, ob alle Zeichen des eingegebenen Strings Ziffern sind
    if int(zahl)%2==0:                  # Prüfung, ob die Zahl gerade ist
        print("Zahl ist gerade.")       # wenn, dann
    else:
        print("Zahl ist ungerade.")     # sonst, wenn ungerade
else:
    print("Eingabe ist keine Ganzzahl.")# sonst, wenn Stringzeichen keine Ziffer
"""


#2
"""
# Eingaben der Daten
today=input("Gebe das aktuelle Datum im Format dd-mm-yyyy ein:\n")
bday=input("Gebe das Geburtsdatum im Format dd-mm-yyyy ein:\n")

# Splitten des Strings am Bindestrich/ Return ist eine Liste
today_split=today.split("-")
bday_split=bday.split("-")

# Absichern, dass sich in beiden Listen nur Zahlen befinden (noch als Strings natürlich)
 if (today_split[2].isdigit() and today_split[1].isdigit() and today_split[0].isdigit())\
    and (bday_split[2].isdigit() and bday_split[1].isdigit() and bday_split[0].isdigit()):
    # wenn die Differenz der Jahreszahl bereits größer oder kleiner 18
    if int(today_split[2]) - int(bday_split[2]) > 18:
        print("Volljährig z38")
    elif int(today_split[2]) - int(bday_split[2]) < 18:
        print("Nicht volljährig z40")
    else:
        # wenn Differenz der Jahre gleich 18, Test ob Geburtsmonat größer/ kleiner
        if int(bday_split[1]) - int(today_split[1]) > 0:
            print("Nicht volljährig z43")
        elif int(bday_split[1]) - int(today_split[1]) < 0: 
            print("Volljährig z45")
        else:
            # wenn die Entscheidung erst mit dem Tag gefällt werden kann
            if int(bday_split[0]) - int(today_split[0]) > 0:
                print("Nicht volljährig z48")
            elif int(bday_split[0]) - int(today_split[0]) == 0:
                print("Volljährig z50")
            else:
                print("Volljährig z52")
# wenn Datumsformat falsch
else:
    print("Datumsformat beachten!") """

#3

""" jahr=input("Gebe eine Jahreszahl ein:\n")
# Prüfung, ob String eine Zahl ist
if jahr.isdigit():
    # Prüfung, ob glatt teilbar durch 4, aber nicht durch 100 oder glatt teilbar durch 400
    if (int(jahr)%4 == 0 and int(jahr)%100 != 0) or (int(jahr)%400 == 0):
        print("Schaltjahr")
    else:
        print("Kein Schaltjahr")
# Wenn String keine Zahl
else:
    print("Eingabe war keine Jahreszahl") """

# Vorsicht! Logikumkehr
jahr1="2000"
if (int(jahr1)%4 == 0): # Ausdruck wird als TRUE interpretiert
    pass                # also wird dieser Block betreten

if (int(jahr1)%4): # Ausdruck wird als 0, also FALSE interpretiert
    pass           # also wird dieser Block nicht(!) betreten
else:
    print(bool(int(jahr1)%4)) # sondern dieser Block



