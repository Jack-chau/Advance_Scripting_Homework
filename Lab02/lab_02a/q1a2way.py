class Student:
    def __init__( self, id : int, name : str ):
        self.__id = id
        self.__name = name
        self.__score = 0
    
    @property
    def id( self ):
        return self.__id
    @property
    def name( self ):
        return self.__name
    @property
    def score( self ):
        return set_score
    
    @id.setter
    def set_id( self, id ):
        self.__id = id

    @name.setter
    def set_name( self, name ):
        self.__name = name
    
    @name.setter
    def set_score( self, score ):
        self.__score = score
    
    def display_student( self ):
        print( f"Student id={self.__id}, name={self.__name},score={self.__score}" )
    
if __name__ == "__main__":
    std1 = Student( 1, "Chau Ka Ho" )
    std1.display_student()
    std1.set_score = 10
    std1.display_student()
    