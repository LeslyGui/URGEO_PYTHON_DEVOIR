import random

#La fonction renverra une liste de floats aléatoires entre debut et fin
def gen_distrib(debut, fin, n):
    Liste_x=random.uniform(debut,fin)
    return Liste_x

#Demande d'entree de debut, fin et de la longueur de la liste
print("Vous allez rentrer deux valeurs entieres et je vais vous retourner une liste aleatoire de valeur dependamment de la dimension de la liste que vous voulez avoir")
dbt="a"
while dbt=="a":
    Variable=input("entrer la premiere valeur. valeur 1=")
    try:
        dbt=float(Variable)
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

fn="a"
while fn =="a":
    Variable_2=input("entrer la deuxieme valeur entiere. valeur 2=")
    try:
        fn=float(Variable_2)
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

longueur="a"
while longueur =="a":
    Variable_1=input("entrer le nombre d'element de la liste .Longueur=")
    try:
        longueur=int(Variable_1)
    except:
        print("Vous devez rentrer un nombre entier  et non une chaine de caractere ou une nombre décimale")

#genere une liste demandee

print("voici la liste de valeur aléatoire comprise entre",dbt,"et",fn,"de dimension", longueur)
liste=[gen_distrib(dbt, fn, longueur) for i in range(longueur)]
for j in range(longueur):
    print(round(liste[j],4))

#fonction calc_stat() qui prend en argument une liste de floats et qui renvoie une liste de trois éléments contenant respectivement le minimum, le maximum et la moyenne de la liste
def calc_stat(liste_valeur):
    dim=len(liste_valeur)
    maximum_liste=max(liste_valeur) #récupere la valeur maximale de la liste
    minimun_liste=min(liste_valeur) #récupere la valeur minimale de la liste
    moyenne=sum(liste_valeur)/dim #calcule la moyenne des elements de la liste
    Liste_Element_statistique=[minimun_liste, maximum_liste, moyenne] #creation d'une liste avec les elements calculés
    return Liste_Element_statistique

#genere une liste statistique d'une liste entree plus haut avec comme parametre debut, fin et longueur de la liste
print("Statistique des valeurs aleatoires generes")
statistic_liste=calc_stat(liste)# appel de la fonction pour la liste generee
print("min=", round(min(statistic_liste),2))
print("max=",round(max(statistic_liste),2))
print("moyenne=",round(sum(statistic_liste)/len(statistic_liste),2))

# 20 listes aléatoires de 100 floats compris entre 0 et 100
print("Liste statistique de 20 listes générées aléatoirement")
dimension=20
liste_20_valeurs_floats=[] # initialisation d'une liste
liste_statistique_liste=[] # initialisation d'une liste
for j in range (dimension):
    liste_aleatoire_decimale=[gen_distrib(0,100,100) for l in range (20)] #genere une liste aleatoire
    liste_20_valeurs_floats.append(liste_aleatoire_decimale) # ecriture de cette liste dans la liste initialisee avant la boucle
    liste_statistique_liste.append(calc_stat(liste_aleatoire_decimale))#ecriture de la liste des statistiques(minimum, maximum, moyenne) pour chaque liste generee 
    print("liste",j,":","min=",round(liste_statistique_liste[j][0],2), "; max=", round(liste_statistique_liste[j][-2],2), "; moyenne=", round(liste_statistique_liste[j][-1],2))


# 1000 listes aléatoires de 100 floats compris entre 0 et 100
dimension=1000
print("Liste statistique de 1000 listes générées aléatoirement")
liste_1000_valeurs_floats=[] # initialisation d'une liste
liste_statistique_liste_1000=[] # initialisation d'une liste
for j in range (dimension):
    liste_aleatoire_decimale_1000=[gen_distrib(0,100,100) for l in range (1000)] #genere une liste aleatoire
    liste_1000_valeurs_floats.append(liste_aleatoire_decimale) # ecriture de cette liste dans la liste initialisee avant la boucle
    liste_statistique_liste_1000.append(calc_stat(liste_aleatoire_decimale_1000))#ecriture de la liste des statistiques(minimum, maximum, moyenne) pour chaque liste generee 
    print("liste",j,":","min=",round(liste_statistique_liste_1000[j][0],2), "; max=", round(liste_statistique_liste_1000[j][-2],2), "; moyenne=", round(liste_statistique_liste_1000[j][-1],2))


# 1000 listes aléatoires de 100 floats compris entre 0 et 100
dimension=10000
print("Liste statistique de 1000 listes générées aléatoirement")
liste_1000_valeurs_floats=[] # initialisation d'une liste
liste_statistique_liste_1000=[] # initialisation d'une liste
for j in range (dimension):
    liste_aleatoire_decimale_1000=[gen_distrib(0,100,100) for l in range (1000)] #genere une liste aleatoire
    liste_1000_valeurs_floats.append(liste_aleatoire_decimale) # ecriture de cette liste dans la liste initialisee avant la boucle
    liste_statistique_liste_1000.append(calc_stat(liste_aleatoire_decimale_1000))#ecriture de la liste des statistiques(minimum, maximum, moyenne) pour chaque liste generee 
    print("liste",j,":","min=",round(liste_statistique_liste_1000[j][0],2), "; max=", round(liste_statistique_liste_1000[j][-2],2), "; moyenne=", round(liste_statistique_liste_1000[j][-1],2))

print("La moyenne, la valeur minimale et maximale ne different pas trop suivant qu'on a une liste de 20, une liste de 1000 ou une liste de 10000 elements")
