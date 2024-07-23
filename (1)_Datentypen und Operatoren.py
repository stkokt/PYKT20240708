"""
Immutable-Datentypen:


int, float, string, bool, decimal, complex
tuple
range
frozenset
bytes


Mutable-Datentypen:

list
dictionary
set
User-Definierte Objekte


Arithmetische Operatoren:

+	Addition	a + b = 30
-	Subtraction	a – b = -10
*	Multiplication	a * b = 200
/	Division	b / a = 2
%	Modulus	b % a = 0
**	Exponent	a**b =10**20
//	Floor Division	9//2 = 4


Vergleichsoperatoren:

<	Less than	a<b
>	Greater than	a>b
<=	Less than or equal to	a<=b
>=	Greater than or equal to	a>=b
==	Is equal to	a==b
!=	Is not equal to	a!=b


Zuweisungsoperatoren:

=       a = 10  (a ist 10)
+=      a += 10 (a=a+10)
-=
*=
/=
**=     b **= 10 (b hoch 10)
//=     (wenn a = 10) a //= 4 -> a == 2
|=


Logikoperatoren:

and, or, not


Bitweise Operatoren:

&, |, ^, ~, <<, >>


Membership- Operatoren

in, not in


Identitäts- Operatoren

is, is not

"""

var = 8                                 # Integervariable angelegt mit Wert = 8
print("Speicheradresse var: ",id(var))  # Ausgabe der Speicheradresse
print("Datentyp var: ",type(var))       # Ausgabe des Datentypes von var

print("\n", "Zeile 77", "\n")
var2 = 8.5                              # Fließkomma- Variable angelegt mit Wert = 8.5
var3 = "text"                           # Stringvariable angelegt mit Wert = "text"
print("Speicher var3: ",id(var3), "Speicher var3[1]: ", id(var3[1])) # Ausgabe der Speicheradresse von var3 und des Index 1 von var3 -> "text" (e)
print("Datentyp var3: ",type(var3))     # Ausgabe des Datentyps von var 3

print("\n", "Zeile 83", "\n")
var4 = var                      # Wertzuweisung auf var4 durch andere Variable
print("Speicher var4: ",id(var4), " Speicher var: ",id(var), "\n")  # Speicheradressen identisch
var = 10                        # Neuzuweisung auf var
print("Speicher var4: ",id(var4), " Speicher var: ",id(var), "\n")  # Durch Zeile 86 Speicheradressen nun unterschiedlich (Integer ist immutable)

"""
Wenn die Variable bei Neuzuweisung eine neue Speicheradresse bekommt, handelt es sich um einen nicht- veränderbaren
Datentyp (immutable). Daher ist die Verknüpfung aus Zeile 84 in diesem Fall (Integer) nicht persistent.

Das Speicherkonzept von Python ist ungewöhnlich. Gleiche Werte haben gleiche Speicheradressen.
"""
print("Zeile 95: Speicherbelegung bei Integervariablen\n")
var5 = 20
var6 = 20
print("Gleicher Wert = gleiche Speicheradresse: ", "var5: ",id(var5), "var6: ",id(var6), "\n")   # Gleicher Wert = gleiche Speicheradresse

print("Zeile 100: Speicherbelegung bei Stringvariablen\n")
var7 = "Papa ante portas"
var8 = "Alles auf Anfang"
print("Adresse var7: ",id(var7), "Adresse var8: ",id(var8), "\n")   # Unterschiedliche Speicheradresse
print("Speicherbelegung aller a in var7 und var8:\n",id(var7[1]), id(var7[3]), id(var7[5]), id(var7[14]),"\n",
      id(var8[6]), id(var8[13]), "\n") # Gleicher Wert (a) = gleiche Speicheradresse

"""
Alle Datentypen in Python sind klassenbasiert, d.h. sie haben Methoden, die man an ihnen verwenden kann.
"""

print("Zeile 111: Verwendung von Methoden eines Datentyps über den Punkt- Operator\n")

print("Methode 'is_integer()' am Datentyp 'int' für Variable var5: ",var5.is_integer())
print("Methode 'title()' am Datentyp 'str' für Variable var7: ",var7.title())
print("Methode 'split()' am Datentyp 'str' für Variable var7: ",var7.split())

print("\nZeile 117: Formatierte Ausgaben\n")

print("Der Titel '"+var7+"' enthält",len(var7.split()),"Worte.") # Konkatinierung bei Strings, kommagetrennt bei anderen Datentypen
print("Der Titel '"+var7+"' enthält "+str(len(var7.split()))+" Worte.") # Durch Konvertierung zu String (str(len(var7.split()))) Konkatination möglich
print(f"Der Titel '{var7}' enthält {len(var7.split())} Worte.")
print("Der Titel '{}' enthält {} Worte.".format(var7, len(var7.split())))

"""
Vorsicht! Das Folgende funktioniert nicht:

print("Der Titel '{}' enthält {} Worte.".format(var7))

wirft den Fehler:

    print("Der Titel '{}' enthält {} Worte.".format(var7))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
IndexError: Replacement index 1 out of range for positional args tuple

Das meint, dass der zweite Platzhalter (Replacement index 1) in .format() nicht übergeben wurde.
"""

