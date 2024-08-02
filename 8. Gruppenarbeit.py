"""
Die 11 Dictionary Methoden:

.clear()	    Löscht alle Einträge des Dictionarys
.copy()	        Erstellt eine Kopie
.fromkeys()	    Erstellt eine Kopie aus den Schlüsseln eines Dictionary
.get()	        Liest einen Wert zu einem übergebenen Schlüssel aus
.items()	    Gibt alles Schlüssel und Werte aus
.keys()	        Zeigt die Schlüssel eines Dictionary an
.pop()	        löscht den Eintrag aus dem Dictionary des übergebenen Schlüssels 
                und liefert dessen Inhalt als Rückgabewert
.popitem()	    Liefert einen Eintrag als Tupel zurück und löscht den Eintrag aus 
                dem Dictionary (im Gegensatz zu pop() muss kein Schlüssel übergeben werden)
.setdefault()	liefert den Wert eines Eintrags aus dem Dictionary, wenn der Schlüssel 
                vorhanden ist. Ist kein entsprechender Schlüssel vorhanden, wird ein 
                Schlüssel mit dem Wert im Dictionary gespeichert
.update()	    Aktualisiert einen Wert, wenn der Schlüssel vorhanden ist. Wenn noch 
                kein entsprechender Schlüssel vorhanden ist, wird Wert und Schlüssel eingetragen
.values()	    Liefert alle Werte des Dictionary zurück (ohne Schlüssel)

"""

# Aufgabe 1
# Füge die Einträge aus telefonbuch_plus mit einer geigneten Methode dem
# telefonbuch hinzu. Gebe anschließend alle Namen und alle Nummern aus.

telefonbuch = {
    "Anna": "+49 123 456 789",
    "Ben": "+49 987 654 321",
    "Clara": "+49 555 666 777"
}

telefonbuch_plus = {
    "Dora": "+49 111 222 333",
    "Emil": "+49 444 555 666",
    "Franziska": "+49 777 888 999"
}
# Anfang Lösung Aufgabe 1
print("\nAufgabe 1")
telefonbuch.update(telefonbuch_plus)
# Alternativ walrus- Operator (odergleich)
# telefonbuch |= telefonbuch_plus

print(telefonbuch.keys())
print(telefonbuch.values())

# Ende Lösung Aufgabe 1

# Aufgabe 2
# Gebe alle Länder aus, deren Hauptstädte mit "B" beginnen.
# Tipp: Nutze die Dictionary- Methode .items() und die String- Methode .startswith()
hauptstaedte = {
    "Albanien": "Tirana",
    "Andorra": "Andorra la Vella",
    "Armenien": "Jerewan",
    "Aserbaidschan": "Baku",
    "Belgien": "Brüssel",
    "Bosnien und Herzegowina": "Sarajevo",
    "Bulgarien": "Sofia",
    "Dänemark": "Kopenhagen",
    "Deutschland": "Berlin",
    "Estland": "Tallinn",
    "Finnland": "Helsinki",
    "Frankreich": "Paris",
    "Georgien": "Tiflis",
    "Griechenland": "Athen",
    "Irland": "Dublin",
    "Island": "Reykjavík",
    "Italien": "Rom",
    "Kasachstan": "Astana",
    "Kosovo": "Pristina",
    "Kroatien": "Zagreb",
    "Lettland": "Riga",
    "Liechtenstein": "Vaduz",
    "Litauen": "Vilnius",
    "Luxemburg": "Luxemburg",
    "Malta": "Valletta",
    "Moldawien": "Chișinău",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Niederlande": "Amsterdam",
    "Nordmazedonien": "Skopje",
    "Norwegen": "Oslo",
    "Österreich": "Wien",
    "Polen": "Warschau",
    "Portugal": "Lissabon",
    "Rumänien": "Bukarest",
    "Russland": "Moskau",
    "San Marino": "San Marino",
    "Schweden": "Stockholm",
    "Schweiz": "Bern",
    "Serbien": "Belgrad",
    "Slowakei": "Bratislava",
    "Slowenien": "Ljubljana",
    "Spanien": "Madrid",
    "Tschechien": "Prag",
    "Türkei": "Ankara",
    "Ukraine": "Kiew",
    "Ungarn": "Budapest",
    "Vatikanstadt": "Vatikanstadt",
    "Vereinigtes Königreich": "London",
    "Weißrussland": "Minsk",
    "Zypern": "Nikosia"
}
# Anfang Lösung Aufgabe 2
print("\nAufgabe 2")
for k, v in hauptstaedte.items():
    if v.startswith("B"):
        print(k, ":", v)

