class Album:

    def __init__(self, id, titre, sortie, artiste):
        self.id = id
        self.titre = titre
        self.sortie = sortie
        self.artiste = artiste

    def test_ID(conn, ID) -> bool:
        cur = conn.cursor()
        sql = "SELECT Id FROM Artiste WHERE Id = %s"
        cur.execute(sql, (ID,))
        raw = cur.fetchone()
        cur.close()
        return raw is not None

    def insert(self, conn):
        self.id = input("Id : ")
        while self.test_ID(conn, self.id):
            self.id = input("Id : ")

        self.titre = input("Titre : ")
        self.sortie = input("Sortie (YYYY-MM-DD) : ")
        self.artiste = input("Artiste : ")

        cur = conn.cursor()
        sql = """
        INSERT INTO Album (Id, Titre, Sortie, Artiste) 
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(sql, (self.id, self.titre, self.sortie, self.artiste))
        conn.commit()
        cur.close()

    def modifier(self, conn):
        id = input("Id : ")
        while not self.test_ID(conn, id):
            id = input("Id : ")

        self.titre = input("Titre : ")
        self.sortie = input("Sortie (YYYY-MM-DD) : ")
        self.artiste = input("Artiste : ")

        sql = """
        UPDATE Album 
        SET Titre = %s, Sortie = %s, Artiste = %s 
        WHERE Id = %s
        """
        cur = conn.cursor()
        cur.execute(sql, (self.titre, self.sortie, self.artiste, id))
        conn.commit()
        cur.close()

    def delete(self, conn):
        id = input("Id : ")
        while not self.test_ID(conn, id):
            id = input("Id : ")

        sql = "DELETE FROM Album WHERE Id = %s"
        cur = conn.cursor()
        cur.execute(sql, (id,))
        conn.commit()
        cur.close()
        print(f"Album '{id}' a été supprimé.")

    def affichage(conn):
        sql = "SELECT * FROM Album"
        cur = conn.cursor()
        cur.execute(sql)
        albums = cur.fetchall()
        cur.close()
        
        if albums:
            for album in albums:
                print(f"Id: {album[0]}")
                print(f"Titre: {album[1]}")
                print(f"Sortie: {album[2]}")
                print(f"Artiste: {album[3]}")
                print()
        else:
            print("Aucun album trouvé.")
