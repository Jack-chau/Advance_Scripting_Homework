import mysql.connector


if __name__ == "__main__":
    try:
        mydb = mysql.connector.connect( 
                host = "localhost",
                user = "root",
                password = "Jack0303",
                database = "shapes_db"
        )
        mycursor = mydb.cursor( )
        # query = "CREATE DATABASE IF NOT EXISTS shapes_db"
        # query = """
        #     CREATE TABLE IF NOT EXISTS circle(
        #         id INT NOT NULL AUTO_INCREMENT,
        #         name VARCHAR( 100 ),
        #         radius DOUBLE,
        #         PRIMARY KEY( id )
        #     )
        # """
        query = "SHOW TABLES"
        mycursor.execute( query )
        for line in mycursor:
            print( line )
    except mysql.connector.Error as e:
        print( e )
