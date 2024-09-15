import statistics
class Student:

    def set_id( self, id : int):
        self.__id = id

    def set_name( self, name : str ):
        self.__name = name
    
    def set_score( self, score : float ):
        self.__score = score
    
    def get_score( self ):
        return self.__score

    def display_student( self ):
        print( f"Student id={ self.__id }, name={ self.__name }, score={ self.__score }" )
    
if __name__ == "__main__" :
    stud1, stud2, stud3 = Student(), Student(), Student()
    stud1.set_id( 310567 )
    stud1.set_name( "Cheung Siu Ming" )
    stud1.set_score( 87.1 )
    stud2.set_id( 451267 )
    stud2.set_name( "Ng Wai Man" )
    stud2.set_score( 77.5 )
    stud3.set_id( 789014 )
    stud3.set_name( "Wong Sui Kai" )
    stud3.set_score( 83.4 )
    stud1.display_student()
    stud2.display_student()
    stud3.display_student()
    print( F"Average Score={ statistics.mean( [ stud1.get_score(), stud2.get_score(), stud3.get_score() ]):.2f}" )
