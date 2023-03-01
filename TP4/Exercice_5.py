print("Vous allez rentrer la quantité de TonmTonm que vous voulez acheter et je vous retournerai le prix que vous allez payer")
valeur=-1
while valeur <= -1:
    Variable=input("entrer la quantité que vous voulez acheter . Valeur=")
    try:
        valeur=int(Variable)
        if 0<=valeur<10 :
            print("Le prix de votre achat est", 50*valeur, "gourdes")
        if  10<=valeur<20 :
            print("Le prix de votre achat est", 40*valeur, "gourdes")
        if valeur>=20 :
            print("Le prix de votre achat est", 20*valeur, "gourdes")

    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

