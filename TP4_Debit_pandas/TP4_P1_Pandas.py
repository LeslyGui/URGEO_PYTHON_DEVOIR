#########   ***** Nom: Guillite Lesly
#########   ***** Date: 1/04/2023

import pandas as pd
import matplotlib.pyplot as plt
import random
from math import sqrt

#Il faut specifier le separateur
data = pd.read_csv("data/MIREBALAIS___RIVIERE_ARTIBONITE_30202.txt", skiprows=22, sep=";")# lecture des donnees debit de Mirebalais
data_pluviomterie = pd.read_csv("data/P_068_ST_MICHEL.txt", skiprows=21, sep=";")# lecture des donnees pluviometriques de Saint-Michel

#pour connaitre les elements presents dans les fichiers
data.columns.values
data_pluviomterie.columns.values

#pour indexer les valeurs
data = data.assign(**{"M_Debit": [random.randint(0, 100)/100 for i in range(len(data))]})
data_pluviomterie = data_pluviomterie.assign(**{"M_Debit": [random.randint(0, 100)/100 for i in range(len(data_pluviomterie))]})

#Conversion en format numerique les donnees debits en mm/jr et les donnees pluviometriques
data['Q'] = pd.to_numeric(86.4*data['Q']/7463, errors='coerce')
data_pluviomterie['\tP'] = pd.to_numeric(data_pluviomterie['\tP'], errors='coerce')

#Suppression de ces lignes ou il n'y a aucune valeur
data_sans_na=data.dropna(subset=["Q"])
data_sans_na_pluviomtri=data_pluviomterie.dropna(subset=["\tP"])
#Conversion en format date

data_sans_na["Date"]=pd.to_datetime(data["Date"], format="%Y-%m-%d")
data_sans_na_pluviomtri["Date"]=pd.to_datetime(data_sans_na_pluviomtri["Date"], format="%Y-%m-%d")

######################                             Graph                           ##########################

#####################   minimal annuel ######################
data_minimal = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).min()# pour grouper les donnees en donnnees annuelles par valeurs minimales
data_minimal["Date"] = data_minimal.index # pour avoir les index des valeurs
data_minimal["Q"], data_minimal["Date"] = data_minimal["Date"], data_minimal["Q"] # permutation des emplacements
data_minimal.rename(columns={"Date": "Debit"}, inplace=True) # renommer les colonnes
data_minimal.rename(columns={"Q": "Date"}, inplace=True)
data_minimal.reset_index(drop=True, inplace=True)
data_minimal=data_minimal.drop(index=[13])# pour effacer l'annee 1935 

fig,ax1 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)# definir la largeur du graphe
ax1.plot(data_minimal["Date"], data_minimal["Debit"], label="Ecoulement minimum annuel Mirebalais sur la période 1922-1938 hormis 1935")
ax1.set_xlabel('Date') # affichage du nom de l'axe des abscisses
ax1.set_ylabel('Débit minimal annul enregistré')# affichage du nom de l'axe des ordonnees
ax1.legend()
plt.savefig("output/Ecoulement minimal annuel Mirebalais sur la période 1922-1938 hormis 1935")

#####################   maximal annuel ######################
data_maximal = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).max()# pour grouper les donnees en donnnees annuelles par valeurs maximales
data_maximal["Date"] = data_maximal.index # pour avoir les index des valeurs
data_maximal["Q"], data_maximal["Date"] = data_maximal["Date"], data_maximal["Q"] # permutation des emplacements
data_maximal.rename(columns={"Date": "Debit"}, inplace=True)
data_maximal.rename(columns={"Q": "Date"}, inplace=True)
data_maximal.reset_index(drop=True, inplace=True)
data_maximal=data_maximal.drop(index=[13])# pour effacer l'annee 1935 

fig,ax2 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
ax2.plot(data_maximal["Date"], data_maximal["Debit"], label="Ecoulement maximum annuel Mirebalais sur la période 1922-1938 hormis 1935")
ax2.set_xlabel('Date')
ax2.set_ylabel('Débit maximal enregistré')
ax2.legend()
plt.savefig("output/Ecoulement maximum annuel Mirebalais sur la période 1922-1938 hormis 1935")

