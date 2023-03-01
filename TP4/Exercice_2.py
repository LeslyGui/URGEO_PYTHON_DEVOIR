print("Vous allez rentrer lune quantite d'argent en gourdes. et je vais vous retourner sa valeur en dollars US")
US=150
valeur=-1
while valeur <=-1:
    Variable=input("entrer la quantité que vous voulez acheter . Valeur=")
    try:
        valeur=float(Variable)
        if valeur==0 :
            exit()
        else:
            Ht=valeur/US
            print("La valeur de" ,valeur, "gourdes correspond à",round(Ht,3), "$ US")
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")


