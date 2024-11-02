import mysql.connector
if __name__=="__main__":
    try :
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password = "",
        database="shapes_db"
        )
        mycursor = mydb.cursor()
        query = "SELECT * FROM circles"
        mycursor.execute(query)
        result=mycursor.fetchall()
        for row in result:
            print (row)
    except mysql.connector.Error as e:
        print (e)