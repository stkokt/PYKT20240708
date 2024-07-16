# if- elif- else Verzweigungen
# Zahlenbeispiel
var_a = 20
var_b = 20

if var_a < var_b:               # 'wenn' var_a kleiner var_b 
    print("Var A: ", var_a)     # dann Ausgabe dieser Zeile
elif var_a == var_b:            # 'sonst wenn' var_a gleich var_b
    print("Var A: ", var_a)     # dann Ausgabe dieser beiden Zeilen
    print("Var B: ", var_b)
else:                           # 'sonst' (also var_b ist größer)
    print("Var B: ", var_b)     # Ausgabe dieser Zeile


# Textbeispiel
var_c: str = "Text"
var_d: str = "text1"

if var_c[0].lower()==var_d[0].lower():  # Wenn Anfangsbuchstaben gleich (ohne Beachtung der Groß-, Kleinschreibweise)
    if len(var_c) == len(var_d):        # Wenn (außerdem) die Wortlänge gleich
        print(var_c, var_d)             # dann Ausgabe dieser Zeile
    else:                               # wenn Wortlänge ungleich
        print(var_c)                    # dann Ausgabe dieser Zeile
else:                                   # Wenn Anfangsbuchstaben ungleich (ohne Beachtung der Groß-, Kleinschreibweise)
    print(var_d)                        # dann Ausgabe dieser Zeile


# short- hand if
# anwendbar, wenn nur eine Befehlszeile folgt

var_e = 1
# IF- CONDITION : COMMAND
if var_e > 0: print("Zahl positiv")

# short- hand if else
# COMMAND           IF-CONDITION    ELSE- COMMAND
print("Zahl positiv") if var_e > 0 else print("Zahl 0 oder negativ")


# pass- Anweisung zum Überspringen von Konditionsblöcken

if var_e > 0:
    pass
elif var_e == 0:
    print("Zahl ist 0")
else:
    pass


