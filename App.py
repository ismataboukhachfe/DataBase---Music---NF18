#Fichier pour  creer l'application python de manipulation de donnees

import psycopg2

HOST ="tuxa.sme.utc"
USER = "nf18p032"
PASSWORD = "Fb9EyCL7x6mZ"
DATABASE = "dbnf18p032"

try :
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	print("Connexion réussie \n")
    #

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
      sql="SELECT Id FROM Artiste WHERE Id='%s';" % (ID)
      cur.execute(sql)
     except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

     raw=cur.fetchone()
     if raw:
        return True
     else:
        return False

  def test_ID_g(conn, ID)-> int:
     try:
      cur=conn.cursor()
      sql="SELECT Id_g FROM Groupe WHERE Id_g='%s';" % (ID)
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

  def ajouter(self,conn):
    id=str(input("Entrez le numéro d'ID \n"))
    testID=self.test_ID(id)
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
        sql= "INSERT INTO Solo VALUES ('%s', '%s');" % (id, id_g)
        cur.execute(sql)
      except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

    return

  def afficher(self, conn):
    ID=str(input("Tapez l'ID de l'artiste ou tapez 0 pour afficher tous les artistes\n"))
    if ID=='0':
       try:
        cur = conn.cursor()
        sql= "SELECT id,nom,biographie,origine FROM Artiste ;"
        cur.execute(sql)

       except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

       raw= cur.fetchone()


       while raw:
         print("ID : %s \n"% raw[0])
         print("Nom : %s \n"% raw[1])
         print("Biographie : %s \n"% raw[2])
         print("Origine : %s \n"% raw[3])
         raw=cur.fetchone()


    else:
        test_groupe=self.test_ID_g(conn,ID)
    
    
        try:
           cur = conn.cursor()
           sql= "SELECT id,nom,biographie,origine FROM Artiste WHERE id='%s';" %(ID)
           cur.execute(sql)
    
        except Exception as error:
           print("Une exception s'est produite : ", error)
           print("Type d'exception : ", type(error))
    
        raw= cur.fetchone()
    
        if test_groupe:
           print("Type : Groupe \n")
    
    
        while raw:
          print("ID : %s \n"% raw[0])
          print("Nom : %s \n"% raw[1])
          print("Biographie : %s \n"% raw[2])
          print("Origine : %s \n"% raw[3])
          raw=cur.fetchone()



  def modifier(self, conn):
    ID=str(input("Tapez l'ID de l'artiste"))
    test_id=self.test_ID(ID)
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



class DroitsEdition:
   def ajouter(self, conn, ID_chanson, nom_e):
      try:
        cur=conn.cursor()
        sql = "INSERT INTO DroitsEdition VALUES (%s , '%s');" % (nom_e, ID_chanson)
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
   
   def afficherdroit(self,conn, id_c):
      try:
         cur=conn.cursor()
         sql =" SELECT id_c, nom_e FROM DroitsEdition WHERE id_c='%s'"%(id_c)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

      raw=cur.fetchone()
      while raw:
        print("ID Chanson: %s \n"% raw[0])
        print("Nom éditeur : %s \n"% raw[1])
        raw=cur.fetchone()  
      
   def afficherliste(self,conn,nom_e):
      try:
         cur=conn.cursor()
         sql =" SELECT id_c, nom_e FROM DroitsEdition WHERE nom_e='%s'"%(nom_e)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))   

      raw=cur.fetchone()
      while raw:
        print("ID Chanson: %s \n"% raw[0])
        print("Nom éditeur : %s \n"% raw[1])
        raw=cur.fetchone()  
