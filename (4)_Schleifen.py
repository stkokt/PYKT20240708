# ABBRUCHBEDINGUNG formulieren und aufpassen, dass sie erreicht wird
# while- Loop

# break, continue
cnt=0
while cnt<10:
    if cnt==5:
        break
    print(cnt, end=" ")
    cnt+=1

print()

cnt=0
while cnt<10:
    cnt+=1
    if cnt==5:
        continue
    print(cnt, end=" ")


# for- Loop / foreach- Loop

print("\nfor- Loop")
for number in range(10):
    print(number, end=" ")

# for each
# kann angewendet werden auf ein "iterable" (iterierbares Objekt)
print()
txt="Stefan"

for letter in txt:
    print(letter, end=",")

print()
liste = [7, 7.0, "7", True, [0,1,2]]

for elem in liste:
    print(type(elem))

print()

elem=0
while elem<len(liste):
    print(liste[elem])
    elem+=1


# Man kann Loops natürlich auch verschachteln:

for i in range(2):
    print("Äußere Schleife")
    for j in range(3):
        print("\tMittlere Schleife")
        for k in range(4):
            print("\t\tInnere Schleife")