#####################   moyenne annuelle ######################
data_moy = data_sans_na.groupby(pd.Grouper(key="Date", freq="Y")).mean() # pour grouper les donnees en donnnees annuelles par valeurs moyennnes
data_moy["Date"] = data_moy.index
data_moy["Q"], data_moy["Date"] = data_moy["Date"], data_moy["Q"]
data_moy.rename(columns={"Date": "Debit"}, inplace=True)
data_moy.rename(columns={"Q": "Date"}, inplace=True)
data_moy.reset_index(drop=True, inplace=True)
data_moy=data_moy.drop(index=[13])

fig,ax4 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
ax4.plot(data_moy["Date"], data_moy["Debit"], label="Ecoulement moyen annuel Mirebalais sur la période 1922-1938 hormis 1935")
ax4.set_xlabel('Date')
ax4.set_ylabel('débit moyen annuel enregistré')
ax4.legend()
plt.savefig("output/Ecoulement moyen annuel Mirebalais sur la période 1922-1938 hormis 1935")

#######################   debit moyen mensul   ####################
data_month = data_sans_na.groupby(pd.Grouper(key="Date", freq="M")).mean() # pour grouper les donnees en donnnees mensuelles par valeurs moyennnes
data_month["Date"] = data_month.index
data_month["Q"], data_month["Date"] = data_month["Date"], data_month["Q"]
data_month.rename(columns={"Date": "Debit"}, inplace=True)
data_month.rename(columns={"Q": "Date"}, inplace=True)
data_month.reset_index(drop=True, inplace=True)
data_month=data_month.drop(index=[147,148,149,150,151,152,153,154,155,156,157,158]) # pour enlever les mois de janvier a decembre de l'annee 1935

fig,axs3 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
axs3.plot(data_month["Date"], data_month["Debit"], label="Ecoulement moyen mensuel Mirebalais sur la période 1922-1938 hormis 1935")
axs3.set_xlabel('Date')
axs3.set_ylabel('Débit moyen enregistré')
axs3.legend()
plt.savefig("output/Ecoulement moyen mensuel Mirebalais sur la période 1922-1938 hormis 1935")
#######################   debit moyen mensul de type scatter debit  ####################  
fig,axs4 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
axs4.scatter(data_month["Date"], data_month["Debit"], label="Ecoulement moyen mensuel Mirebalais sur la période 1922-1938 hormis 1935")
axs4.set_xlabel('Date')
axs4.set_ylabel('Débit moyen enregistré')
axs4.legend()
plt.savefig("output/Ecoulement moyen mensuel scatter debit Mirebalais sur la période 1922-1938 hormis 1935")
#####################   moyenne annuelle 2 ans ######################
data_moy_2ans = data_sans_na.groupby(pd.Grouper(key="Date", freq="2Y")).mean() # pour grouper les donnees en donnnees annuelless par valeurs moyennnes sur 2 ans
data_moy_2ans["Date"] = data_moy_2ans.index
data_moy_2ans["Q"], data_moy_2ans["Date"] = data_moy_2ans["Date"], data_moy_2ans["Q"]
data_moy_2ans.rename(columns={"Date": "Debit"}, inplace=True)
data_moy_2ans.rename(columns={"Q": "Date"}, inplace=True)
data_moy_2ans.reset_index(drop=True, inplace=True)

fig,ax5 = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
ax5.plot(data_moy_2ans["Date"], data_moy_2ans["Debit"], label="Ecoulement moyen sur 2 ans Mirebalais sur la période 1922-1938 hormis 1935")
ax5.set_xlabel('dat')
ax5.set_ylabel('débit moyen annuel enrgistré')
ax5.legend()
plt.savefig("output/Ecoulement moyen sur 2 ans Mirebalais sur la période 1922-1938 hormis 1935")

####################   Division des donnees en 4 periodes  ######################

