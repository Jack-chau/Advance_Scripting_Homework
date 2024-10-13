class Worker:
    __number_of_workers = 0
    def __init__( self, name ) :
        self.__name = name 
        Worker.__number_of_workers += 1
    def set_salary( self, salary ) :
        self.__salary = salary
    def get_salary( self ) :
        return self.__salary
    def get_name( self ):
        return self.__name
    @staticmethod
    def get_number_of_workers( ):
        return Worker.__number_of_workers
    
class FTWorker( Worker ) :
    def __init__( self, name, monthly_income ) :
        super( ).__init__( name )
        self.set_monthly_income( monthly_income )
    def set_monthly_income( self, monthly_income ):
        self.monthly_income = monthly_income
        super().set_salary( monthly_income )
    
class PTWorker( Worker ):
    pass

class CommissionWorker( PTWorker ):
    def __init__( self, name, commission, quantity ) :
        super().__init__( name )
        self.__commission = commission
        self.__quantity = quantity
        super().set_salary( self.__commission * self.__quantity )
    def set_commission( self, commission ):
        self.__commission = commission
        super().set_salary( self.__commission * self.__quantity )
    def set_quantity( self, quantity ) :
        self.__quantity = quantity
        super().set_salary( self.__commission * self.__quantity )

class HourlyWorker( PTWorker ):
    def __init__( self, name, wage, hours ):
        super().__init__( name )
        self.__wage = wage
        self.__hours = hours
        super().set_salary( self.__wage * self.__hours )
    def set_wage( self, wage ) :
        self.__wage = wage
        super().set_salary( self.__wage * self.__hours )
    def set_hours( self, hours ):
        self.__hours = hours
        super().set_salary( self.__wage * self.__hours )

if __name__ == "__main__":
    list_worker = list()
    list_worker.append( FTWorker("Kelvin", 15000) )
    list_worker.append( CommissionWorker( "Mary", 1200, 10) )
    list_worker.append( HourlyWorker( "Peter", 80, 160) )

    # a. Print total number of workers
    print( f"There are {Worker.get_number_of_workers()} workers in total")
    # b. Print original salary
    print( "Original salary:" )
    for i in list_worker :
        print( f"{i.get_name()} earned ${i.get_salary()}")
    # c. Set new values to instance variables
    list_worker[0].set_monthly_income( 18000 )
    list_worker[1].set_commission( 1500 )
    list_worker[1].set_quantity(9)
    list_worker[2].set_wage( 90 )
    list_worker[2].set_hours( 180 )
    # d. Print updated salary
    print( "Updated salary:" )
    for i in list_worker :
        print( f"{i.get_name()} earned ${i.get_salary()}")