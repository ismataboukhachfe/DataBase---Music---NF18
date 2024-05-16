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
     sql="SELECT identifiant FROM Utilisateur WHERE identifiant =%s" % (ID)
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
        self.dateinscription = str(input("Entrer la date d'inscription : "))
        typeu = int(input("Entrer 1 si premium , 0 si non"))
        if typeu == 1 : self.typeu = 'premium'
        if typeu == 0 : self.typeu = 'régulier'
        
        if self.test_ID(conn,self.identifiant) == True : 
            print("Impossible car l'identifiant existe deja, veuillez essayer un autre identifiant")
            return 
        
        sql = "INSERT INTO utilisateur VALUES ('%s', '%s', '%s','%s','%s','%s')" % (self.identifiant, self.nom_utilisateur, self.motdepasse,self.adressemail,self.dateinscription,self.typeu)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        
    def modifier(self,conn):
        
    
        self.identifiant = str(input("Entrer l'identifiant : "))
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))
        self.motdepasse = str(input("Entrer le mot de passe : "))
        self.adressemail = str(input("Entrer l'adressemail: "))
        self.dateinscription = str(input("Entrer la date d'inscription : "))
        typeu = int(input("Entrer 1 si premium , 0 si non"))
        if typeu == 1 : self.typeu = 'premium'
        if typeu == 0 : self.typeu = 'régulier'
        
        if self.test_ID(conn,self.identifiant) == False : 
                print("Impossible car l'identifiant n'existe pas")
                return 
        
    
        sql = """
        UPDATE utilisateur
        SET nom_utilisateur = '%s', motdepasse = '%s', adressemail = '%s', dateinscription = '%s, type = '%s' 
        WHERE identifiant = '%s'  """ % (self.nom_utilisateur, self.motdepasse,self.adressemail,self.dateinscription,self.typeu,self.identifiant) 
       
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()        
    
    
    def delete(self, conn):
        
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))

        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '%s' " % self.nom_utilisateur
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
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
        
        if self.test_nom(conn,self.nom) == True : 
            print("Impossible car le nom existe deja")
            return 
        sql = "INSERT INTO genre VALUES ('%s')" % (self.nom)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        
    def affichage(self, conn):
        if self.test_nom(conn,self.nom) == False : 
            print("Impossible car le nom n'existe pas")
            return 

        sql = "SELECT * FROM genre"
    
        cur = conn.cursor()
        cur.execute(sql)
        genres = cur.fetchall()  # Fetch all rows
        for genre in genres:
            print(genre)
        cur.close()
        
    
    def delete(self, conn):
        if self.test_nom(conn,self.nom) == False : 
            print("Impossible car le nom n'existe pas ")
            return 
        
        self.nom = str(input("Entrer le genre que vous voulez ajouter : "))
        
        sql = "DELETE FROM genre WHERE genre = '%s' " % self.nom
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"Utilisateur '{self.nom}' a été supprimé.")


class Preferences : 
    
    def __init__(self,utilisateur,genre) : 
        self.utilisateur = utilisateur 
        self.genre = genre 
    
    def test_nom(conn, nom,genre)-> int:
         cur=conn.cursor()
         sql="SELECT Id FROM preferences WHERE utilisateur =%s and genre = %s " % (nom,genre)
         cur.execute(sql)

         raw=cur.fetchone()
         if raw:
            return True
         if raw:
            return False   

    
    def ajouter(self,conn) :
        
        if self.test_nom(conn,self.utilisateur,self.genre) == True : 
            print("La relation existe deja")
            return 
        
        self.utilisateur = str(input("Entrer l'identifiant de l'utilisateur : ")) 
        self.genre = str(input("Entrer le genre : "))
        sql = "INSERT INTO utilisateur VALUES ('%s', '%s')" % (self.utilisateur, self.genre)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()

    def delete(self, conn):
        if self.test_nom(conn,self.utilisateur,self.genre) == False : 
            print("La relation n'existe pas")
            return 

        self.utilisateur = str(input("Entrer l'identifiant de l'utilisateur : ")) 
        self.genre = str(input("Entrer le genre : "))
        sql = "DELETE FROM preferences WHERE utilisateur = '%s' and genre = '%s' " % (self.utilisateur,self.genre)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"La relation '{self.utilisateur}' et '{self.genre}'  a été supprimé.")
        
    def affichage(self, conn):
        self.utilisateur = str(input("Entrer l'identifiant de l'utilisateur : ")) 
        if self.test_nom(conn,self.utilisateur,self.genre) == False : 
            print("La relation n'existe pas")
            return 
        sql = "SELECT * FROM preferences where utilisateur = '%s'  " %(self.utilisateur)
    
        cur = conn.cursor()
        cur.execute(sql)
        preferences = cur.fetchall()  # Fetch all rows
        for preference in preferences:
            print(preference[0],preference[1])
            print()
        cur.close()


