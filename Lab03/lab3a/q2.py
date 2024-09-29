class Rectangle:
    __no_of_rectangle : int = 0
    def __init__( self, length : float, width : float ):
        self.__length = length
        self.__width = width
        Rectangle.__no_of_rectangle += 1

    def find_area( self ) -> float:
        area : float = self.__length * self.__width
        return area
    
    def find_perimeter( self ) -> float:
        perimeter : float = self.__length * 2 + self.__width * 2
        return perimeter

    @staticmethod
    def find_number_of_rectangle( ) -> int:
            return Rectangle.__no_of_rectangle

if __name__ == "__main__":
    r1 : Rectangle = Rectangle( 1, 1 )
    r2 : Rectangle = Rectangle( 2, 3 )
    r3 : Rectangle = Rectangle( 1, 3 )
    print( f"r1: area = { r1.find_area( ) }, perimeter = { r1.find_perimeter( ) }" )
    print( f"r1: area = { r2.find_area( ) }, perimeter = { r2.find_perimeter( ) }" )
    print( f"r1: area = { r3.find_area( ) }, perimeter = { r3.find_perimeter( ) }" )
    print( f"Totally there are { Rectangle.find_number_of_rectangle( ) } rectangle(s) created")