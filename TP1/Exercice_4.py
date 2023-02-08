print("Vous allez rentrer deux valeurs et je vais vous renvoyer leur division euclidienne")
Entier_1=0
while Entier_1==0:
    Variable=input("entrer le premier entier. Entier 1=")
    try:
        Entier_1=int(Variable)
    except:
        print("Vous devez rentrer un entier et non une chaine de caractere ou une valeur décimale")

Entier_2=0
while Entier_2==0:
    Variable_1=input("Entrer le deuxieme entier. Entier 2=")
    try:
        Entier_2=int(Variable_1)
    except:
        print("Vous devez rentrer un entier et non une chaine de caractere ou une valeur décimale")

Quotient=int(Entier_1/Entier_2)
Reste=Entier_1-Quotient*Entier_2
print("La division euclidienne de " + str(Entier_1)+ " et de " + str(Entier_2)+ " donne un quotient égal à " + str(Quotient)+ " et un reste égal à " + str(Reste))
