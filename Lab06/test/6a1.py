import mysql.connector
from abc import ABC, abstractmethod
from math import pi

class ConnectDB( ):
    def execute_query( query ) :
        with mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = "Jack0303",
            database = "shapes_db"
        ) as mydb :
            mycursor = mydb.cursor( )
            mycursor.execute( query )
            result = mycursor.fetchall( )
            mydb.commit( )
            return result 
    
    def create_table( ):
        query = """
                    CREATE TABLE IF NOT EXISTS circles( 
                        id int NOT NULL AUTO_INCREMENT,
                        name VARCHAR( 100 ),
                        radius DOUBLE,
                        PRIMARY KEY( id )
                    )
                """
        ConnectDB.execute_query( query )

    def create_circle( circle ):
        query = (
            f"INSERT INTO circles ( name, radius ) VALUES ( '{ circle.get_name()}', {circle.get_radius()} )"
        )
        ConnectDB.execute_query( query )

    def read_shapes( ) :
        query = f"SELECT * FROM circles"
        result = ConnectDB.execute_query( query )
        list_shapes = list( )
        for row in result :
            list_shapes.append( Circle( row[2], "Circle", True) )
        return list_shapes
    
class Shape( ABC ) :
    def __init__( self, name = "Shape" ) :
        self.__name = name
    def get_name( self ) :
        return self.__name
    @abstractmethod
    def find_area( self ) :
        return NotImplemented
    @abstractmethod
    def find_perimeter( self ) :
        return NotImplemented
    def __str__( self ) :
        return f"name={ self.__name }"

class Circle( Shape ) :
    def __init__( self, radius, name="Circle", create_from_db = False ):
        super().__init__( name )
        self.__radius = radius
        if create_from_db == False :
            ConnectDB.create_circle( self )
    def get_radius( self ) :
        return self.__radius
    def find_area( self ) :
        return self.__radius ** 2 * pi
    def find_perimeter( self ) :
        return self.__radius * 2 * pi
    def __str__( self ) :
        return super().__str__() + f" radius = {self.__radius:.1f} area={circle.find_area():.2f} perimeter={circle.find_perimeter():.2f}"
    
if __name__ == "__main__":
    try :
        ConnectDB.create_table()
        while True:
            print( 'Shapes in database:' )
            list_shapes = ConnectDB.read_shapes()
            for circle in list_shapes:
                print( circle )
            radius = float( input( 'Please input radius of Circle:' ) )
            Circle( radius )
    except ValueError as e:
        print( e )

    