# Ende Lösung Aufgabe 2


# Aufgabe 3
# Erstelle eine Einkaufsliste (Datentyp Liste) mit 5 Artikeln 
# aus dem Dictionary und ermittle den Gesamtpreis.
# Tipp: Nutze dazu die Dictionary- Methode .keys()

produkte = {
    "Apfel": 0.5,
    "Banane": 0.3,
    "Kirsche": 1.2,
    "Karotte": 0.4,
    "Gurke": 0.8,
    "Birne": 0.6,
    "Kohl": 0.2,
    "Limette": 0.7
}
# Anfang Lösung Aufgabe 3
print("\nAufgabe 3")
einkaufsliste=['Apfel', 'Kirsche', 'Karotte', 'Birne', 'Limette']
preis=0.0

for produkt in einkaufsliste:
    if produkt in produkte.keys():
        preis+=produkte[produkt]

print(f"Die Artikel der Einkaufsliste haben einen Gesamtpreis von {round(preis, 2)} €.")

# Ende Lösung Aufgabe 3

# Aufgabe 4
# Gebe die Buchtitel in der Reihenfolge ihres Erscheinens aus.
# Tipp: Nutze die Builtin- Funktion sorted() und die Dictionary- Methoden .values() 
# und .items()

buecher = {
    "1984": 1949,
    "Der kleine Prinz": 1943,
    "Moby Dick": 1851,
    "Krieg und Frieden": 1869,
    "Die Verwandlung": 1915,
    "Ulysses": 1922,
    "Der große Gatsby": 1925,
    "Hundert Jahre Einsamkeit": 1967,
    "Der Name der Rose": 1980,
    "Harry Potter und der Stein der Weisen": 1997
}
# Anfang Lösung Aufgabe 4
print("\nAufgabe 4")
jahr=sorted(buecher.values())

for y in jahr:
    for k,v in buecher.items():
        if v==y:
            print(k)

# Alternative
""" for y in jahr:
    print(list(buecher.keys())[list(buecher.values()).index(y)]) """

# Ende Lösung Aufgabe 4

# Aufgabe 5
# Ermittle die Landeshauptstadt mit den meisten und die mit den wenigsten Einwohnern.
# Tipp: Nutze die Builtin- Funktionen min() und max(), sowie die Dictionary- Methoden
# .values() und .items()

landeshauptstaedte = {
    "Stuttgart": 597939,
    "München": 1388300,
    "Berlin": 3520100,
    "Potsdam": 159450,
    "Bremen": 546450,
    "Hamburg": 1751780,
    "Wiesbaden": 272630,
    "Schwerin": 91260,
    "Hannover": 514130,
    "Düsseldorf": 593682,
    "Mainz": 202750,
    "Saarbrücken": 176990,
    "Dresden": 525100,
    "Magdeburg": 229924,
    "Kiel": 239860,
    "Erfurt": 203480
}
# Anfang Lösung Aufgabe 5
print("\nAufgabe 5")
maxVal=max(landeshauptstaedte.values())
maxCity=""
for k,v in landeshauptstaedte.items():
    if v == maxVal:
        maxCity=k
        
print(f"{maxCity} hat {maxVal} Einwohner.")

minVal=min(landeshauptstaedte.values())
minCity=""

for k,v in landeshauptstaedte.items():
    if v == minVal:
        minCity=k

print(f"{minCity} hat {minVal} Einwohner.")
# Ende Lösung Aufgabe 5

# Aufgabe 6
# Errechne die Notendurchschnitte pro Person und pro Fach
noten = {
    "Max": {"Mathe": 2.5, "Deutsch": 1.2, "Englisch": 3.4},
    "Lena": {"Mathe": 1.5, "Deutsch": 2.4, "Englisch": 1.8},
    "Tom": {"Mathe": 3.3, "Deutsch": 3.0, "Englisch": 2.8}
}
# Anfang Lösung Aufgabe 6
print("\nAufgabe 6")
max_d=0
lena_d=0
tom_d=0
mathe_d=0
deutsch_d=0
englisch_d=0

for k, v in noten.items():
    for k1, v1 in v.items():
        if k=="Max":
            max_d+=v1
        if k=="Lena":
            lena_d+=v1
        if k=="Tom":
            tom_d+=v1
        if k1=="Mathe":
            mathe_d+=v1
        if k1=="Deutsch":
            deutsch_d+=v1
        if k1=="Englisch":
            englisch_d+=v1