periode_1=data_sans_na.loc[0:1377, ["Date", "Q" ]]  # periode 1
Periode_1_min_annuel=periode_1.groupby(pd.Grouper(key="Date", freq="Y")).min() # periode 1 valeurs minimales sur les annees 
Periode_1_moyenne_annuelle=periode_1.groupby(pd.Grouper(key="Date", freq="Y")).mean() # periode 1 valeurs moyennes sur les annees 
Periode_1_max_annuel=periode_1.groupby(pd.Grouper(key="Date", freq="Y")).max() # periode 1 valeurs maximales sur les annees 
Periode_1_min_mensuel=periode_1.groupby(pd.Grouper(key="Date", freq="m")).min() # periode 1 valeurs minimales sur les mois
Periode_1_max_mensuel=periode_1.groupby(pd.Grouper(key="Date", freq="m")).max() # periode 1 valeurs maximales sur les mois
Periode_1_moyenne_mensuelle=periode_1.groupby(pd.Grouper(key="Date", freq="m")).mean() # periode 1 valeurs moyennes sur les mois
##############################     Periode 2     #######################
periode_2=data_sans_na.loc[1378:2755, ["Date", "Q" ]]# periode 2
Periode_2_min_annuel=periode_2.groupby(pd.Grouper(key="Date", freq="Y")).min() # periode 2 valeurs minimales sur les annees 
Periode_2_max_annuel=periode_2.groupby(pd.Grouper(key="Date", freq="Y")).max() # periode 2 valeurs maximales sur les annees
Periode_2_moyenne_annuelle=periode_2.groupby(pd.Grouper(key="Date", freq="Y")).mean() # periode 2 valeurs moyennes sur les annees
Periode_2_min_mensuel=periode_2.groupby(pd.Grouper(key="Date", freq="m")).min() # periode 2 valeurs minimales sur les mois
Periode_2_max_mensuel=periode_2.groupby(pd.Grouper(key="Date", freq="m")).max() # periode 2 valeurs maximales sur les mois
Periode_2_moyenne_mensuelle=periode_2.groupby(pd.Grouper(key="Date", freq="m")).mean() # periode 2 valeurs moyennes sur les mois
###############################    Periode 3   #####################
periode_3=data_sans_na.loc[2756:4164, ["Date", "Q" ]]
Periode_3_min_annuel=periode_3.groupby(pd.Grouper(key="Date", freq="Y")).min() # periode 3valeurs minimales sur les annees 
Periode_3_max_annuel=periode_3.groupby(pd.Grouper(key="Date", freq="Y")).max() # periode 3 valeurs maximales sur les annees
Periode_3_moyenne_annuelle=periode_3.groupby(pd.Grouper(key="Date", freq="Y")).mean() # periode 3 valeurs moyennes sur les annees
Periode_3_min_mensuel=periode_3.groupby(pd.Grouper(key="Date", freq="m")).min() # periode 3 valeurs minimales sur les mois
Periode_3_max_mensuel=periode_3.groupby(pd.Grouper(key="Date", freq="m")).max() # periode 3 valeurs maximales sur les mois
Periode_3_moyenne_mensuelle=periode_3.groupby(pd.Grouper(key="Date", freq="m")).mean() # periode 3 valeurs moyennes sur les mois
#####################    Periode 4
periode_4=data_sans_na.loc[4165:5540, ["Date", "Q" ]]
Periode_4_min_annuel=periode_4.groupby(pd.Grouper(key="Date", freq="Y")).min() # periode 4 valeurs minimales sur les annees 
Periode_4_max_annuel=periode_4.groupby(pd.Grouper(key="Date", freq="Y")).max() # periode 4 valeurs maximales sur les annees
Periode_4_moyenne_annuelle=periode_4.groupby(pd.Grouper(key="Date", freq="Y")).mean() # periode 4 valeurs moyennes sur les annees
Periode_4_min_mensuel=periode_4.groupby(pd.Grouper(key="Date", freq="m")).min() # periode 4 valeurs minimales sur les mois
Periode_4_max_mensuel=periode_4.groupby(pd.Grouper(key="Date", freq="m")).max() # periode 4 valeurs maximales sur les mois
Periode_4_moyenne_mensuelle=periode_4.groupby(pd.Grouper(key="Date", freq="m")).mean() # periode 4 valeurs moyennes sur les mois

