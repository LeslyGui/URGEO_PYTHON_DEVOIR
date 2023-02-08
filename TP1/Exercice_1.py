print("Vous allez rentrer deux valeurs réels et je vais vous retourner automatiquement la permutation")
Somme1=0
while Somme1==0:
    Nombre_1=input("entrer le premier nombre: Nombre 1=")
    try:
        Somme1=float(Nombre_1)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")
print(Somme1)

Somme2=0
while Somme2==0:
    Nombre_2=input("Entrer le second nombre: Nombre 2=")
    try:
        Somme2=float(Nombre_2)
    except:
         print("Vous devez rentrer un nombre et non une chaine de caractere")

print("La permutation est donc")
Nombre_3=Nombre_1
Nombre_1=Nombre_2
Nombre_2=Nombre_3
print("Le premier nombre devient " + Nombre_1 +".Le second devient " + Nombre_2)

