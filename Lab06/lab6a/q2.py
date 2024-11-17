import mysql.connector
from abc import ABC, abstractmethod
from math import pi
class ConnectDB:
    def execute_query(query):
        with mysql.connector.connect(
            host="localhost",
            user="root",
            password="Jack0303",
            database="shapes_db"
        ) as mydb:
            mycursor = mydb.cursor()
            mycursor.execute(query)
            result = mycursor.fetchall()
            mydb.commit()
        return result
    def create_table():
        query = """
            CREATE TABLE IF NOT EXISTS circles (
            id int NOT NULL AUTO_INCREMENT,
            name VARCHAR(100),
            radius DOUBLE,
            PRIMARY KEY (id)
        )"""
        ConnectDB.execute_query(query)
        query = """
            CREATE TABLE IF NOT EXISTS rectangles (
            id int NOT NULL AUTO_INCREMENT,
            name VARCHAR(100),
            length DOUBLE,
            width DOUBLE,
            PRIMARY KEY (id)
        )"""
        ConnectDB.execute_query(query)

    def create_circle(circle):
        query = (f"INSERT INTO circles (name, radius) "
        f"VALUES ('{circle.get_name()}', {circle.get_radius()})")
        ConnectDB.execute_query(query)

    def create_rectangle(rectangle):
        query = (f"INSERT INTO rectangles (name, length, width) " 
        f"VALUES ('{rectangle.get_name()}', {rectangle.get_length()},
        {rectangle.get_width()})")
        ConnectDB.execute_query(query)
        
def read_shapes():
    query = f"SELECT * FROM circles"
    result=ConnectDB.execute_query(query)
    list_shapes = list()
    for row in result:
        list_shapes.append(Circle(row[2], "Circle", True))
    query = f"SELECT * FROM rectangles"
    result=ConnectDB.execute_query(query)
    for row in result:
        list_shapes.append(Rectangle(row[2], row[3], "Rectangle", True))
    return list_shapes
class Shape(ABC):
    def __init__(self, name="Shape"):
        self.__name = name
    def get_name(self):
        return self.__name
    @abstractmethod
    def find_area(self):
        return NotImplemented
    @abstractmethod
    def find_perimeter(self):
        return NotImplemented
    def __str__(self):
        return f"name={self.__name}"
class Circle(Shape):
    def __init__(self, radius, name="Circle", create_from_db=False):
        super().__init__(name)
        self.__radius = radius
        if create_from_db == False:
        ConnectDB.create_circle(self)
    def get_radius(self):
        return self.__radius
    def find_area(self):
        return self.__radius ** 2 * pi
    def find_perimeter(self):
        return self.__radius * 2 * pi
    def __str__(self):
        return super().__str__() + f" radius={self.__radius:.1f} area={self.find_area():.2f}
    perimeter={self.find_perimeter():.2f}"
class Rectangle(Shape):
    def __init__(self, length, width, name="Rectangle", create_from_db=False):
        super().__init__(name)
        self.__length = length
        self.__width = width
        if create_from_db == False:
            ConnectDB.create_rectangle(self)
    def get_length(self):
        return self.__length
    def get_width(self):
        return self.__width
    def find_area(self):
        return self.__length * self.__width
    def find_perimeter(self):
        return (self.__length + self.__width) * 2
    def __str__(self):
        return super().__str__() + f" length={self.__length:.1f} width={self.__width:.1f}
        area={self.find_area():.2f} perimeter={self.find_perimeter():.2f}"
if __name__=="__main__":
    try :
        ConnectDB.create_table()
        while True:
            print("Shapes in database:")
            list_shapes = ConnectDB.read_shapes()
            for shape in list_shapes:
                print (shape)
                print ("Input 'c' - Create a Circle")
                print ("Input 'r' - Create a Rectangle")
                user_input = input()
            if user_input == "c":
                radius = float(input("Please input radius of Circle:"))
                Circle(radius)
            if user_input == "r":
                length = float(input("Please input length of Rectangle:"))
                width = float(input("Please input width of Rectangle:"))
                Rectangle(length, width)
    except ValueError as e:
    print (e)