import mysql.connector
class ConnectDB:
    try :
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jack0303",
        database="student_module_db"
        )
    except mysql.connector.Error as e:
        print (e)
    def create_table():
        try :
            # Complete the following codes
            # to create 3 tables
            mycursor = ConnectDB.mydb.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS student (
            id VARCHAR(9) NOT NULL,
            name VARCHAR(100),
            PRIMARY KEY (id)
            )"""
            mycursor.execute(query)
            query = """
            CREATE TABLE IF NOT EXISTS module (
            id VARCHAR(7) NOT NULL,
            name VARCHAR(100),
            PRIMARY KEY (id)
            )"""
            mycursor.execute(query)
            query = """
            CREATE TABLE IF NOT EXISTS registration (
            student_id VARCHAR(9),
            module_id VARCHAR(7),
            PRIMARY KEY (student_id, module_id),
            FOREIGN KEY (student_id) REFERENCES student(id),
            FOREIGN KEY (module_id) REFERENCES module(id)
            )"""
            mycursor.execute(query)
            ConnectDB.mydb.commit()
        except mysql.connector.Error as e:
            print (e)
if __name__=="__main__":
    ConnectDB.create_table()