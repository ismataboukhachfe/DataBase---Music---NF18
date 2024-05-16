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
        conn.commit()
        conn.close()
        
    def modifier(self,conn):
    
        id = str(input("Id : "))
        while not(self.test_ID(conn,id)):
            id = str(input("Id : "))

        self.titre = str(input("Titre : "))
        self.duree = str(input("Duree : "))
        self.pays = str(input("Pays : "))
        self.album = str(input("Album : "))
        self.genre = str(input("Genre : "))

    
        sql = "UPDATE Chanson SET Titre = '%s', Duree = '%s', Pays = '%s', Album = '%s', Genre ='%s' WHERE id = '%s' " % (self.titre, self.duree, self.pays, self.album, self.genre, selfid) 
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()   
        
    def delete(self, conn):
        
        id = str(input("Id : "))
        while not(self.test_ID(conn,id)):
            id = str(input("Id : "))
        sql = "DELETE FROM utilisateur WHERE nom_utilisateur = '%s' " %id
        
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        print(f"Utilisateur '{id}' a été supprimé.")

    def affichage(cls):
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
        
