#Fichier pour  creer l'application python de manipulation de donnees 

import psycopg2

HOST ="tuxa.sme.utc"
USER = "nf18p032"
PASSWORD = "Fb9EyCL7x6mZ"
DATABASE = "dbnf18p032"

try :
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	print("Connexion réussie \n")
    #conn.close()
	
except Exception as error:
	print("Une exception s'est produite : ", error)
	print("Type d'exception : ", type(error))
class Artiste:
  def __init__(self,id, nom, type, origine, biographie):
    self.id=id
    self.nom=nom
    self.type=type
    self.origine=origine
    self.biographie=biographie

  def test_nom_groupe(conn, nom_g):
    try:
      cur=conn.cursor()
      sql= "SELECT G.Id_G FROM Groupe as G JOIN Artiste as A ON G.Id_G=A.Id WHERE A.nom=%s;" % (nom_g)
      cur.execute(sql)
    except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))
       return False, ""

    raw = cur.fetchone()

    if raw:
      return True, raw
    else:
      return False, ""

  def test_ID(conn, ID)-> int:
     try:
      cur=conn.cursor()
      sql="SELECT Id FROM Artiste WHERE Id=%s;" % (ID)
      cur.execute(sql)
     except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))  #gestion exception à revoir

     raw=cur.fetchone()
     if raw:
        return True
     else:
        return False
     
  def test_ID_g(conn, ID)-> int:
     try:
      cur=conn.cursor()
      sql="SELECT Id_g FROM Groupe WHERE Id=%s;" % (ID)
      cur.execute(sql)
     except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))
       return False
     
     raw=cur.fetchone()
     if raw:
        return True
     else:
        return False

  def insert(self,conn):
    id=str(input("Entrez le numéro d'ID \n"))
    while testID:
         id=str(input("Tapez un ID différent \n"))
         testID=self.test_id(conn,id)
    type=int(input("Tapez 1 s'il s'agit d'un artiste solo, 2 s'il s'agit d'un groupe ou 3 si c'est un artiste solo lié à un groupe \n"))
    type_test=True
    while type_test:
      if type==1:
        nom=str(input("Entrez le nom de l'artiste à ajouter:\n"))
        biographie=str(input("Entrez la biographie de l'artiste: \n"))
        type_test=False

      elif type==2:
        nom=str(input("Entrez le nom du groupe à ajouter:\n"))
        biographie=str(input("Entrez la biographie du groupe: \n"))
        type_test=False

      elif type==3:
        nom=str(input("Entrez le nom de l'artiste à ajouter:\n"))
        biographie=str(input("Entrez la biographie de l'artiste \n"))
        nom_g=str(input("Tapez le nom du groupe auquel appartient l'artiste \n"))
        test_g, id_g=self.test_nom_groupe(conn, nom_g)
        if test_g==False:
           nom_g=str(input("Tapez un nom de groupe différent \n"))
           test_g, id_g=self.test_groupe(conn, nom_g)
        type_test=False
      else:
        print("Erreur, tapez 1 pour solo, 2 pour groupe ou 3 pour solo appartenant à un groupe \n")

    origine=str(input("Entrez son origine : \n"))

    try:
      cur=conn.cursor() 
      sql = "INSERT INTO Artiste VALUES (%d, %s, %s, %s);" % (id, nom, biographie, origine)
      cur.execute(sql)

    except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))
    
    if type==1:
      try:
        cur=conn.cursor()
        sql= "INSERT INTO Solo VALUES ('%s', NULL);" % (id)
        cur.execute(sql)
      except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

    if type==2:
      try:
        cur=conn.cursor()
        sql= "INSERT INTO Groupe VALUES ('%s');" % (id)
        cur.execute(sql)
      except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))
    
    if type==3:
      try:
        cur=conn.cursor()
        sql= "INSERT INTO Solo VALUES ('%s', %s);" % (id, id_g)
        cur.execute(sql)
      except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

    return

  def afficher(self, conn, ID):
    test_groupe=self.test_ID_g
        
    try:
       cur = conn.cursor()
       sql= "SELECT id,nom,biographie,origine FROM Artiste WHERE id=%s;" %(ID)
       cur.execute(sql)

    except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

    raw= cur.fetchone()

    if test_groupe:
       print("Type : Groupe \n")

    else:
       print("Type: Solo \n")

    while raw:
      print("ID : %s \n", raw[0])
      print("Nom : %s \n", raw[1])
      print("Biographie : %s \n", raw[2])
      print("Origine : %s \n", raw[3])
      raw=cur.fetchone()



  def modifier(self, conn, ID):
    test_id=self.test_ID()
    if test_id==False:
       print("Artiste non trouvé")
    
    if test_id:
       print("Que voulez-vous modifier? \n")
       choix=int(input("Tapez 1 pour le nom, 2 pour la biographie, 3 pour l'origine, 0 pour quitter \n"))

       if choix==0:
          return 0
       if choix==1:
          nom=str(input("Tapez le nouveau nom : \n"))
          try:
            cur = conn.cursor()
            sql= "UPDATE Artiste SET Artiste.nom=%s WHERE Artiste.id=%s;" %(nom, ID)
            cur.execute(sql)

          except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))
       
       if choix==2:
          biographie=str(input("Tapez le nouveau nom : \n"))
          try:
            cur = conn.cursor()
            sql= "UPDATE Artiste SET Artiste.biographie=%s WHERE Artiste.id=%s;" %(biographie, ID)
            cur.execute(sql)

          except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))
          
       if choix==3:
          origine=str(input("Tapez le nouveau nom : \n"))
          try:
            cur = conn.cursor()
            sql= "UPDATE Artiste SET Artiste.origine=%s WHERE Artiste.id=%s;" %(origine, ID)
            cur.execute(sql)

          except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))

  def supprimer(self, conn, ID):
    test_id=self.test_ID()
    if test_id==False:
      print("Artiste non trouvé")

    if test_id:
       test_id_g=self.test_ID_g()
       if test_id_g:
          try:
            cur = conn.cursor()
            sql= "DELETE FROM Groupe WHERE Groupe.id_g=%s;" %(ID)
            cur.execute(sql)

          except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))

       else:
          try:
            cur = conn.cursor()
            sql= "DELETE FROM Solo WHERE Solo.id_S=%s;" %(ID)
            cur.execute(sql)

          except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))

       try:
            cur = conn.cursor()
            sql= "DELETE FROM Artiste WHERE Artiste.id=%s;" %(ID)
            cur.execute(sql)

       except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))
  