# Abprüfen von zwei Konditionen
print("\nAbprüfen von zwei Konditionen")
print("10<5 and 4<5 = ", 10<5 and 4<5) # Beide Konditionen müssen zutreffen, damit 
                    # der Gesamtausdruck WAHR wird, daher hier 
                    # Gesamtausdruck FALSCH

print("10<5 or 4<5 = ",10<5 or 4<5)  # Nur eine der beiden Konditionen muss zutreffen,
                    # damit der Gesamtausdruck WAHR wird, daher hier 
                    # Gesamtausdruck WAHR
"""

11.07.2024 -> Little Endian (less significant bit on the left side)
2024/07/11 -> Big Endian

2^7 2^6 2^5 2^4 2^3 2^2 2^1 2^0     Binärinterpretation bei Big Endian

Beim verODERn wird im Ergebnis das Bit auf 1 gesetzt,
wenn es in mindestens einer der beiden Ausgangsreihen auf 1 war

0000 0001   = 1
0000 0010   = 2
_______________ | (bitweises or)
0000 0011   = 3


Beim verUNDen wird im Ergebnis das Bit auf 1 gesetzt,
wenn es in beiden Ausgangsreihen auf 1 war

0000 0001   = 1
0000 0010   = 2
_______________ & (bitweises und)
0000 0000   = 0

aber: 

0000 0001   = 1
0000 0011   = 3
_______________ & (bitweises und)
0000 0001   = 1


Beim verXODERn wird im Ergebnis das Bit auf 1 gesetzt,
wenn es nur(!) in einer der beiden Ausgangsreihen auf 1 war

0000 1011   = 11
0000 1001   = 9
_______________^ (bitweises xor, exklusives oder)
0000 0010   = 2


verNOTen lässt sich immer nur ein Wert. Dabei werden die Bit-setzungen
einfach umgekehrt 

0000 0011   = 3
_______________ ~
1111 1100   = 252

ABER SIEHE ZEILE 252, reale VerNOTung führt zur Bildung des Zweierkomplements. 
"""
# Verschiebeoperatoren >> , << 

print("\nVerschiebeoperatoren >> , <<")
var9 = 2    # 0000 0010
print("var9:",var9," binär:",bin(var9))

# Linksverschiebung um eine Stelle verdoppelt den Wert
var9<<=1    # 0000 0100 Binärreihe aus Zeile 201 wird um eine Stelle nach links verschoben
print("var9 nach Linksverschiebung (eine Stelle):",var9, " binär:",bin(var9))

# Rechtsverschiebung um eine Stelle halbiert den Wert
var9>>=2    # 0000 0001 Verschiebung um 2 Stellen nach rechts
print("var9 nach Rechtsverschiebung (2 Stellen):",var9, " binär:",bin(var9))

print("\nDurch Verschiebung rausfallende Bits können nicht wiederhergestellt werden.")
var10 = 3    # 0000 0011
print(("var10: ", var10, " binär:",bin(var10)))
var10 >>= 2  # 0000 0000
print("var10 nach zweifacher Rechtsverschiebung: ", var10, " binär:",bin(var10))
var10<<=2
print("var10 nach anschließender zweifacher Linksverschiebung: ", var10, " binär:",bin(var10))
# Durch Rechts- Verschiebung rausfallende positive Bits
# werden durch anschließende Links- Verschiebung nicht
# wiederhergestellt


# Bitweises OR
print("\nBitweises OR")
var11 = 4    # 0000 0100
print("var11:",var11, "binär: ", bin(var11))
print("Veroderung von var11(=4 bzw. 0100) mit 2 (0010)")
var11 |= 2   # 0000 0010
# 0000 0110
print("var11 nach VerODERung: ",var11," bzw.", bin(var11)) # var11 ist jetzt 6

# Bitweises AND
print("\nBitweises AND")
var12 = 4    # 0000 0100
print("var12:", var12, " bzw.", bin(var12))
var12 &= 2   # 0000 0010
# 0000 0000
print("var12 nach VerUNDung mit 2 (0010): ",var12, " bzw. ", bin(var12)) # var12 ist jetzt 0

# Bitweises XOR
print("\nBitweises XOR")
var13 = 5    # 0000 0101
print("var13:", var13, " bzw.", bin(var13))
var13 ^= 4   # 0000 0100
# 0000 0001
print("var9 nach VerXODERung mit 4 (0100): ",var13," bzw.", bin(var13)) # var13 ist jetzt 1

print("\nVerNOTen von 3 (siehe Zeile 192)")
print(~(0b11), bin(~(0b11)))
"""
Ausgabe: -4 -0b100 statt 252 0b11111100

Python wertet den Ausdruck ~0b00000011 als Zweierkomplement aus
Somit wird daraus nicht 252 sondern -4. 

siehe: Bildung eines Zweierkomplements bei NOT in Python

https://www.youtube.com/watch?v=__-OEo6CHQ8

Kurze Regel:

Ausgangspunkt positive Zahl:

Addiert 1 zu absoluten Wert und kehrt das Vorzeichen um zu Minus

Ausgangspunkt negative Zahl:

Substrahiert 1 vom absoluten Wert und kehrt das Vorzeichen um zu Plus

"""


