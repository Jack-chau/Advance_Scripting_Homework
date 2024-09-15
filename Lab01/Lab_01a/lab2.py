class Student:
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_age( self, age ):
        self.__age = age

    def get_age( self ):
        if self.__age < 18 or not isinstance( self.__age, int ) :
            print( f'Invalid age {self.__age}, reset to 18' )
            self.__age = 18
            return self.__age
        else:
            return self.__age

if __name__=="__main__":
    stud1 = Student()
    stud1.set_name("Chan Tai Man")
    stud1.set_age( 19 )
    print (f"Student: name={stud1.get_name()}, age={stud1.get_age()}")

    stud2 = Student()
    stud2.set_name("Ng Hing")
    stud2.set_age( -23 )
    print (f"Student: name={stud2.get_name()}, age={stud2.get_age()}")
