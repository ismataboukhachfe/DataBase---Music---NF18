import psycopg2

HOST ="tuxa.sme.utc"
USER = "nf18p032"
PASSWORD = "Fb9EyCL7x6mZ"
DATABASE = "dbnf18p032"

try :
	conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
	print("Connexion réussie \n")

except Exception as error:
	print("Une exception s'est produite : ", error)
	print("Type d'exception : ", type(error))


class Utilisateur : 
    
    def __init__(self, identifiant=None, nom_utilisateur=None, motdepasse=None, adressemail=None, dateinscription=None, typeu=None, preferences=None):
        self.identifiant = identifiant
        self.nom_utilisateur = nom_utilisateur
        self.motdepasse = motdepasse
        self.adressemail = adressemail
        self.dateinscription = dateinscription
        self.typeu = typeu
        self.preferences = preferences  # Ajout de l'attribut preferences
        
    def test_ID(conn, ID)-> bool:
      try:
          cur=conn.cursor()
          sql="SELECT id FROM Utilisateur WHERE id ='%s';" % (ID)
          cur.execute(sql)
      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
      raw=cur.fetchone()
      if raw:
        return True
      else:
        return False

    def modifier(self, conn):
        try:
            # Vérifier si l'identifiant existe déjà
            while self.test_ID(conn, self.identifiant):
                print("Impossible car l'identifiant existe déjà, veuillez essayer un autre identifiant")
                self.identifiant = str(input("Entrer l'identifiant : "))

            # Demander les informations à l'utilisateur
            self.nom_utilisateur = str(input("Entrer le nom_utilisateur : "))
            self.motdepasse = str(input("Entrer le mot de passe : "))
            self.adressemail = str(input("Entrer l'adresse mail: "))
            self.dateinscription = str(input("Entrer la date d'inscription (YYYY-MM-DD) : "))
            typeu = int(input("Entrer 1 pour premium, 0 pour régulier : "))
            self.typeu = 'premium' if typeu == 1 else 'régulier'
            
            self.preferences = str(input("Entrer les préférences (au format JSON) : "))  # Demander les préférences à l'utilisateur

            # Construction de la requête SQL sécurisée avec psycopg2
            sql = """
            UPDATE Utilisateur
            SET nom_utilisateur = %s, mot_de_passe = %s, email = %s, inscription = %s, type = %s, preferences = %s
            WHERE id = %s
            """

            # Exécution de la requête préparée
            cur = conn.cursor()
            cur.execute(sql, (self.nom_utilisateur, self.motdepasse, self.adressemail, self.dateinscription, self.typeu, self.preferences, self.identifiant))
            conn.commit()
            print(f"Utilisateur avec id {self.identifiant} mis à jour avec succès.")
        except Exception as error:
            print("Une exception s'est produite : ", error)
            print("Type d'exception : ", type(error))
        finally:
            cur.close()


