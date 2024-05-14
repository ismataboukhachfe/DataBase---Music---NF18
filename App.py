#Fichier pour  creer l'application python de manipulation de donnees 


class Utilisateur : 
    
    def __init__(self,identifiant,nom_utilisateur, motdepasse,adressemail,dateinscription ):
       
        self.identifiant = identifiant 
        self.nom_utilisateur = nom_utilisateur 
        self.motdepasse = motdepasse
        self.adressemail = adressemail 
        self.dateinscription = dateinscription 
        
        
    def ajouter(self,conn) :
        
        self.identifiant = str(input("Entrer l'identifiant : "))
        self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))
        self.motdepasse = str(input("Entrer le mot de passe : "))
        self.adressemail = str(input("Entrer l'adressemail: "))
        self.dateinscription = str(input("Entrer la date d'inscription : "))
        
        sql = "INSERT INTO utilisateur VALUES ('%s', '%s', '%s','%s','%s')" % (identifiant, nom_utilisateur, motdepasse,adressemail,dateinscription)
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        
def modifier(self,conn,identifiant, nom_utilisateur, motdepasse, adressemail, dateinscription):
    
        self.identifiant = identifiant 
        self.nom_utilisateur = nom_utilisateur 
        self.motdepasse = motdepasse
        self.adressemail = adressemail 
        self.dateinscription = dateinscription 
    
    
        sql = """
        UPDATE utilisateur
        SET nom_utilisateur = '%s', motdepasse = '%s', adressemail = '%s', dateinscription = '%s'
        WHERE identifiant = '%s'% (nom_utilisateur, motdepasse,adressemail,dateinscription,identifiant) 
        """
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()        
        
    def delete(self, conn, nom):
        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '/s " % nom
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"Utilisateur '{nom}' a été supprimé.")
        
    def affichage(self,conn,nom) : 
        sql = "SELECT * FROM utilisateur WHERE nom_utilisateur = '%s'" % nom
    
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
        else:
            print(f"Utilisateur avec le nom '{nom}' non trouvé.")














    