class DroitsArtistiques:
   def ajouter(self,conn,ID_chanson, ID_Artiste, type):
      try:
        cur=conn.cursor()
        sql = "INSERT INTO DroitsArtistiques VALUES ('%s' , '%s', %s);" % (ID_chanson,ID_Artiste, type)
        cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

   def afficherdroit(self,conn, id_c):
      try:
         cur=conn.cursor()
         sql =" SELECT id_c, id_a, type FROM DroitsArtistiques WHERE id_c='%s'"%(id_c)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

      raw=cur.fetchone()
      while raw:
        print("ID Chanson: %s \n"% raw[0])
        print("ID Artiste : %s \n"% raw[1])
        print("Type : %s \n"% raw[2])
        raw=cur.fetchone()     
      
   def afficherliste(self,conn,id_a):
      try:
         cur=conn.cursor()
         sql =" SELECT id_c, id_a, type FROM DroitsArtistiques WHERE id_a='%s'"%(id_a)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

      raw=cur.fetchone()
      while raw:
        print("ID Chanson: %s \n"% raw[0])
        print("ID Artiste : %s \n"% raw[1])
        print("Type : %s \n"% raw[2])
        raw=cur.fetchone()     


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
        sql=  '''SELECT A.nom AS nom_artiste
	FROM Chanson C
	JOIN Album Ab ON C.Album = Ab.id
	JOIN Artiste A ON Ab.Artiste = A.id
	WHERE C.Durée > INTERVAL '5' MINUTE
	GROUP BY A.nom;'''

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



class Utilisateur : 
    
    def __init__(self,identifiant,nom_utilisateur, motdepasse,adressemail,dateinscription,typeu ):
       
        self.identifiant = identifiant 
        self.nom_utilisateur = nom_utilisateur 
        self.motdepasse = motdepasse
        self.adressemail = adressemail 
        self.dateinscription = dateinscription 
        self.typeu = typeu
        
    def test_ID(conn, ID)-> int:
     cur=conn.cursor()
     sql="SELECT Id FROM Utilisateur WHERE identifiant =%s" % (ID)
     cur.execute(sql)

     raw=cur.fetchone()
     if raw:
        return True
     if raw:
        return False   
    
    def ajouter(self,conn) :
        
        self.identifiant = str(input("Entrer l'identifiant : "))
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))
        self.motdepasse = str(input("Entrer le mot de passe : "))
        self.adressemail = str(input("Entrer l'adressemail: "))
        self.dateinscription = str(input("Entrer la date user=Utilisateur() d'inscription : "))
        typeu = int(input("Entrer 1 si premium , 0 si non"))
        if typeu == 1 : self.typeu = 'premium'
        if typeu == 0 : self.typeu = 'régulier'
        
        if self.test_ID(self.identifiant) == True : 
            print("Impossible car l'identifiant existe deja, veuillez essayer un autre identifiant")
            return 
        
        sql = "INSERT INTO utilisateur VALUES ('%s', '%s', '%s','%s','%s','%s')" % (self.identifiant, self.nom_utilisateur, self.motdepasse,self.adressemail,self.dateinscription,self.typeu)
        
        cur = conn.cursor()
        cur.execute(sql)
        
        
        
    def modifier(self,conn):
        
    
        self.identifiant = str(input("Entrer l'identifiant : "))
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))
        self.motdepasse = str(input("Entrer le mot de passe : "))
        self.adressemail = str(input("Entrer l'adressemail: "))
        self.dateinscription = str(input("Entrer la date d'inscription : "))
        typeu = int(input("Entrer 1 si premium , 0 si non"))
        if typeu == 1 : self.typeu = 'premium'
        if typeu == 0 : self.typeu = 'régulier'
    
    
        sql = """
        UPDATE utilisateur
        SET nom_utilisateur = '%s', motdepasse = '%s', adressemail = '%s', dateinscription = '%s, type = '%s' 
        WHERE identifiant = '%s'  """ % (self.nom_utilisateur, self.motdepasse,self.adressemail,self.dateinscription,self.typeu,self.identifiant) 
       
        
        cur = conn.cursor()
        cur.execute(sql)
        
        cur.close()        
    
    
    def delete(self, conn):
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))

        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '/s " % self.nom_utilisateur
        
        cur = conn.cursor()
        cur.execute(sql)
        
        cur.close()
        print(f"Utilisateur '{self.nom_utilisateur}' a été supprimé.")
        
    def affichage(self,conn) : 
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))

        sql = "SELECT * FROM utilisateur WHERE nom_utilisateur = '%s'" % self.nom_utilisateur
    
        cur = conn.cursor()
        cur.execute(sql)
        user = cur.fetchone()
        cur.close()
    
        if user:
            print(f"Identifiant: {user[0]}")
            print(f"Nom d'utilisateur: {user[1]}")
            print(f"Mot de passe: {user[2]}")
            print(f"Adresse email: {user[3]}")
            print(f"Date d'inscription: {user[4]}")
            print(f"type: {user[5]}")
        else:
            print(f"Utilisateur avec le nom '{self.nom_utilisateur}' non trouvé.")