print(f"Max hat einen Notendurchschnitt von {round(max_d/len(noten["Max"].values()), 2)}.\n\
Lena hat einen Notendurchschnitt von {round(lena_d/len(noten["Lena"].values()), 2)}.\n\
Tom hat einen Notendurchschnitt von {round(tom_d/len(noten["Tom"].values()), 2)}.\n\
Der Mathe- Durchschnitt ist {round(mathe_d/len(noten), 2)}.\n\
Der Deutsch- Durchschnitt ist {round(deutsch_d/len(noten), 2)}.\n\
Der Mathe- Durchschnitt ist {round(englisch_d/len(noten), 2)}.\n")


# Aufgabe 7
# Schreibe ein Dictionary, das ein Shoppingcenter simuliert mit 5 Geschäften und je 3 Artikeln. 
# Erstelle nun ein Konsolen- Menu, das alle Artikel mit einer Artikelnummer ausgibt. 
# Der Nutzer soll (mehrere) Artikel auswählen können. Nach Verlassen der Auswahl soll dem Nutzer
# ausgegeben werden, in welchen Geschäften er die jeweiligen Artikel findet. 
# (z.B. „Latschen, Stiefel finden Sie bei Reno. Rosen, Nelken finden Sie bei Blume2000. usw…“
print("\nAufgabe 7")
# Anfang Lösung Aufgabe 7
mall={"Reno":["Stiefel", "Sandalen", "Pantoffel"] ,
      "Blume2000":["Nelken", "Rosen", "Tulpen"],
      "REWE":["Wurst", "Obst", "Brot"],
      "Kik":["Schale", "Stifte", "Schreibblock"],
      "DM":["Seife", "Schwamm", "Deo"]}

print("Guten Tag. Was suchen Sie? (Artikelnummer eingeben)\n")

artNr=0
choice2=""
searchList=[]
findList=dict.fromkeys(mall)
for k, v in findList.items():
    findList[k]=[]
tmpList=[]

for k, v in mall.items():
    for art in v:
        artNr+=1
        print(f"{artNr}....{art}")

while choice2 != "x":
    choice2=input("Artikelnummer:\n")
    if choice2.isnumeric() and int(choice2) in range(1, artNr+1):
        searchList.append(int(choice2))

artNr=0
for k, v in mall.items():
    for art in v:
        artNr+=1
        if artNr in searchList:
            tmpList.append(art)                                
    findList[k]+=tmpList
    tmpList.clear()

for k, v in findList.items():
    for art in v:
        print(f"{art} finden Sie bei {k}")

# Alternative:
"""
shoppingcenter = {
    "Deichfrau": {"d1":"Schuhe", "d2":"Stiefel" ,"d3": "Sandalen"},
    "Oldi": {"a1":"Zahnpasta", "a2":"Schokolade" ,"a3":"Möhren"},
    "Zolinda": {"z1":"Hose","z2":"Bluse", "z3":"T-Shirt"},
    "immerschon": {"i1":"Computer", "i2":"Headset", "i3":"Mixer"},
    "Hirnbach": {"h1":"Bohrmaschine", "h2":"Schrauben", "h3":"Hammer"}
    }

def finde_geschaeft(artikel_nr, center):
    for geschaeft, artikel in center.items():
        if artikel_nr in artikel.values():
            return geschaeft
        
def finde_artikel(artikel_nr, center):
    for geschaeft, artikel in center.items():
        for nr, artikelname in artikel.items():
            if artikel_nr in nr:
                return artikelname
            
liste_auswahl_kunde = set()        


auswahl_wird_ausgeführt = True

while auswahl_wird_ausgeführt:

    for shops in shoppingcenter.values():
        for nr, artikel in shops.items():
            print(f"{nr}: {artikel}")

    auswahl = input("Bitte Artikel-Nr. auswählen (z.B.: d1) oder Auswahl verlassen mit (x): ")
    
    if auswahl == "x":        
        if not len(liste_auswahl_kunde):
            print("Sie haben keine Artikel ausgewählt")
        else:
            for shop, items in shoppingcenter.items():

                liste_shop_artikel = []

                for art_nr in liste_auswahl_kunde: 
                    
                    if art_nr in items:
                        liste_shop_artikel.append(finde_artikel(art_nr,shoppingcenter))

                if not liste_shop_artikel:
                    continue
                else:
                    liste_shop_artikel = str(liste_shop_artikel).strip("[]")       
                    print(f"{liste_shop_artikel} finden Sie bei {shop}")                  

        auswahl_wird_ausgeführt = False
        
    else:
        liste_auswahl_kunde.add(auswahl)

"""
# Ende Lösung Aufgabe 7







