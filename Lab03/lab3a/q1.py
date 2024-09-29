class Test:
    test = 10

    def reset_test( self ) :
        self.test = 0
    def add_one( self ):
        self.test += 1

if __name__ == "__main__":
    c1 = Test( )
    c1.add_one( )
    print( f"c1.test = { c1.test }" ) # 11
    print( f"Test.test = { Test.test }" ) # 10
    c1.reset_test( )
    c1.add_one( )
    print( f"c1.test = { c1.test }") #1
    print( f'Test.test = { Test.test }') #10

