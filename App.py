#Fichier pour  creer l'application python de manipulation de donnees 

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
        self.dateinscription = str(input("Entrer la date d'inscription : "))
        typeu = int(input("Entrer 1 si premium , 0 si non"))
        if typeu == 1 : self.typeu = 'premium'
        if typeu == 0 : self.typeu = 'régulier'
        
        if self.test_ID(self.identifiant) == True : 
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

        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '/s " % self.nom_utilisateur
        
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
        
        if self.test_nom(self.nom) == True : 
            print("Impossible car le nom existe deja")
            return 
        sql = "INSERT INTO genre VALUES ('%s')" % (self.nom)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        
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
        conn.commit()
        cur.close()
        print(f"Utilisateur '{self.nom}' a été supprimé.")

        

    
    
    
    












    