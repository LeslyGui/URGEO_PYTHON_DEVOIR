print("Vous allez rentrer les dimensions d'une salle et je vais vous retourner automatiquement son volume")
Longueur=0
while Longueur==0:
    Variable=input("entrer la longueur de la salle. Longueur=")
    try:
        Longueur=float(Variable)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

Largeur=0
while Largeur==0:
    Variable_1=input("entrer la largeur de la salle. Largeur=")
    try:
        Largeur=float(Variable_1)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")
   
Hauteur=0
while Hauteur==0:
    Variable_2=input("entrer la hauteur de la salle. Hauteur=")
    try:
        Hauteur=float(Variable_2)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

Volume=Longueur*Largeur*Hauteur
print("Le volume de la salle répondant aux dimensions suivantes: Longueur= " + str(Longueur)+" Largeur= " + str(Largeur) + " Hauteur= " + str(Hauteur)+ " est égale à " +str(Volume))

    




    

