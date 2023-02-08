# fonction recursif qui donne la suite de Fibonnaci associé au rand de la suite que l'utilisateur va rentrer

def fibonnaci(nombre):
    if nombre<=1:
        return nombre
    else:
     return fibonnaci(nombre-1)+fibonnaci(nombre-2)

print("Vous allez rentrer une valeur et je vais vous retourner sa suite de Fibonnaci")
valeur=-1
while valeur <= -1:
    Variable=input("entrer la valeur de la limite dont vous voulez connaitre la suite de Fibonnaci associée. Valeur=")
    try:
        valeur=int(Variable)
        for l in range(valeur+1):
            print(fibonnaci(l))
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

#print(fibonnaci(valeur))
