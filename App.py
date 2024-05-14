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

  def test_groupe(conn, ID)-> bool:
    cur=conn.cursor()
    sql= "SELECT Id_G from Groupe WHERE Id_G=%s" % (ID)
    cur.execute(sql)

    raw = cur.fetchone()

    if raw:
      return True
    else:
      return False

  def test_ID(conn, ID)-> int:
     cur=conn.cursor()
     sql="SELECT Id FROM Artiste WHERE Id=%s" % (ID)
     cur.execute(sql)

     raw=cur.fetchone()
     if raw:
        return True
     else:
        return False


  def insert(self,conn):
    id=str(input("Entrez le numéro d'ID"))
    while testID:
         id=str(input("ID déjà pris, tapez un ID différent"))
         testID=self.test_id(conn,id)
    type=int(input("Tapez 1 s'il s'agit d'un artiste solo, 2 s'il s'agit d'un groupe ou 3 si c'est un artiste solo lié à un groupe"))

    if type==1:
      testID=self.test_id(conn,id)
      nom=str(input("Entrez le nom de l'artiste à ajouter:\n"))
      biographie=str(input("Entrez la biographie de l'artiste"))

    elif type==2:
      nom=str(input("Entrez le nom du groupe à ajouter:\n"))
      biographie=str(input("Entrez la biographie du groupe"))
    else:
      print("Erreur, tapez 1 pour solo ou 2 pour groupe")

    origine=str(input("Entrez son origine : \n"))

    sql = "INSERT INTO Artiste VALUES (%d, %s, %s, %s)" % (id, nom, biographie, origine)

    return

  def afficher(self, conn, ID):
    cur = conn.cursor()
    sql= "SELECT nom,biographie,origine FROM Artiste WHERE id=%s" %(ID)
    cur.execute(sql)

    raw= cur.fetchone()
    while raw:
      print("Nom : %s", raw[0])
      print("Biographie : %s", raw[1])
      print("Origine : %s", raw[2])
      raw=cur.fetchone()

    

  

