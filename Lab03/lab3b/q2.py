class Employee( ) :
    # static variable
    __number_of_employee = 0
    __total_salary_expense = 0

    def __init__( self, name, salary ) :
        self.__name = name
        self.__salary = salary
        Employee.__number_of_employee += 1
        Employee.__total_salary_expense += salary

    def set_salary( self, salary ):
        if salary > 0 :
            Employee.__total_salary_expense -= self.__salary
            self.__salary = salary
            Employee.__total_salary_expense += self.__salary

    def raise_salary( self, percentage ):
        self.set_salary( self.__salary * ( 1 + percentage/100 ) )

    def display( self ):
        print( f"Employee name = { self.__name }, salary = { self.__salary:.0f}" )

    @staticmethod
    def get_average_salary( ) :
        return round( Employee.__total_salary_expense / Employee.__number_of_employee, 0 )

if __name__ == "__main__":
    # 1 Create a list named emp_list to hold all
    #   employee objects
    emp_list = list( )
    # 2 - 4 Create employee object with name and salary
    #       Add it to the list you created in step 1
    emp_list.append( Employee( name = "Chan Tai Man", salary = 12000 ) )
    emp_list.append( Employee( name = "Tam Ping Shing", salary = 13500 ) )
    emp_list.append( Employee( name = "Leung Pig Hung", salary = 15000 ) )
    print( "Before:" )
    # 5 Use looping and call display method to print
    #   employee information
    for i in emp_list :
        i.display( )
    print( f"Average salary is {Employee.get_average_salary( )}" )
    print( "After: ")
    emp_list[0].raise_salary( 10 )
    emp_list[1].raise_salary( 5 )
    emp_list[2].set_salary( 9000 )
    for i in emp_list :
        i.display( ) 
    print( f"Average salary is {Employee.get_average_salary( )}" )