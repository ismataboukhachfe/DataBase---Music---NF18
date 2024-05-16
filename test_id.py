def test_ID(conn, ID)-> int:
     cur=conn.cursor()
     sql="SELECT Id FROM Artiste WHERE Id=%s" % (ID)
     cur.execute(sql)

     raw=cur.fetchone()
     if raw:
        return True
     if raw:
        return False
