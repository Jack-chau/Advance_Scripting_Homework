import math
from abc import ABC, abstractmethod
class Shape(ABC):
    __number_of_shapes : int = 0
    def __init__( self, name = "Shape" ) :
        self.__name = name
        Shape.__number_of_shapes += 1

    @abstractmethod
    def find_area( self ) -> float:
        return NotImplemented

    @abstractmethod
    def find_perimeter( self ) -> float:
        return NotImplemented

    @staticmethod
    @abstractmethod
    def get_number_of_shapes() -> int:
        return NotImplemented
        
    def display( self, end=""):
        print( f'This is a {self.__name:s}{end:s}')
        
class Circle( Shape ):
    __number_of_circle = 0 
    def __init__( self, radius : float, name="Circle"):
        super().__init__( name )
        self.__radius = radius
        Circle.__number_of_circle += 1

    def find_area( self ) -> float:
        return math.pi * self.__radius * self.__radius
    
    def find_perimeter( self ) -> float:
        return self.__radius * 2 * math.pi

    def get_number_of_shapes( ):
        return Circle.__number_of_circle
    
    def display( self, end='' ):
        super().display( f' with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}')

class Rectangle( Shape ):
    __number_of_rectangle = 0
    def __init__( self, length : float, width :float, name="Rectangle"):
        super().__init__(name)
        self.__length = length
        self.__width = width
        Rectangle.__number_of_rectangle += 1

    def find_area( self ) :
        return self.__length * self.__width
    
    def find_perimeter( self ):
        return self.__length * 2 + self.__width * 2
    
    def get_number_of_shapes( ):
        return Rectangle.__number_of_rectangle
    
    def display( self, end='' ):
        super().display( f' with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}' )
    
class RightAngledTriangle( Shape ):
    __number_of_triangle = 0
    def __init__( self, base_length : float, height : float, name="Right-angled Triangle" ) :
        super().__init__( name )
        self.__base_length = base_length
        self.__height = height
        RightAngledTriangle.__number_of_triangle += 1
    
    def find_area( self ):
        return ( self.__base_length * self.__height ) /2 
    
    def find_perimeter( self ) :
        return (self.__base_length + self.__height ) + ( self.__base_length ** 2 + self.__height ** 2 )**0.5
    def get_number_of_shapes():
        return RightAngledTriangle.__number_of_triangle
    
    def display( self, end=''):
        super().display( f' with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}' )

class Cylinder( Circle ):
    __number_of_cylinder = 0
    def __init__( self, radius : float, length : float, name="Cylinder" ):
        super().__init__( radius, name )
        self.__length = length
        Cylinder.__number_of_cylinder += 1

    def find_area( self ):
        return super().find_area() * 2 + super().find_perimeter() * self.__length

    def find_perimeter( self ):
        return super().find_perimeter() * self.__length

    def find_volume( self):
        return super().find_area() * self.__length

    def get_number_of_shapes( ):
        return Cylinder.__number_of_cylinder
    
    def display( self, end=''):
        super().display( f'volume = {self.find_volume():.2f}{end:s}' )
            
#You are NOT allowed to modify following codes
if __name__=="__main__":
    list_shape = list()
    # Shape objects can no longer be created anymore
    # list_shape.append(Shape())
    # list_shape.append(Shape("Pentagon"))
    list_shape.append(Circle(1))
    list_shape.append(Rectangle(2,2))
    list_shape.append(RightAngledTriangle(3,4))
    list_shape.append(Cylinder(1,3))
    for shape in list_shape:
        shape.display()
    print (f"There are {Circle.get_number_of_shapes()}"
           f" circle(s) in total")
    print (f"There are {Rectangle.get_number_of_shapes()}"
           f" rectangle(s) in total")
    print (f"There are {RightAngledTriangle.get_number_of_shapes()}"
           f" right-angled triangle(s) in total")
    print (f"There are {Cylinder.get_number_of_shapes()}"
           f" cylinder(s) in total")



