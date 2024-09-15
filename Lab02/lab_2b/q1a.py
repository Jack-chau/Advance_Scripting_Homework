class A:
    def __init__( self, a ):
        self.set_a( a )
    def set_a( self, a ):
        if a > 0:
            self.a = a
    
if __name__ == "__main__":
    a1 = A(1)
    a2 = A(-2)
    a3 = A(3)
    a1 = a2
    a2 = a3
    a1.set_a( 4 )
    a2.a = -1
    a3.set_a( 5 )
    print( f"a1 = {a1.a}")
    print( f"a2 = {a2.a}")
    print( f"a3 = {a3.a}")