class Calaulator:
    def __init__( self, name : str, version : int ) -> None:
        self.name = name
        self.version = version
    
    def get_calculator_info( self ) -> str:
        return f"{ self.name } V.{ self.version }"
    
    @staticmethod
    def add_all( self, *numbers : int ) -> int:
        return sum( numbers )
    
calc : Calaulator = Calaulator( name="Jack Calaulator", version=1)
print( calc.get_calculator_info())
print( calc.add_all(1,2,3,4,5))
print( Calaulator.add_all( 1,2,3) )