class Genre :
    
    def __init__(self,nom) : 
        self.nom = nom 
        
    def test_nom(conn, nom)-> int:
         cur=conn.cursor()
         sql="SELECT Id FROM genre WHERE nom =%s" % (nom)
         cur.execute(sql)

         raw=cur.fetchone()
         if raw:
            return True
         if raw:
            return False   
    
    def ajouter(self,conn) :
        
        self.nom = str(input("Entrer le genre que vous voulez ajouter : "))
        
        if self.test_nom(self.nom) == True : 
            print("Impossible car le nom existe deja")
            return 
        sql = "INSERT INTO genre VALUES ('%s')" % (self.nom)
        
        cur = conn.cursor()
        cur.execute(sql)
        
        
        
    def affichage(self, conn):
        sql = "SELECT * FROM genre"
    
        cur = conn.cursor()
        cur.execute(sql)
        genres = cur.fetchall()  # Fetch all rows
        for genre in genres:
            print(genre)
        cur.close()
        
    
    def delete(self, conn):
        self.nom = str(input("Entrer le genre que vous voulez ajouter : "))

        sql = "DELETE FROM genre WHERE genre = '/s' " % self.nom
        
        cur = conn.cursor()
        cur.execute(sql)
        
        cur.close()
        print(f"Utilisateur '{self.nom}' a été supprimé.")

class Album:

    def __init__(self, id, titre, sortie, artiste):
        self.id = id
        self.titre = titre
        self.sortie = sortie
        self.artiste = artiste

    
    def test_ID(conn, ID) -> bool:
        cur = conn.cursor()
        sql = "SELECT Id FROM Artiste WHERE Id = %s"
        cur.execute(sql, (ID,))
        raw = cur.fetchone()
        cur.close()
        return raw is not None

    def insert(self, conn):
        self.id = input("Id : ")
        while self.test_ID(conn, self.id):
            self.id = input("Id : ")

        self.titre = input("Titre : ")
        self.sortie = input("Sortie (YYYY-MM-DD) : ")
        self.artiste = input("Artiste : ")

        cur = conn.cursor()
        sql = """
        INSERT INTO Album (Id, Titre, Sortie, Artiste) 
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(sql, (self.id, self.titre, self.sortie, self.artiste))
        
        cur.close()

    def modifier(self, conn):
        id = input("Id : ")
        while not self.test_ID(conn, id):
            id = input("Id : ")

        self.titre = input("Titre : ")
        self.sortie = input("Sortie (YYYY-MM-DD) : ")
        self.artiste = input("Artiste : ")

        sql = """
        UPDATE Album 
        SET Titre = %s, Sortie = %s, Artiste = %s 
        WHERE Id = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (self.titre, self.sortie, self.artiste, id))
        
        cur.close()

    def delete(self, conn):
        id = input("Id : ")
        while not self.test_ID(conn, id):
            id = input("Id : ")

        sql = "DELETE FROM Album WHERE Id = %s"
        cur = conn.cursor()
        cur.execute(sql, (id,))
        
        cur.close()
        print(f"Album '{id}' a été supprimé.")

    def affichage(conn):
        sql = "SELECT * FROM Album"
        cur = conn.cursor()
        cur.execute(sql)
        albums = cur.fetchall()
        cur.close()
        
        if albums:
            for album in albums:
                print(f"Id: {album[0]}")
                print(f"Titre: {album[1]}")
                print(f"Sortie: {album[2]}")
                print(f"Artiste: {album[3]}")
                print()
        else:
            print("Aucun album trouvé.")