class Playlist : 
    
    
    def __init__(self,identifiant,titre,description,autorisation,utilisateur) : 
        self.identifiant = identifiant 
        self.titre = titre
        self.description = description
        self.autorisation = autorisation 
        self.utilisateur = utilisateur 
    
    def test_Playlist(conn, playlist)-> int:
        cur=conn.cursor()
        sql="SELECT * FROM playlist WHERE identifiant =%s" % (playlist)
        cur.execute(sql)
        raw=cur.fetchone()
     
        if raw:
            return True
        if raw:
            return False   
        
    def ajouter(self,conn) :

        self.identifiant = str(input("Entrer l'identifiant du playlist : ")) 
        self.titre = str(input("Entrer le titre du playlist : "))
        self.description = str(input("Entrer la description du playlist : "))
        self.autorisation = str(input("Entrer l'autorisation du playlist : ")) 
        self.utilisateur = str(input("Entrer le nom de l'utilisateur createur playlist : "))
        
        if self.test_Playlist(conn,self.identifiant) == True : 
            print("Impossible car l'identifiant existe deja, veuillez essayer un autre identifiant")
            return 
        
        sql = "INSERT INTO utilisateur VALUES ('%s', '%s', '%s','%s','%s')" % (self.identifiant, self.titre, self.description,self.autorisation,self.utilisateur)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        
    def modifier(self,conn):
        
    
        self.identifiant = str(input("Entrer l'identifiant du playlist : ")) 
        self.titre = str(input("Entrer le titre du playlist : "))
        self.description = str(input("Entrer la description du playlist : "))
        self.autorisation = str(input("Entrer l'autorisation du playlist : ")) 
        self.utilisateur = str(input("Entrer le nom de l'utilisateur createur playlist : "))
       
        if self.test_Playlist(conn,self.identifiant) == False : 
            print("le playlist n'existe pas")
            return 

    
        sql =  """
        UPDATE playlist
        SET  titre = '%s',description = '%s', autorisation = '%s', utilisateur = '%s'
        WHERE identifiant = '%s'  """ % (self.titre, self.description,self.autorisation,self.utilisateur,self.identifiant) 
       
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()        

    def delete(self, conn):
        self.identifiant = str(input("Entrer l'identifiant' : "))
        if self.test_Playlist(conn, self.identifiant) == False : 
            print("Le playlist n'existe pas")
            return 

        sql = "DELETE FROM playlist WHERE identifiant = '%s' " % self.identifiant
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"Playlist '{self.identifiant}' a été supprimé.")
        print()

    def affichage(self, conn):
        self.identifiant = str(input("Entrer l'identifiant : "))
        
        sql = "SELECT * FROM playlist WHERE identifiant = '%s'" % self.identifiant
    
        cur = conn.cursor()
        cur.execute(sql)
        user = cur.fetchone()
        cur.close()
        
        if self.test_Playlist(conn,self.identifiant) == False : 
            print("Le playlist n'existe pas")
            return 

        if user:
            print(f"Identifiant: {user[0]}")
            print(f"Titre: {user[1]}")
            print(f"Description : {user[2]}")
            print(f"Autorisation: {user[3]}")
            print(f"Utlisateur: {user[4]}")
        else:
            print(f"Playlist avec l'identifiant '{self.identifiant}' non trouvé.")
            
        
choix1=int(input("Tapez le numéro correspondant à votre choix: \n 1 : Questions SQL \n 2 : Afficher des données \n 3 : Modifier la BDD\n Autre pour quitter \n"))
while choix1>0 and choix1<4:
	if choix1==1:
		choixQ=int(input("Tapez le numéro correspondant à votre choix:\n 1 : Q1\n 2 : Q2\n 3 : Q3\n 4 : Q4\n"))
		