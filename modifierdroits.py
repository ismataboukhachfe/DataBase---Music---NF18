#modifier DroitsArtistiques
def modifier(self, conn):
      ID_c=str(input("Entrez l'ID de la chanson :\n"))
      test=Chanson.test_ID(conn, ID)
      while test==False:
         print("ID non trouvé \n")
         ID=str(input("Entrez l'ID de la chanson :\n"))
         test=Chanson.test_ID(conn, ID)

      id_a=str(input("Tapez le nom d'un artiste existant"))
      typenum=int(input("Type : Tapez 1 pour 'auteur' ou 2 pour 'compositeur' ou 3 pour 'collaborateur'"))
      while type<1 or type>3:
               print("Erreur")
               type=int(input("Type : Tapez 1 pour 'auteur' ou 2 pour 'compositeur' ou 3 pour 'collaborateur'"))
      if typenum==1:
         type='auteur'
      elif typenum==2:
         type='compositeur'
      elif typenum==3:
         type='collaborateur'
      try:
         cur=conn.cursor()
         sql =" UPDATE DroitsArtistiques SET id_a='%s', type='%s' WHERE id_c='%s';"%(id_a,type,ID_c)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))


#modifier DroitsEdition

   def modifier(self, conn):
      ID=str(input("Entrez l'ID de la chanson :\n"))
      test=Chanson.test_ID(conn, ID)
      while test==False:
         print("ID non trouvé \n")
         ID=str(input("Entrez l'ID de la chanson :\n"))
         test=Chanson.test_ID(conn, ID)

      nom_e=str(input("Tapez le nom d'un éditeur existant"))
      try:
         cur=conn.cursor()
         sql =" UPDATE DroitsEdition SET nom_e='%s' WHERE id_c='%s';"%(nom_e,ID)
         cur.execute(sql)

      except Exception as error:
        print("Une exception s'est produite : ", error)
        print("Type d'exception : ", type(error))
