from math import pi

print("Vous allez rentrer deux valeurs et je vais vous retourner le volume du cone associe")
valeur=-1
while valeur <= -1:
    Rayon=input("entrer la valeur du rayon=")
    try:
        valeur=float(Rayon)      
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere ou un nombre négatif")

valeur_2=-1
while valeur_2 <= -1:
    hauteur=input("entrer la valeur de la hauteur=")
    try:
        valeur_2=float(hauteur)      
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere ou un nombre négatif")

def volume_cone(x,y):
    return round(pi*(x**2)*y/3, 3)

volume=volume_cone(float(Rayon),float(hauteur))

print("Le volume du cone de rayon " + str(Rayon)+ " et de hauteur " + str(hauteur)+ " donne un volume de " + str(volume))

