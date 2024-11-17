import mysql.connector
if __name__=="__main__":
    try :
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Jack0303"
        )
        mycursor = mydb.cursor()
        query = "CREATE DATABASE IF NOT EXISTS student_module_db"
        mycursor.execute(query)
    except mysql.connector.Error as e:
        print (e)