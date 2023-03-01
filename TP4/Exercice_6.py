
from math import sqrt
print("Vous allez rentrer les coordonnées de deux points dans l'espace et je vais vous retourner la distance entre les deux points")

def calc_distance_3D(x, y, z, m, n ,p):#fonction qui prend 6 valeurs qui representent les coordonnees des 2 points dans l'espace
    distance=sqrt((x-m)**2+(y-n)**2+(z-p)**2)
    return round(distance,3)

Abscisse_Point_1="a"
while Abscisse_Point_1=="a":
    Nombre_1=input("entrer l'abscisse du premier point': Abscisse_1=")
    try:
        Abscisse_Point_1=float(Nombre_1)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

Ordonnee_Point_1="a"
while Ordonnee_Point_1=="a":
    Nombre_2=input("entrer l'Ordonnee du premier point: Ordonnee_1=")
    try:
        Ordonnee_Point_1=float(Nombre_2)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

Altitude_Point_1="a"
while Altitude_Point_1=="a":
    Nombre_3=input("entrer l'altitude du premier point: Altitude_1=")
    try:
        Altitude_Point_1=float(Nombre_3)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

Abscisse_Point_2="a"
while Abscisse_Point_2=="a":
    Nombre_4=input("entrer l'abscisse du second point: Abscisse_2=")
    try:
       Abscisse_Point_2=float(Nombre_4)
    except:
         print("Vous devez rentrer un nombre et non une chaine de caractere")


Ordonnee_Point_2="a"
while Ordonnee_Point_2=="a":
    Nombre_5=input("Entrer l'Ordonnee du second point: Ordonnee_2=")
    try:
       Ordonnee_Point_2=float(Nombre_5)
    except:
         print("Vous devez rentrer un nombre et non une chaine de caractere")

Altitude_Point_2="a"
while Altitude_Point_2=="a":
    Nombre_6=input("entrer l'altitude du second point: Altitude_2=")
    try:
       Altitude_Point_2=float(Nombre_6)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

dis=calc_distance_3D(float(Abscisse_Point_1) ,float(Ordonnee_Point_1) ,float(Altitude_Point_1),float(Abscisse_Point_2),float(Ordonnee_Point_2) ,float(Altitude_Point_2))
print("La distance entre les deux points est donc",dis)
