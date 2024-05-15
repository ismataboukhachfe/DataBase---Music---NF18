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
#----------------------------------------------------------------------------------------------------#
class ContientChanson:
    @classmethod
    def inserer(idPlaylist, idChanson):
        cursor = conn.cursor()
        insertion = "INSERT INTO ContientChanson VALUES ('%s', '%s')" % (idPlaylist, idChanson)
        cursor.execute(insertion)
        connection.commit()
        connection.close()

    @classmethod
    def modifier(colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE ContientChanson SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        connection.commit()
        connection.close()

    @classmethod
    def supprimer(condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM ContientChanson WHERE %s" % (condition)
        cursor.execute(suppression)
        connection.commit()
        connection.close()

    @classmethod
    def afficherTous():
        cursor = conn.cursor()
        affichage = "SELECT * FROM ContientChanson"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        connection.close()
	    
    @classmethod
    def afficherParCondition(condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM ContientChanson WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        connection.close()
#----------------------------------------------------------------------------------------------------#
class Historique:
    @classmethod
    def inserer(chanson, utilisateur, compteur):
        cursor = conn.cursor()
        insertion = "INSERT INTO Historique VALUES ('%s', '%s', '%s')" % (chanson, utilisateur, compteur)
        cursor.execute(insertion)
        connection.commit()
        connection.close()

    @classmethod
    def modifier(colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Historique SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        connection.commit()
        connection.close()

    @classmethod
    def supprimer(condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Historique WHERE %s" % (condition)
        cursor.execute(suppression)
        connection.commit()
        connection.close()

    @classmethod
    def afficherTous():
        cursor = conn.cursor()
        affichage = "SELECT * FROM Historique"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1], rawdata[2])
            rawdata = cursor.fetchone()
        connection.close()

    @classmethod
    def afficherParCondition(condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Historique WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1], rawdata[2])
            rawdata = cursor.fetchone()
        connection.close()
#----------------------------------------------------------------------------------------------------#
class Amis:
    @classmethod
    def inserer(utilisateur1, utilisateur2):
        cursor = conn.cursor()
        insertion = "INSERT INTO Amis VALUES ('%s', '%s')" % (utilisateur1, utilisateur2)
        cursor.execute(insertion)
        connection.commit()
        connection.close()

    @classmethod
    def modifier(colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Amis SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        connection.commit()
        connection.close()

    @classmethod
    def supprimer(condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Amis WHERE %s" % (condition)
        cursor.execute(suppression)
        connection.commit()
        connection.close()

    @classmethod
    def afficherTous():
        cursor = conn.cursor()
        affichage = "SELECT * FROM Amis"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        connection.close()

    @classmethod
    def afficherParCondition(condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Amis WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0], rawdata[1])
            rawdata = cursor.fetchone()
        connection.close()
#----------------------------------------------------------------------------------------------------#
class Editeur:
    @classmethod
    def inserer(nom):
        cursor = conn.cursor()
        insertion = "INSERT INTO Editeur VALUES ('%s')" % (nom)
        cursor.execute(insertion)
        connection.commit()
        connection.close()

    @classmethod
    def modifier(colonne, valeur, condition):
        cursor = conn.cursor()
        modification = "UPDATE Editeur SET %s = %s WHERE %s" % (colonne, valeur, condition)
        cursor.execute(modification)
        connection.commit()
        connection.close()

    @classmethod
    def supprimer(condition):
        cursor = conn.cursor()
        suppression = "DELETE FROM Editeur WHERE %s" % (condition)
        cursor.execute(suppression)
        connection.commit()
        connection.close()

    @classmethod
    def afficherTous():
        cursor = conn.cursor()
        affichage = "SELECT * FROM Editeur"
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0])
            rawdata = cursor.fetchone()
        connection.close()

    @classmethod
    def afficherParCondition(condition):
        cursor = conn.cursor()
        affichage = "SELECT * FROM Editeur WHERE %s" % (condition)
        cursor.execute(affichage)
        rawdata = cursor.fetchone()
        while rawdata:
            print(rawdata[0])
            rawdata = cursor.fetchone()
        connection.close()
#----------------------------------------------------------------------------------------------------#
