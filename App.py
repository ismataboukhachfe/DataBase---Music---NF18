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

  def test_groupe(conn, nom_g):
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
       print("Type d'exception : ", type(error))
       return True

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
        test_g, id_g=self.test_groupe(conn, nom_g)
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
    try:
       cur = conn.cursor()
       sql= "SELECT nom,biographie,origine FROM Artiste WHERE id=%s;" %(ID)
       cur.execute(sql)

    except Exception as error:
       print("Une exception s'est produite : ", error)
       print("Type d'exception : ", type(error))

    raw= cur.fetchone()
    while raw:
      print("Nom : %s", raw[0])
      print("Biographie : %s", raw[1])
      print("Origine : %s", raw[2])
      raw=cur.fetchone()

    

  

