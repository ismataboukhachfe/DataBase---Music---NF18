#Fichier pour  creer l'application python de manipulation de donnees 

import psycopg2

class Artiste:
  def ajouter():
    type=int(input("Tapez 1 s'il s'agit d'un artiste solo ou 2 s'il s'agit d'un groupe))
      if type==1:
        nom=str(input("Entrez le nom de l'artiste à ajouter:\n"))
      elif type==2:
        nom=str(input("Entrez le nom du groupe à ajouter:\n"))
      else:
        print("Erreur, tapez 1 pour solo ou 2 pour groupe)
        
  
    origine=str(input("Entrez son origine : \n"))
    
  
