print("Vous allez rentrer le rayon d'un cercle et je vais vous retourner automatiquement son perimetre et sa surface")
Rayon=0
while Rayon==0:
    Nombre_1=input("entrer le rayon du cercle: Rayon=")
    try:
       Rayon=float(Nombre_1)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")
Perimetre=6.28*Rayon
Surface=3.14*Rayon*Rayon
print("Le périmètre du cercle de rayon " + str(Rayon)+" est:" + str(Perimetre))
print("La surface du cercle de rayon " + str(Rayon)+ " est:" + str(Surface))


