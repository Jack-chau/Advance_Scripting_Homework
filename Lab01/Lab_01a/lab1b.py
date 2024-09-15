if __name__ == "__main__":
    import math
    class Circle:
        radius = 0

        def __init__( self ):
            self.radius = 0

        def __init__( self, r ):
            self.radius = r

        def find_area( self ):
            answer = self.radius ** 2 * math.pi
            return answer

    c1 = Circle( 3 )
    c2 = Circle( 4 )
    c3 = Circle( 5 )

    print (f"The total area of three circles is "
           f"{c1.find_area()+c2.find_area()+c3.find_area():.2f}")
