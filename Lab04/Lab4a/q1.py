import math
class Shape( ):
    __number_of_shapes : int = 0

    def __init__( self, name = "Shape" ) :
        self.__name = name
        Shape.__number_of_shapes += 1

    def find_area( self ) :
        return 0
    
    def find_perimeter( self ) :
        return 0

    def display( self, end = "" ) :
        print( f"This is a {self.__name:s} {end:s}" )
    
    @staticmethod
    def get_number_of_shapes( ) :
        return Shape.__number_of_shapes

class Circle( Shape ) :
    def __init__( self, radius, name = "Circle") :
        super().__init__( name )
        self.__radius = radius
    
    def find_area( self ) :
        area = math.pi * self.__radius * self.__radius
        return area
    
    def find_perimeter( self ) :
        return 2 * math.pi * self.__radius

    def display( self, end = "" ) :
        super().display( f"with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}" )
    
class Rectangle( Shape ):
    def __init__( self, length, width, name = "Rectangle" ) :
        super().__init__( name )
        self.__length = length
        self.__width = width

    def find_area( self ) :
        return self.__length * self.__width
    
    def find_perimeter( self ) :
        return self.__length * 2 + self.__width * 2
    
    def display( self, end="" ):
        super( ).display( f"with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}" )

class RightAngledTriangle( Shape ) :
    def __init__( self, base_lenght, height, name = "Right-angled Triangle" ):
        self.__base_lenght = base_lenght
        self.__height = height
        super( ).__init__( name )

    def find_area( self ) :
        return self.__base_lenght * self.__height / 2

    def find_perimeter( self ):
        perimeter = ( self.__base_lenght + self.__height ) + math.sqrt( self.__base_lenght * self.__base_lenght  + self.__height * self.__height )
        return perimeter 
    
    def display( self, end="" ):
        super().display(f"with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}")

class Cylinder( Circle ) :
    def __init__( self, radius, length, name = "Cylinder" ):
        super().__init__( name, radius )
        self.__length = length

    def find_area( self ) :
        total_surface_area = ( super().find_area( ) * 2 ) + ( 2 * self.__length * super().find_perimeter() )
        return total_surface_area

    def find_perimeter( self ):
        return super().find_perimeter() * self.__length

    def find_volume( self ):
        return super().find_area() * self.__length
    
    def display(self, end="" ) :
        super().display( f", volume = {self.find_volume()}{end:s}" )

#You are NOT allowed to modify following codes
if __name__=="__main__":
    list_shape = list()
    list_shape.append(Shape())
    list_shape.append(Shape("Pentagon"))

    #You may comment out some of the following codes for testing
    list_shape.append(Circle(1))
    list_shape.append(Rectangle(2,2))
    list_shape.append(RightAngledTriangle(3,4))
    list_shape.append(Cylinder(1,3))

    for shape in list_shape:
        shape.display()
    print (f"There are {Shape.get_number_of_shapes()}"
           f" shapes in total")





