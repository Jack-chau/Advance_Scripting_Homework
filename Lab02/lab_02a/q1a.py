class Student:
    def __init__( self, id : int, name : str ):
        self.__id = id
        self.__name = name
        self.__score = 0

    def set_score( self, score : int ) :
        if score > 0:
            self.__score = score

    def get_score( self ):
        return self.__score
    
    def display_student( self ):
        print( f"Student id={self.__id}, name={self.__name},score={self.__score}" )
    
if __name__ == "__main__":
    std1 = Student( 1, "Chau Ka Ho" )
    std1.display_student()
    std1.set_score( -1 )
    std1.display_student()
    std1.set_score( 10 )
    std1.display_student()
