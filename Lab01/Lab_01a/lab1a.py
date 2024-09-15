class Circle:
    radius = 0
    def find_area( self, r ) :
        self.radius = r
        answer = self.radius ** 2 * 3.1415

        return round( answer, 2 )
a = Circle( )
print( a.find_area(5) )