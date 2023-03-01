from math import *
def fact(n):
    if n== 0:
        return 1
    return n*fact(n-1)

print("Vous allez rentrer une valeur entiere et je vais vous retourner la valeur approximative definit par e=sum(1/factorielle(n))")
valeur=-1
while valeur <= -1:
    Variable=input("entrer la valeur de la limite . Valeur=")
    try:
        valeur=int(Variable)
        e=0
        for l in range(valeur+1):
            e=e+1/fact(l)
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

print(e)

