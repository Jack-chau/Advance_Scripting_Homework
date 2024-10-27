from abc import ABC, abstractmethod
class Worker( ABC ):
    __number_of_workers = 0
    def __init__( self, name : str ):
        Worker.__number_of_workers += 1
        self.__name = name

    @staticmethod
    def get_number_of_workers( ) -> int:
        return Worker.__number_of_workers
    
    def __str__( self ) -> str :
        return f'{self.__name:s} eraned ${self.get_salary()}'
    @abstractmethod
    def set_salary( self ):
        return NotImplemented
    @abstractmethod
    def get_salary( self ):
        return NotImplemented

class FTWorker( Worker ):
    def __init__( self, name, monthly_income:float ):
        super().__init__( name )
        self.set_salary( monthly_income )

    def set_salary( self, monthly_income ):
        self.__monthly_income = monthly_income
    
    def get_salary( self ):
        return self.__monthly_income
    
class PTWorker( Worker ):
    pass

class CommissionWorker( PTWorker ):
    def __init__( self, name, commission, quantity ):
        super().__init__( name )
        self.set_salary( commission, quantity )
    
    def set_salary( self, commission, quantity ):
        self.__commission = commission
        self.__quantity = quantity
    
    def get_salary( self ):
        return self.__commission * self.__quantity

class HourlyWorker( PTWorker ):
    def __init__( self, name, wage, hours ):
        super().__init__( name )
        self.set_salary( wage, hours )

    def set_salary( self, wage, hours ):
        self.__wage = wage
        self.__hours = hours
    
    def get_salary( self ):
        return self.__wage * self.__hours
    

if __name__=="__main__":
    list_worker = list()
    list_worker.append(FTWorker("Kelvin", 15000))
    list_worker.append(CommissionWorker("Mary", 1200, 10))
    list_worker.append(HourlyWorker("Peter", 80, 160))

    print (f"There are {Worker.get_number_of_workers()}"
           f" workers in total")    
    print ("Original salary:")
    for worker in list_worker:
        print(worker) #Do not modify this line

    # Set new values to instance variables
    list_worker[0].set_salary( monthly_income=18000 )
    list_worker[1].set_salary( commission=1500, quantity=9 )
    list_worker[2].set_salary( wage=90, hours=180 )

    print ("Updated salary:")
    for worker in list_worker:
        print(worker) #Do not modify this line
