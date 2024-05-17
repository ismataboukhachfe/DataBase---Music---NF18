#Supprimer DroitsArtistiques

  def supprimer(self,conn):
      id_c=str(input("Entrez l'ID de la chanson :\n"))
      test=Chanson.test_ID(conn, ID)
      while test==False:
         print("ID non trouvé \n")
         id_c=str(input("Entrez l'ID de la chanson :\n"))
         test=Chanson.test_ID(conn, ID)
      id_a=str(input("Tapez l'ID d'un artiste existant"))
      try:
         cur=conn.cursor()
         sql =" DELETE FROM DroitsArtistiques WHERE id_a='%s'AND id_c='%s';"%(id_a,id_c)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))

#Supprimer DroitsEdition

   def supprimer(self,conn):
      ID=str(input("Entrez l'ID de la chanson :\n"))
      test=Chanson.test_ID(conn, ID)
      while test==False:
         print("ID non trouvé \n")
         ID=str(input("Entrez l'ID de la chanson :\n"))
         test=Chanson.test_ID(conn, ID)
      nom_e=str(input("Entrez le nom d'un éditeur existant"))
      try:
         cur=conn.cursor()
         sql =" DELETE FROM DroitsEdition WHERE nom_e='%s'AND id_c='%s';"%(nom_e,ID)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