class Chanson:

        

    def __init__(self, id, titre, duree, pays, album, genre):
        self.id = id
        self.titre = titre
        self.duree = duree
        self.pays = pays
        self.album = album
        self.genre = genre

    def test_ID(conn, ID)-> int:
        cur=conn.cursor()
        sql="SELECT Id FROM Artiste WHERE Id=%s" % (ID)
        cur.execute(sql)
        
        raw=cur.fetchone()
        if raw:
           return True
        else:
           return False

    def insert(self):
    
        id = str(input("Id : "))
        while self.test_ID(conn,id):
            id = str(input("Id : "))

        self.titre = str(input("Titre : "))
        self.duree = str(input("Duree : "))
        self.pays = str(input("Pays : "))
        self.album = str(input("Album : "))
        self.genre = str(input("Genre : "))

        
        cur = conn.cursor()
        sql = "INSERT INTO Chanson (Id, Titre, Duree, Pays, Album, Genre) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        cur.execute(sql, (self.id, self.titre, self.duree, self.pays, self.album, self.genre))
        
        
        
    def modifier(self,conn):
    
        self.id = str(input("Id : "))
        while not(self.test_ID(conn,id)):
            self.id = str(input("Id : "))

        self.titre = str(input("Titre : "))
        self.duree = str(input("Duree : "))
        self.pays = str(input("Pays : "))
        self.album = str(input("Album : "))
        self.genre = str(input("Genre : "))

    
        sql = "UPDATE Chanson SET Titre = '%s', Duree = '%s', Pays = '%s', Album = '%s', Genre ='%s' WHERE id = '%s' " % (self.titre, self.duree, self.pays, self.album, self.genre, self.id) 
        
        cur = conn.cursor()
        cur.execute(sql)
        
        cur.close()   
        
    def delete(self, conn):
        
        id = str(input("Id : "))
        while not(self.test_ID(conn,id)):
            id = str(input("Id : "))
        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '%s' " %id
        
        cur = conn.cursor()
        cur.execute(sql)
        
        cur.close()
        print(f"Utilisateur '{id}' a été supprimé.")

    def affichage(conn):
        sql = """    
            SELECT * FROM Chanson
        """       
        cur = conn.cursor()
        cur.execute(sql)
        song = cur.fetchone()
        cur.close()
    
        if user:
            print(f"Identifiant: {song[0]}")
            print(f"Titre: {song[1]}")
            print(f"Duree: {song[2]}")
            print(f"Pays: {song[3]}")
            print(f"Album: {song[4]}")
            print(f"Genre: {song[5]}")
        else:
            print(f"Chanson avec le nom '{song}' non trouvé.")
        

