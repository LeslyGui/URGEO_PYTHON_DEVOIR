print("ok")
import pandas as pan

df= pan.read_csv("data/haiti_earthquake_pass7days_from_2023-01-18.csv")

taille =len(df)
#pour connaitre la taille du fichier
df.columns
#pour avoir les noms des en-tetes des colonnes.
df = df.assign(Impact ="Faible")
#Création de la colonne Impact et assignation a toutes les valeurs de la valeur "faible"
for l in range (taille):
  df.loc[df['magnitude'] < 2, 'Impact']="Tres faible"
  #comparaison des valeurs de la magnitude, si la condition est vérifiée, modifier la colonne Impact
df=df.reindex(columns=['#id', 'time', 'latitude [deg]', 'latitude_uncertainty [km]','depth_uncertainty [m]', 'magnitude','Impact','magnitude_type', 'mode','event_type' ])
#pour rearranger les colonnes dans l'ordre souhaité
print(df)
df.to_csv('output/haiti_earthquake_pass7days_from_2023-01-18.csv')
#pour enregistrer dans le output
