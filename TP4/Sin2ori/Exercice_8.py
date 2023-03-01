from math import sqrt
import math
import numpy as np
import random
import matplotlib.pyplot as plt

print("Vous allez rentrer 3 valeurs pour pouvoir generer une liste de coordonnees(x) dans le plan et je vais vous retourner la distance entre le Sinus de ces elements et l'origine")

#fonction qui genere les valeurs de x aleatoirement
def gen_distrib(debut, fin, m):
    Liste_x=random.uniform(debut,fin)
    return round(Liste_x,4)

#fonction qui calcule la distance entre deux points
def calc_distance_2D(x, y, m, n):
    distance=sqrt((x-m)**2+(y-n)**2)
    return round(distance,3)

#fonction qui renvoie le sinus d'une liste de valeur
def calc_sinus(liste_valeur):
    dim=len(liste_valeur)
    Sinus_liste=[]
    for l in range (dim):
        Sinus_liste.append(math.sin(math.radians(liste_valeur[l])))  #ecriture du sinus de l'element dans une liste avec la valeur de l'angle en degré
    return Sinus_liste

#fonction qui renvoie la liste de la distance entre l'origine et le sinus de la valeur du point genere aleatoirement
def calc_dist2ori(list_x, list_y):
    distance_entre_origine_coor_sinus_point=[]
    dim=len(list_x)
    for l in range(dim):
        distance_entre_origine_coor_sinus_point.append(calc_distance_2D(list_x[l], list_y[l], 0, 0))            
    return distance_entre_origine_coor_sinus_point


#Demande d'entree de debut, fin et de la longueur de la liste
dbt="a"
while dbt == "a":
    Variable=input("entrer la premiere valeur. valeur 1=")
    try:
        dbt=float(Variable)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere ")

fn="a"
while fn == "a":
    Variable_2=input("entrer la deuxieme valeur entiere. valeur 2=")
    try:
        fn=float(Variable_2)
    except:
        print("Vous devez rentrer un nombre et non une chaine de caractere")

longueur=-1
while longueur <= -1:
    Variable_1=input("entrer le nombre d'element de la liste .Longueur=")
    try:
        longueur=int(Variable_1)
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou un nombre décimale")

#genere une liste demandee     
print("voici la liste de valeur aléatoire comprise entre",dbt,"et",fn,"de dimension", longueur)
liste_element_x=[gen_distrib(dbt, fn, longueur) for i in range(longueur)]
print(liste_element_x)

#renverra une liste de floats représentant la distance entre chaque point de la fonction et l'origine (de coordonnées (0,0)).
fonction_sinus_liste=calc_sinus(liste_element_x)# appel de la fonction pour la liste generee
fonction_distance=calc_dist2ori(liste_element_x, fonction_sinus_liste)
print("Voici la distance")
print(fonction_distance)

with open("Sin2ori.txt",'w') as fillin:
    Abscisse=str(liste_element_x)[1:-1]# suppression des accolades[]. 1 pour le premier element de la chaine de caractere
    Ordonnee=str(fonction_distance)[1:-1]# suppression des accolades[]. -1 pour le dernier element de la chaine de caractere
    fillin.write(str(Abscisse))#Ecriture dans le fichier. La fonction Write, n'admet que des chaines de caractere.
    fillin.write("\n"+str(Ordonnee))  
fillin.close()

with open("Sin2ori.txt",'r') as fillin:
    lignes=fillin.read().split("\n")# Enregistrement de chaque ligne comme une chaine de caractere.
fillin.close

Abs=[float(x) for x in lignes[0].split(',')]# Conversion de chaque element de la premiere ligne en float
Ord=[float(x) for x in lignes[1].split(',')]# Conversion de chaque element de la premiere ligne en float

plt.figure(figsize=(8,8))
plt.plot(Abs, Ord)
plt.xlabel("x")
plt.ylabel("Distance de sin(x) à l'origine")
plt.savefig("sin2ori.png")
plt.show()


