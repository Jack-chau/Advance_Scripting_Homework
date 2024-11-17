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
    def insert_students(students):
        mycursor = ConnectDB.mydb.cursor()
        query = "INSERT INTO student (id, name) VALUES (%s, %s)"
        mycursor.executemany(query, students)
        ConnectDB.mydb.commit()
    def insert_modules(modules):
        mycursor = ConnectDB.mydb.cursor()
        query = "INSERT INTO module (id, name) VALUES (%s, %s)"
        mycursor.executemany(query, modules)
        ConnectDB.mydb.commit()
    def insert_registrations(registrations):
        mycursor = ConnectDB.mydb.cursor()
        query = "INSERT INTO registration (student_id, module_id) VALUES (%s, %s)"
        mycursor.executemany(query, registrations)
        ConnectDB.mydb.commit()
if __name__=="__main__":
# You are NOT allowed to modify the following codes
    students = (("201234567","Kelvin"), ("202345678", "Peter"))
    modules = (("ITE3102", "Network Fundamentals"),
                ("ITP3915", "Programming Fundamentals"),
                ("ITP4456", "Database Applications"),
                ("ITP4451", "IoT Fundamentals"),
                ("ITP4457", "Web Technologies"),
                ("ITP4458", "Wireless Technologies"),
                ("ITP4459", "Advanced Scripting Technology"),
                ("ITP4410", "Internet Programming"),
                ("ITP4413", "Server Administration"))
    registrations = (("201234567", "ITE3102"),
                ("201234567", "ITP3915"),
                ("201234567", "ITP4456"),
                ("201234567", "ITP4451"),
                ("201234567", "ITP4457"),
                ("201234567", "ITP4458"),
                ("201234567", "ITP4459"),
                ("202345678", "ITE3102"),
                ("202345678", "ITP3915"),
                ("202345678", "ITP4456"),
                ("202345678", "ITP4459"),
                ("202345678", "ITP4410"),
                ("202345678", "ITP4413"))
    ConnectDB.insert_students(students)
    ConnectDB.insert_modules(modules)