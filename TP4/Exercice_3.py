print("Vous allez rentrer une valeur et je vais vous dire si ce nombre est pair ou pas")
Entier_1=-1
while Entier_1<=-1:
    Variable=input("entrer le premier entier. Entier 1=")
    try:
        Entier_1=int(Variable)
    except:
        print("Vous devez rentrer un entier et non une chaine de caractere ou une valeur décimale")

Quotient=int(Entier_1/2)
Reste=Entier_1-Quotient*2
if Reste>0:
    print("ImPair")
else:
    print("pair")

