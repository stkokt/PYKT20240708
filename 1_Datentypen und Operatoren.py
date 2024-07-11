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
//=     (wenn a = 10) a //= 4 (a == 2)


Logikoperatoren:

and, or, not


Bitweise Operatoren:

- &, |, ^, ~, <<, >>


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






