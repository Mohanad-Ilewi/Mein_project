 
txt = "Hallo IHR"
print (txt)

x = "python"
y = "is"
z = "awesome"

print (x, y, z)

x:int = 5; y:float = 7.5; 
x = 5; y = 7.5; 
z = x + y
print ( z )
print (type(x))
print (type(y))
print (type(z))


x = "Danke, es hat spaß gemacht"
print (x)
print (type (x))
print (str (x))

print (type(y))


wert1 = 100
wert2 = 23
if (wert1 > wert2):
    print ("wert1 ist größe als wert2")
else: 
    print ("wert1 ist kleiner als wert2")

a = False
if (a == True):
    print ("Nutzer eingeloggt")
else: 
    print ("Nutzer NICHT eingeloggt")

    Kind = 6
    if (Kind < 6):
        print ("Du gehst um 7:00 ins Bett")

    elif ((Kind >= 6) & (Kind < 12) ):
        print ("Du gehst um 22:00 ins Bett")

    else: 
        print ("Mach das Licht aus, wenn Du nach Hause kommst")



# [] = Liste
GaesteAnzahl = 30
isVegetariaDabei = True
mercimek = ["Zwiebel", "Öl", "Tomatenpaste", "rote Linsen", "Kartoffeln", "Minze"]
print (type (mercimek))
 
print (mercimek)
# append =  Wenn ich etwas vergessen habe und will hinzüfgen
mercimek.append ("Paprikapulver")
print (mercimek[0])       # das heißt print nur die ertse (Zwiebel)
print (mercimek[3])       # das heißt print die dritte in [rote Linsen] 
print (mercimek[4])

print ("Anzahl der Zutaten" + str(len(mercimek)))
mercimek.insert(2, "priese Salz")
for zutat in mercimek:
    print (zutat)
    print (len(zutat))

    Krimskrams = {"Knöpfe", "Aufnaeher", "Stifte"}
    print (type(Krimskrams))
    for zeugs in Krimskrams:
        print (zeugs)

    Gruppe = ("Anja", "Mohanad", "Florian")
    print (type(Gruppe))
    for teilnehmer in Gruppe:
        tn = teilnehmer
        print (teilnehmer)


