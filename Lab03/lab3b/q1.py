class Vehicle:
    # Important:
    # All variables except constants should be declared as non-public
    MAX_NUM_WHEELS = 16
    MIN_NUM_WHEELS = 2
    DEFAULT_NUM_WHEELS = 4
    __total_vehicle = 0

    def __init__( self, num_wheels ) :
        Vehicle.__total_vehicle += 1
        if ( num_wheels < Vehicle.MIN_NUM_WHEELS or num_wheels > Vehicle.MAX_NUM_WHEELS ) :
            self.__num_wheels = Vehicle.DEFAULT_NUM_WHEELS
        else :
            self.__num_wheels = num_wheels
        
    def get_num_wheel( self ):
        return self.__num_wheels
    
    @staticmethod
    def get_total_vehicle( ) :
        return Vehicle.__total_vehicle
    
if __name__ == "__main__" :
    my_car = Vehicle( 4 )
    my_truck = Vehicle( Vehicle.MAX_NUM_WHEELS )
    my_bike = Vehicle( Vehicle.MIN_NUM_WHEELS )

    print( f"My car has { my_car.get_num_wheel( ) } wheels" )
    print( f"My truck has { my_truck.get_num_wheel( ) } wheels" )
    print( f"My bike has { my_bike.get_num_wheel( ) } wheels" )
    print( f"There are { Vehicle.get_total_vehicle( ) } vehicle(s)" )
