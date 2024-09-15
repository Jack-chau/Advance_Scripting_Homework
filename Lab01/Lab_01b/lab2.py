class Employee:
    def set_name( self, name : str ):
        self.__name = name
    
    def set_salary( self, salary : float ):
        self.__salary = salary
    
    def raise_salary( self, percentage : float ):
        self.__salary = self.__salary * percentage / 100 + self.__salary
        return self.__salary
    
    def display( self ):
        print( f"Employee name={self.__name}, salary={self.__salary:.0f}" )

if __name__ == "__main__":
    emp1, emp2 = Employee(), Employee()

    emp1.set_name("Chen Tai Man")
    emp1.set_salary(12000)

    emp2.set_name("Tam Ping Shing")
    emp2.set_salary(13500)
    print( "Before:" )
    emp1.display( )
    emp2.display( )
    print( "After:")
    emp1.raise_salary( 10.0 )
    emp2.raise_salary( 5.0 )
    emp1.display( )
    emp2.display( )

    