#################################################     Graphe         ##################### 

###########################   Graphe periode 1 à 4 #################
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axs[0, 0].plot(periode_1["Date"],periode_1["Q"])    
axs[0, 0].set_title("Période 1")

axs[0, 1].plot(periode_2["Date"],periode_2["Q"])
axs[0, 1].set_title("Période 2")

axs[1, 0].plot(periode_3["Date"],periode_3["Q"])
axs[1, 0].set_title("Période 3")

axs[1, 1].plot(periode_4["Date"],periode_4["Q"])
axs[1, 1].set_title("Période 4")
plt.savefig("output/Periode 1 2 3 et 4.png")
######################  graphe max annuel division  #################
fig, axt = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axt[0, 0].plot(Periode_1_max_annuel)    
axt[0, 0].set_title("Période 1 maximum annuel")

axt[0, 1].plot(Periode_2_max_annuel)
axt[0, 1].set_title("Période 2 maximum annuel")

axt[1, 0].plot(Periode_3_max_annuel)
axt[1, 0].set_title("Période 3 maximum annuel")

axt[1, 1].plot(Periode_4_max_annuel)
axt[1, 1].set_title("Période 4 maximum annuel")

plt.savefig("output/Periode maximum annuel 1 2 3 et 4.png")
######################  graphe min annuel division #################
fig, axu = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axu[0, 0].plot(Periode_1_min_annuel)    
axu[0, 0].set_title("Période 1 minimum annuel")

axu[0, 1].plot(Periode_2_min_annuel)
axu[0, 1].set_title("Période 2 minimum annuel")

axu[1, 0].plot(Periode_3_min_annuel)
axu[1, 0].set_title("Période 3 minimum annuel")

axu[1, 1].plot(Periode_4_min_annuel)
axu[1, 1].set_title("Période 4 minimum annuel")

plt.savefig("output/Periode minimum annuel 1 2 3 et 4.png")
######################  graphe moyenne annuel division 
fig, axv = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axv[0, 0].plot(Periode_1_moyenne_annuelle)    
axv[0, 0].set_title("Période 1 moyenne annuelle")

axv[0, 1].plot(Periode_2_moyenne_annuelle)
axv[0, 1].set_title("Période 2 moyenne annuelle")

axv[1, 0].plot(Periode_3_moyenne_annuelle)
axv[1, 0].set_title("Période 3 moyenne annuelle")

axv[1, 1].plot(Periode_4_moyenne_annuelle)
axv[1, 1].set_title("Période 4 moyenne annuelle")

plt.savefig("output/Periode moyenne annuelle 1 2 3 et 4.png")
######################  graphe max mensuel #################
fig, axx = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axx[0, 0].plot(Periode_1_max_mensuel)    
axx[0, 0].set_title("Période 1 maximum mensuel")

axx[0, 1].plot(Periode_2_max_mensuel)
axx[0, 1].set_title("Période 2 maximum mensuel")

axx[1, 0].plot(Periode_3_max_mensuel)
axx[1, 0].set_title("Période 3 maximum mensuel")

axx[1, 1].plot(Periode_4_max_mensuel)
axx[1, 1].set_title("Période 4 maximum mensuel")

plt.savefig("output/Période maximum mensuel 1 2 3 et 4.png")
######################  graph min mensuel division  #################
fig, axw = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
axw[0, 0].plot(Periode_1_min_mensuel)    
axw[0, 0].set_title("Période 1 minimum mensuel")

axw[0, 1].plot(Periode_2_min_mensuel)
axw[0, 1].set_title("Période 2 minimum mensuel")

axw[1, 0].plot(Periode_3_min_mensuel)
axw[1, 0].set_title("Période 3 minimum mensuel")

axw[1, 1].plot(Periode_4_min_mensuel)
axw[1, 1].set_title("Période 4 minimum mensuel")

plt.savefig("output/periode minimum mensuel 1 2 3 et 4.png")
######################  graph moyenne mensuelle division 4 prio
fig, a = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
a[0, 0].plot(Periode_1_moyenne_mensuelle)    
a[0, 0].set_title("Période 1 moyenne mensuelle")

