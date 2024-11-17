import mysql.connector
class Student :
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__list_module = list()
    def add_module(self, module):
        self.__list_module.append(module)
        def display(self):
        print (f"Student {self.__name} ({self.__id}) "
        f"enrolled the following module(s):")
        for module in self.__list_module:
        print (module)
class Module:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    def __str__(self):
        return f"\t{self.__id} - {self.__name}"
        def __eq__(self, other):
        if self.__id == other.__id:
        return True
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
    def read_student_from_db():
    try :
        mycursor = ConnectDB.mydb.cursor()
        query = f"SELECT * FROM student"
        mycursor.execute(query)
        result_student=mycursor.fetchall()
        list_student = list()
        for row in result_student:
        student = Student(row[0], row[1])
            query = f"SELECT id, name FROM registration, module WHERE registration.module_id
            = module.id AND student_id={row[0]}"
            mycursor.execute(query)
            result_module=mycursor.fetchall()
        list_module = list()
        for row2 in result_module:
            student.add_module(Module(row2[0], row2[1]))
            list_student.append(student)
        return list_student
    except mysql.connector.Error as e:
        print (e)
if __name__=="__main__":
    print("Students in database:")
    list_student = ConnectDB.read_student_from_db()
# display stduent information
    for student in list_student:
        student.display()