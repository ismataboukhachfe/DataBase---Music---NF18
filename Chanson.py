class Chanson:
    
    def __init__(self):
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
        if raw:
           return False

    @classmethod
    def insert(self):
    
        id = str(input("Id : "))
        while test_ID(conn,id)
        titre = str(input("Titre : "))
        duree = str(input("Duree : "))
        pays = str(input("Pays : "))
        album = str(input("Album : "))
        genre = str(input("Genre : "))

        
        cur = conn.cursor()
        sql = "INSERT INTO Chanson (Titre, Duree, Pays, Album, Genre) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"
        cur.execute(sql, (self.id, self.duree, self.pays, self.album, self.genre))
        conn.commit()
        
        conn.close()
        

    @classmethod
    def affichage(cls):
        sql = """    
            SELECT * FROM Chanson
        """       
        raw = cur.fetchone()
        while raw:
          print (raw[0], raw[1])
          raw = cur.fetchone()