a[0, 1].plot(Periode_2_moyenne_annuelle)
a[0, 1].set_title("Période 2 moyenne mensuelle")

a[1, 0].plot(Periode_3_moyenne_annuelle)
a[1, 0].set_title("Période 3 moyenne mensuelle")

a[1, 1].plot(Periode_4_moyenne_annuelle)
a[1, 1].set_title("Période 4 moyenne mensuelle")

plt.savefig("output/Periode moyenne mensuelle 1 2 3 et 4.png")

############################################ pluviometrie #################################
######################   pluviometrie minimale  annuelle
data_minimal_pluviomtri_annul = data_sans_na_pluviomtri.groupby(pd.Grouper(key="Date", freq="Y")).min()
data_minimal_pluviomtri_annul["Date"] = data_minimal_pluviomtri_annul.index
data_minimal_pluviomtri_annul["\tP"], data_minimal_pluviomtri_annul["Date"] = data_minimal_pluviomtri_annul["Date"], data_minimal_pluviomtri_annul["\tP"]
data_minimal_pluviomtri_annul.rename(columns={"Date": "Pluviomtri"}, inplace=True)
data_minimal_pluviomtri_annul.rename(columns={"\tP": "Date"}, inplace=True)
data_minimal_pluviomtri_annul.reset_index(drop=True, inplace=True)

fig,axa = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
axa.plot(data_minimal_pluviomtri_annul["Date"], data_minimal_pluviomtri_annul["Pluviomtri"], label="pluviometrie minimum annuel Mirebalais sur la période 1920-1940")
axa.set_xlabel('Date')
axa.set_ylabel('pluviometrie moyenne enregistré')
axa.legend()
plt.savefig("output/pluviometrie minimale annuelle Mirebalais sur la période 1920-1940")

# ON remarque que la pluviometrie minimale pour chaque annee correspond a la valeur nulle c'est a dire que sa representation graphique est une ligne droite alors que pour le debit
# sa representation est une ligne brisée avec des pics. 
############################## pluviometrie maximale annuelle

data_maximal_pluviomtri_annul = data_sans_na_pluviomtri.groupby(pd.Grouper(key="Date", freq="Y")).max()
data_maximal_pluviomtri_annul["Date"] = data_maximal_pluviomtri_annul.index
data_maximal_pluviomtri_annul["\tP"], data_maximal_pluviomtri_annul["Date"] = data_maximal_pluviomtri_annul["Date"], data_maximal_pluviomtri_annul["\tP"]
data_maximal_pluviomtri_annul.rename(columns={"Date": "Pluviomtri"}, inplace=True)
data_maximal_pluviomtri_annul.rename(columns={"\tP": "Date"}, inplace=True)
data_maximal_pluviomtri_annul.reset_index(drop=True, inplace=True)

fig,axb = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
axb.plot(data_maximal_pluviomtri_annul["Date"], data_maximal_pluviomtri_annul["Pluviomtri"], label="pluviometrie maximum annuelle Mirebalais sur la période 1920-1940")
axb.set_xlabel('Date')
axb.set_ylabel('pluviometrie maximale enregistrée')
axb.legend()
plt.savefig("output/pluviometrie maximale annuelle Mirebalais sur la période 1920-1940")
# Les donnees pluviometries maximales sont plus elevees que celles des debits. 

############################## pluviometrie moyenne mensuelle
data_moynn_pluviomtri_mnsul = data_sans_na_pluviomtri.groupby(pd.Grouper(key="Date", freq="m")).mean()
data_moynn_pluviomtri_mnsul["Date"] = data_moynn_pluviomtri_mnsul.index
data_moynn_pluviomtri_mnsul["\tP"], data_moynn_pluviomtri_mnsul["Date"] = data_moynn_pluviomtri_mnsul["Date"], data_moynn_pluviomtri_mnsul["\tP"]
data_moynn_pluviomtri_mnsul.rename(columns={"Date": "Pluviomtri"}, inplace=True)
data_moynn_pluviomtri_mnsul.rename(columns={"\tP": "Date"}, inplace=True)
data_moynn_pluviomtri_mnsul.reset_index(drop=True, inplace=True)

