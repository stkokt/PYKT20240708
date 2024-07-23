# 1.  Gebe die Zahlen von 1 bis 10 rückwärts aus.
# Benutze dazu einmal einen while- Loop und einmal einen for- Loop.

# mit for- Loop
for n in range(10, 0, -1):
    print(n, end=" ")

print()
# mit while- Loop 
cnt10rev=0
while cnt10rev<10:
    print((cnt10rev-10)*-1, end=" ")
    cnt10rev+=1

print()
# 2.  Gebe die ganzen 10er bis 100 aus.
# Benutze dazu einmal einen while- Loop und einmal einen for- Loop.

# while- Loop
cnt10th=0
while cnt10th<=100:
    if cnt10th%10 == 0 and cnt10th != 0:
        print((cnt10th), end=" ")
    cnt10th+=1

print()

# for- Loop
for n in range(0,101, 10):
    if n!=0:
        print(n, end=" ")

print()

# for- Loop Variante 2
for n in range(101):
    if n!=0 and n%10==0:
        print(n, end=" ")

print()

vornamen = ['Madison', 'Michael', 'Oliver', 'Mia', 'Liam', 'Elijah', 'Amelia', 'Lucas', 
            'Ava', 'Chloe', 'William', 'Daniel', 'William', 'Joseph', 'Harper', 'Andrew', 
            'Sophia', 'Alexander', 'Olivia', 'Zoe', 'David', 'Noah', 'Abigail', 'Sophia', 
            'Matthew', 'Evelyn', 'Scarlett', 'Henry', 'Ava', 'Isabella', 'Mia', 'Grace', 
            'Emily', 'Benjamin', 'Emma', 'Benjamin', 'Emma', 'Lily', 'Olivia', 'Grace', 
            'Isabella', 'Elizabeth', 'Alexander', 'Charlotte', 'James', 'James', 'Sofia', 
            'Emily', 'Lily', 'Ella']

# 3.    Ermittle aus dieser Liste die Namen, die mehrfach genannt werden und gebe aus, 
#       wieviele und welche es sind.
duplikate=0
d_list=""
for name in vornamen:
    if vornamen.count(name) >1:
        if name not in d_list:
            duplikate+=1
            d_list += name + ", "
print(f"Die Liste der Vornamen enthält {duplikate} Mehrfache: {d_list}")

print()

# 4.  Ermittle aus dieser Liste die unterschiedlichen Anfangsbuchstaben der Namen
#     und gebe aus, wieviele es sind.

strAnfang = ""
for name in vornamen:
    if name[0] not in strAnfang:
        strAnfang += name[0]
print(f"Die Liste der Vornamen enthält {len(strAnfang)} unterschiedliche Anfangsbuchstaben.")

print()

# 5.  Ermittle die Primzahlen bis 100 und gebe sie aus.

""" 
# Primzahlen bis ...
obergrenze = int(input("Geben Sie die Obergrenze für die Suche nach Primzahlen ein: "))
for num in range(2, obergrenze + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
 """

# 6.  Baue mittels eines while- Loops ein Konsolenmenü.

menu=0

while menu != "x":
    print("1: Algorithmus 1\t2: Algorithmus 2\nx: Ende")
    menu=input("Wähle einen Menüpunkt:\n" )

    match menu:
        case "1":
            print("Algorithmus 1 gewählt.")
        case "2":
            print("Algorithmus 2 gewählt.")
        case "x":
            break
        case _:
            print("Bitte einen Menüpunkt wählen!")