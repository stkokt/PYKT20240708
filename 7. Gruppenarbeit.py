# LC = List Comprehension

#1 Erzeuge mittels LC eine Liste der Zahlen von 1-100 und gebe sie aus.

liste1=[x+1 for x in range(100)]        # Alternativ liste1=[x for x in range(1,101)]
print("Aufgabe 1\n")
print(liste1, "\n")

#2 Erzeuge aus der Liste oben mittels LC eine zweite Liste, in der alle Zahlen verdoppelt sind.

liste2=[x*2 for x in liste1]
print("Aufgabe 2\n")
print(liste2, "\n")

#3 Erzeuge aus der Liste oben mittels LC eine dritte Liste aller durch 3 teilbaren Zahlen bis 100.

liste3=[x for x in liste1 if x%3==0]
print("Aufgabe 3\n")
print(liste3, "\n")

#4
# Die Listen 4_1 und 4_2 sollen in Liste 4_3 so zusammengesetzt werden, 
# dass Liste 4_3 keine doppelten Zahlen enthält 
print("Aufgabe 4")
liste4_1=[50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 1.1, 100, 101, 102, 103, 104]
liste4_2=[76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 1.1, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148]
liste4_3=list(set(liste4_1 + liste4_2))
#liste4_3=list(set(liste4_1).union(liste4_2))     # Alternative Nils
print(liste4_3)


# Zusatz 4: Die Listen 4_1 und 4_2 enthalten einen gemeinsamen Floatwert. Liste 4_3 soll
# bis zu diesem Wert nur die Werte aus Liste 4_1 und ab diesem Wert nur Werte aus Liste 2 enthalten.
# Tipp: Wandle die Werte in einen String um und wende die String- Methode isdecimal() an. 

print("Zusatzaufgabe 4")
ind4_1=0
ind4_2=0
for x in liste4_1:
    if str(x).isdecimal():
        ind4_1=liste4_1.index(x)
for x in liste4_2:
    if str(x).isdecimal():
        ind4_1=liste4_2.index(x)
liste4_3=liste4_1[:ind4_1]+liste4_2[ind4_2:]
print(liste4_3)


#5 Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [[0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

print("Aufgabe 5\n")
import random
liste5=[x for x in range(100)]

tmpList=[]
listeOfFive=[]

for x in liste5:    
    if x%5==0:
        tmpList.append(liste5[x])
        listeOfFive.append(tmpList.copy())  # Hier Kopie statt Original, weil Listen mutable!
    else:
        listeOfFive.append(liste5[x])

print(listeOfFive)

# Alternativ per Funktion und LC:

"""
def listOf5(x):
    tmpList=[]
    if x%5==0:
        for x in range(x+1):
            if x%5==0:
                tmpList.append(x)
        return tmpList
    else:
        return x
    
listeOfFive=[listOf5(x) for x in range(100)]
"""

#6 Erzeuge ein Liste aus zufälligen 3-stelligen Zahlen (random Modul). Entferne von jeder die erste und die dritte Ziffer und quadriere die mittlere.
# Tipp: Wandle die Werte in einen String und dann in eine Liste um.

print("Aufgabe 6\n")
liste6=[random.randint(100, 999) for x in range(10)]
print(liste6, "\n")
liste6squared=[(int(list(str(x))[1]))**2 for x in liste6]

# liste6squared=[((x-(x//100*100))//10)**2 for x in liste6]     # Alternative Gordon

# alternativ: Funktion schreiben und in LC verwenden
""" def keepMiddleAndSquareIt(num):
    listOfNum=list(str(num)) # str: "345" -> list: ['3','4','5']
    return int(listOfNum[1])**2 # int: 4 ->**2: 16

liste6squared=[keepMiddleAndSquareIt(x) for x in liste6] """

print("\ngeaenderte Liste:\n", liste6squared, "\n")



#7 Erzeuge die Liste [[[1,2,3],[4,5,6],[7,8,9]], [10,11,12],[13,14,15],[16,17,18]], [18,20,21],[22,23,24],[25,26,27]]]
#   mittels LC

liste7=[[[i+1+j*3+k*9 for i in range(3)] for j in range(3)] for k in range(3)]
# liste7 = [[i, i+1, i+2] for i in range(1, 28, 3)]     # Alternative Silvio
# liste7=[[[ z+y*3+x*9 for z in range(1,4) ]for y in range(3) ] for x in range(3)]      # Alternative 
print("Aufgabe 7\n")
print(liste7)