#DroitsEdition.ajouter et DroitsArtistiques.ajouter doivent être dans Chanson.ajouter 


class Interrogation:
   def Q1(conn):
      try:
        cur = conn.cursor()
        sql= "SELECT A.nom AS nom_artiste, AVG(C.Durée) AS durée_moyenne FROM Chanson C JOIN Album Ab ON C.Album = Ab.id JOIN Artiste A ON Ab.Artiste = A.id GROUP BY A.nom HAVING COUNT(*) >= 5;"
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
    
      raw=cur.fetchone()
      print("Nom   Durée moyenne \n")
      while raw:
         print(raw[0], raw[1])
         raw=cur.fetchone()
    
   
   def Q2(conn):
      try:
        cur = conn.cursor()
        sql= "SELECT A.nom AS nom_artiste, COUNT(*) AS nombre_de_chansons FROM Chanson C JOIN Album Ab ON C.Album = Ab.id JOIN Artiste A ON Ab.Artiste = A.id GROUP BY A.nom ORDER BY COUNT(*) DESC LIMIT 5;"
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
    
      raw=cur.fetchone()
      print("Nom   Nombre de chansons \n")
      while raw:
         print(raw[0], raw[1])
         raw=cur.fetchone()
    
   
   def Q3(conn):
      try:
        cur = conn.cursor()
        sql= "SELECT A.nom AS nom_artiste FROM Chanson C JOIN Album Ab ON C.Album = Ab.id JOIN Artiste A ON Ab.Artiste = A.id GROUP BY A.nom WHERE C.Durée > (TIME '00:05:00') ;"
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
    
      raw=cur.fetchone()
      print("Nom de l'artiste  Durée de la chanson \n")
      while raw:
         print(raw[0], raw[1])
         raw=cur.fetchone()
   
   def Q4(conn):
      try:
        cur = conn.cursor()
        sql= "SELECT P.genre, COUNT(P.genre) FROM Preferences P GROUP BY P.genre ORDER BY COUNT(P.genre) DESC;"
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
    
      raw=cur.fetchone()
      print("Nom de l'artiste  Durée de la chanson \n")
      while raw:
         print(raw[0], raw[1])
         raw=cur.fetchone()
      