class ContientAlbum:

    def __init__(self, album, playlist):
        self.album = album
        self.playlist = playlist

    
    def test_ID(conn, table, ID) -> bool:
        cur = conn.cursor()
        sql = "SELECT Id FROM %s WHERE Id = %%s" % table
        cur.execute(sql, (ID,))
        raw = cur.fetchone()
        cur.close()
        return raw is not None

    def insert(self, conn):
        self.album = input("Album ID : ")
        while not self.test_ID(conn, "Album", self.album):
            self.album = input("Album ID : ")

        self.playlist = input("Playlist ID : ")
        while not self.test_ID(conn, "Playlist", self.playlist):
            self.playlist = input("Playlist ID : ")

        cur = conn.cursor()
        sql = """
        INSERT INTO ContientAlbum (album, playlist) 
        VALUES (%s, %s)
        """
        cur.execute(sql, (self.album, self.playlist))
        
        cur.close()

    def modifier(self, conn):
        old_album = input("Old Album ID : ")
        old_playlist = input("Old Playlist ID : ")
        while not self.test_ID(conn, "ContientAlbum", (old_album, old_playlist)):
            old_album = input("Old Album ID : ")
            old_playlist = input("Old Playlist ID : ")

        self.album = input("New Album ID : ")
        while not self.test_ID(conn, "Album", self.album):
            self.album = input("New Album ID : ")

        self.playlist = input("New Playlist ID : ")
        while not self.test_ID(conn, "Playlist", self.playlist):
            self.playlist = input("New Playlist ID : ")

        sql = """
        UPDATE ContientAlbum 
        SET album = %s, playlist = %s
        WHERE album = %s AND playlist = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (self.album, self.playlist, old_album, old_playlist))
        
        cur.close()

    def delete(self, conn):
        album = input("Album ID : ")
        playlist = input("Playlist ID : ")
        while not self.test_ID(conn, "ContientAlbum", (album, playlist)):
            album = input("Album ID : ")
            playlist = input("Playlist ID : ")

        sql = "DELETE FROM ContientAlbum WHERE album = %s AND playlist = %s"
        cur = conn.cursor()
        cur.execute(sql, (album, playlist))
        
        cur.close()
        print(f"Liaison entre l'album '{album}' et la playlist '{playlist}' a été supprimée.")

    
    def affichage(conn):
        sql = "SELECT * FROM ContientAlbum"
        cur = conn.cursor()
        cur.execute(sql)
        links = cur.fetchall()
        cur.close()
        
        if links:
            for link in links:
                print(f"Album: {link[0]}")
                print(f"Playlist: {link[1]}")
                print()
        else:
            print("Aucune liaison trouvée.")

class ContientChanson:

    def inserer(conn,idPlaylist, idChanson):
        cursor = conn.cursor()
        insertion = "INSERT INTO ContientChanson VALUES ('%s', '%s')" % (idPlaylist, idChanson)
        cursor.execute(insertion)
        
        

    
    def modifier(conn,colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE ContientChanson SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        
        

    def supprimer(conn,condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM ContientChanson WHERE %s" % (condition)
        cursor.execute(suppression)
        
        

    def afficherTous(conn):
        cursor = conn.cursor()
        affichage = "SELECT * FROM ContientChanson"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        
	    
    def afficherParCondition(conn,condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM ContientChanson WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        
#----------------------------------------------------------------------------------------------------#
class Historique:
    def inserer(conn,chanson, utilisateur, compteur):
        cursor = conn.cursor()
        insertion = "INSERT INTO Historique VALUES ('%s', '%s', '%s')" % (chanson, utilisateur, compteur)
        cursor.execute(insertion)
        
        

    def modifier(conn,colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Historique SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        
        

    def supprimer(conn,condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Historique WHERE %s" % (condition)
        cursor.execute(suppression)
        
        

    def afficherTous(conn):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Historique"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1], rawdata[2])
            rawdata = cursor.fetchone()
        

    def afficherParCondition(conn,condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Historique WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1], rawdata[2])
            rawdata = cursor.fetchone()
        
#----------------------------------------------------------------------------------------------------#
class Amis:
    def inserer(conn,utilisateur1, utilisateur2):
        cursor = conn.cursor()
        insertion = "INSERT INTO Amis VALUES ('%s', '%s')" % (utilisateur1, utilisateur2)
        cursor.execute(insertion)
        
        

    def modifier(conn,colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Amis SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        
        

    def supprimer(conn,condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Amis WHERE %s" % (condition)
        cursor.execute(suppression)
        
        
    def afficherTous(conn):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Amis"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        

    def afficherParCondition(conn,condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Amis WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        
#----------------------------------------------------------------------------------------------------#
class Editeur:
    def inserer(conn,nom):
        cursor = conn.cursor()
        insertion = "INSERT INTO Editeur VALUES ('%s')" % (nom)
        cursor.execute(insertion)
        
        

    def modifier(conn,colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Editeur SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        
        

    def supprimer(conn,condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Editeur WHERE %s" % (condition)
        cursor.execute(suppression)
        
        


    def afficherTous(conn):
        try:
         cur = conn.cursor()
         sql= "SELECT * FROM Editeur"
         cur.execute(sql)

        except Exception as error:
         print("Une exception s'est produite : ", error)
         print("Type d'exception : ", type(error))

        raw= cur.fetchone()

        while raw:
            print(raw[0])
            raw = cur.fetchone()
        

    def afficherParCondition(conn,condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Editeur WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0])
            rawdata = cursor.fetchone()
        

choix1=int(input("Tapez le numéro correspondant à votre choix: \n 1 : Questions SQL \n 2 : Afficher des données \n 3 : Modifier la BDD\n 4 : Insérer une donnée\n 5 : Supprimer un élément d'une table\n Autre pour quitter \n"))
while choix1>0 and choix1<4:
  if choix1==1:
      choixQ=int(input("Tapez le numéro correspondant à votre choix:\n 1 : Q1\n 2 : Q2\n 3 : Q3\n 4 : Q4\n"))
      if choixQ==1:
        Interrogation.Q1(conn)
      elif choixQ==2:
        Interrogation.Q2(conn)
      elif choixQ==3:
        Interrogation.Q3(conn)
      elif choixQ==4:
        Interrogation.Q4(conn)


  elif choix1==2:
      f="""Afficher :\n1:Utilisateur\n2:Artiste\n3:Chanson\n4:Album\n
      5:Editeurs\n6:Genres musicaux\n7:Historique d'un utilisateur\n
      8:Préférences d'un utilisateur\n9:Playlists d'un utilisateur\n
      10:Amis d'un utilisateur\n11:Droits d'édition d'une chanson ou d'un éditeur\n
      12:Droits artistiques d'une chanson ou d'un artiste"""
      print(f)
      choixA=int(input())
      
      if choixA==1:
          Utilisateur.affichage(Utilisateur, conn)          

      elif choixA==2: 
          Artiste.afficher(Artiste,conn)

      elif choixA==3:
         Chanson.affichage(conn)
      
      elif choixA==4:
         Album.affichage(conn)

      elif choixA==5:
         Editeur.afficherTous(conn)

      elif choixA==6:
         Genre.affichage(Genre, conn)

      elif choixA==7:
         Historique.afficherParCondition(conn,1)

      #elif choixA==8:
      #   Preferences.affichage(conn)

      #elif choixA==9:
      #   Playlist.affichage(conn)

      elif choixA==10:
          Amis.afficherParCondition(conn,1)

      elif choixA==11:
         choix=int(input("Tapez 1 pour connaitre l'éditeur d'une chanson ou 2 pour les chansons d'un éditeur\n"))
         if choix==1:
           id_c=str(input("Donner l'id de la chanson\n"))
           DroitsEdition.afficherdroit(DroitsEdition, conn, id_c)
         elif choix==2:
           nom=str(input("Tapez le nom de l'éditeur\n"))
           DroitsEdition.afficherliste(DroitsEdition,conn,nom)
         else:
           print("Relisez la consigne et recommencez")
            
      elif choixA==12:
         choix=int(input("Tapez 1 pour connaitre l'éditeur d'une chanson ou 2 pour les chansons d'un éditeur\n"))
         if choix==1:
           id_c=str(input("Donner l'id de la chanson\n"))
           DroitsArtistiques.afficherdroit(DroitsArtistiques, conn, id_c)
         elif choix==2:
           id_a=str(input("Tapez le nom de l'éditeur\n"))
           DroitsArtistiques.afficherliste(DroitsArtistiques,conn,id_a)
         else:
           print("Relisez la consigne et recommencez")
            
         
  elif choix1==3:
     f = """Modifier la table : \n1:Utilisateur\n2:Artiste\n3:Chanson\n
     4:Album\n5:Editeur\n6:Genre musical\n7:Historique\n
     8:Préférences\n9:Playlists\n10:Amis\n
     11:DroitsEdition\n12:DroitsArtistiques\n"""
  
     print(f)

     choixA=int(input())

     if choixA==1:
          Utilisateur.modifier(Utilisateur, conn)          

     elif choixA==2: 
          Artiste.modifier(Artiste,conn)

     elif choixA==3:
         Chanson.modifier(conn)
      
     elif choixA==4:
         Album.modifier(conn)

     elif choixA==5:
         Editeur.modifier(conn)

     elif choixA==6:
         Genre.modifier(Genre, conn)

     elif choixA==7:
         Historique.modifier(conn,1)

     #elif choixA==8:
     #   Preferences.modifier(conn)

     #elif choixA==9:
     #   Playlist.modifier(conn)

     elif choixA==10:
         Amis.modifier(conn,1) 

     elif choixA==11:
        0    

     elif choixA==12:
        0


  elif choix1==4:
     f = """Insérer une donnée dans la table : \n1:Utilisateur\n2:Artiste\n3:Chanson\n
     4:Album\n5:Editeur\n6:Genre musical\n7:Historique\n
     8:Préférences\n9:Playlists\n10:Amis\n
     11:DroitsEdition\n12:DroitsArtistiques\n"""

     print(f)

     choixA=int(input()) 

     if choixA==1:
          Utilisateur.ajouter(Utilisateur, conn)          

     elif choixA==2: 
          Artiste.ajouter(Artiste,conn)

     elif choixA==3:
         Chanson.insert(conn)
      
     elif choixA==4:
         Album.insert(conn)

     elif choixA==5:
         Editeur.inserer(conn)

     elif choixA==6:
         Genre.ajouter(Genre, conn)

     elif choixA==7:
         Historique.inserer(conn,1)

     #elif choixA==8:
     #   Preferences.ajouter(conn)

     #elif choixA==9:
     #   Playlist.ajouter(conn)

     elif choixA==10:
         Amis.inserer(conn,1) 

     elif choixA==11:
        0    

     elif choixA==12:
        0


  elif choix1==5:
     f = """Supprimer une donnée de la table : \n1:Utilisateur\n2:Artiste\n3:Chanson\n
     4:Album\n5:Editeur\n6:Genre musical\n7:Historique\n
     8:Préférences\n9:Playlists\n10:Amis\n
     11:DroitsEdition\n12:DroitsArtistiques\n"""

     print(f)

     choixA=int(input())

     if choixA==1:
          Utilisateur.delete(Utilisateur, conn)          

     elif choixA==2: 
          Artiste.supprimer(Artiste,conn)

     elif choixA==3:
         Chanson.delete(conn)
      
     elif choixA==4:
         Album.delete(conn)

     elif choixA==5:
         Editeur.supprimer(conn)

     elif choixA==6:
         Genre.delete(Genre, conn)

     elif choixA==7:
         Historique.supprimer(conn,1)

     #elif choixA==8:
     #   Preferences.delete(conn)

     #elif choixA==9:
     #   Playlist.delete(conn)

     elif choixA==10:
         Amis.supprimer(conn,1) 

     elif choixA==11:
        0

     elif choixA==12:
        0

  choix1=int(input("Tapez le numéro correspondant à votre choix: \n 1 : Questions SQL \n 2 : Afficher des données \n 3 : Modifier la BDD\n 4 : Insérer une donnée\n 5 : Supprimer un élément d'une table\n Autre pour quitter \n"))
  