fig,axj = plt.subplots(1, 1, figsize=(9, 9), sharey=True)
axj.scatter(data_moynn_pluviomtri_mnsul["Date"], data_moynn_pluviomtri_mnsul["Pluviomtri"], color="red" , alpha=0.5, label="pluviometrie moyen mensul Mirebalais sur la période 1920-1940")
axj.set_xlabel('Date')
axj.set_ylabel('pluviometrie moyenne mensulle enregistré')
axj.legend()
plt.savefig("output/pluviometrie moyenne mensuelle Mirebalais sur la période 1920-1940")

############################## pluviometrie moyenne mensuelle et debit mensuel face a face
fig, b = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(20,20))
b[0, 0].scatter(data_month["Date"], data_month["Debit"], label="Ecoulement moyen mensuel Mirebalais sur la période 1922-1938 hormis 1935")    
b[0, 0].set_title("Ecoulement moyen mensuel Mirebalais sur la période 1922-1938 hormis 1935")
b[0, 0].set_xlabel('Date')

b[1, 0].scatter(data_moynn_pluviomtri_mnsul["Date"], data_moynn_pluviomtri_mnsul["Pluviomtri"], color="red" , alpha=0.5, label="pluviometrie moyenne mensuel Mirebalais sur la période 1920-1940")
b[1, 0].set_title("pluviometrie moyen mensuel Mirebalais sur la période 1920-1940")
b[1, 0].set_xlabel('Date')

b[0, 1].remove()
b[1, 1].remove()

plt.savefig("output/scatter")

######################  Correlation differee ###############
fusionner_data_debit_pluviometrie=pd.merge(data_sans_na, data_sans_na_pluviomtri,on='Date') # fusionner les deux dataframes avec comme reference les valeurs des dates
#print(fusionner_data_debit_pluviometrie)

###########    Pour enregistrer le fichier
fichier1 = "output/fusionner_data_debit_pluviometrie.txt"
fusionner_data_debit_pluviometrie.to_csv(fichier1, sep="\t", index=False)

####################   fonction de Pearson avec la fonction Corr
r_pearson=round(fusionner_data_debit_pluviometrie["\tP"].corr(fusionner_data_debit_pluviometrie["Q"]),9)

####################   fonction de Pearson avec calcul a partir d'une fonction definie
def fonction_Pearson(liste_1, liste_2):  # fonction qui prend deux listes comme parametres, une pour la pluviometrie une pour le debit
    moyenne_liste_1=sum(liste_1)/len(liste_1) # calcul de la moyenne de la premiere liste
    moyenne_liste_2=sum(liste_2)/len(liste_2) # calcul de la moyenne de la deuxiemeliste
    somme=0
    somme_1=0
    somme_2=0
    for i in range(len(liste_1)):
        somme=somme+(liste_1[i]-moyenne_liste_1) *(liste_2[i]-moyenne_liste_2) # somme des valeurs qui seront au numerateur
        somme_1=somme_1+(liste_1[i]-moyenne_liste_1)**2 # somme de  la premiere partie qui sera au denominateur
        somme_2=somme_2+(liste_2[i]-moyenne_liste_2)**2 # somme de la deuxieme partie qui sera au denominateur
        produit=sqrt(somme_1*somme_2) # racine carre du produit des deux sommes du denominateur
    r=somme/produit # calcul de la correlation de Pearson
    return round(r,9) # retourne cette valeur

##################  Conversion des deux colonnes necessaire et calcul de la valeur du coefficient

liste_pluviometrie=fusionner_data_debit_pluviometrie['\tP'].tolist() # ecriture des valeurs des precipitations dans une liste
liste_debit=fusionner_data_debit_pluviometrie['Q'].tolist() # ecriture des valeurs des precipitations dans une liste

correlation= fonction_Pearson(liste_debit, liste_pluviometrie) # appel de la fonction de correlation 
print(correlation)
print(r_pearson)

plt.show()
# il y a donc une faible correlation positive entre nos donnéess