
import random
class BankAcct:
    def __init__( self, id, name ):
        self.__id = id
        self.__name = name
        self.__balance = 0
    def service_charge( self ):
        return 0
    def deposit( self, deposit_amount ):
        self.__deposit_amount = deposit_amount
        if self.__deposit_amount  > 0 :
            self.__balance += self.__deposit_amount 
            print( f"Customer {self.__name} deposit {self.__deposit_amount } into account {self.__id} successfully, account balance is {self.__balance}" )
        else :
            print( f"{self.__name}, deposit of {self.__deposit_amount } from account {self.__id} is not successful" )
    def withdraw( self, withdraw_amount ):
        self.__withdraw_amount = withdraw_amount
        if self.__withdraw_amount > 0 and  self.__balance >= self.__withdraw_amount + self.service_charge():
            self.__balance -= self.__withdraw_amount
            print( f"Customer {self.__name} withdraw {self.__withdraw_amount} into account {self.__id} successfully, account balance is {self.__balance}" )
        else:
            print( f"{self.__name}, withdraw of {self.__withdraw_amount} from account {self.__id} is not successful" )

        if self.service_charge() > 0:
            self.__balance -= self.service_charge()
            print( f"Service charge {self.service_charge()} is deducted from account {self.__id}, successfully, account balance is {self.__balance} " )

class SavingAcct( BankAcct ):
    NO_OF_FREE_WITHDRAW  = 2
    AMOUNT_OF_CHARGES = 20
    def __init__( self, name ) :
        super().__init__( "S"+str(random.randint( 100000, 999999)), name )
        self.__no_of_withdraw = 0
    def service_charge( self ):
        if self.__no_of_withdraw > SavingAcct.NO_OF_FREE_WITHDRAW :
            return SavingAcct.AMOUNT_OF_CHARGES
        else:
            return 0
    def withdraw( self, withdraw_amount ):
        self.__no_of_withdraw += 1
        super().withdraw( withdraw_amount = withdraw_amount)
        
class CurrentAcct( BankAcct ):
    NO_OF_CHARGED_CHEQUE = 2
    AMOUNT_OF_CHARGES = 10
    def __init__( self, name ):
        super().__init__( "C" + str(random.randint( 100000, 999999)), name )
        self.__no_of_cheque = 0
    def service_charge( self ):
        if self.__no_of_cheque <= CurrentAcct.NO_OF_CHARGED_CHEQUE :
            return CurrentAcct.AMOUNT_OF_CHARGES
        else: 
            return 0
    def withdraw( self, withdraw_amount ):
        self.__no_of_cheque += 1
        super().withdraw( withdraw_amount = withdraw_amount )

if __name__ == "__main__" :
    list_bankacct = list()
    list_bankacct.append( SavingAcct("Kelvin") )
    list_bankacct.append( CurrentAcct( "Mary" ) )
    list_bankacct[0].deposit(10000)
    list_bankacct[1].deposit(8000)
    list_bankacct[0].withdraw(12000)
    list_bankacct[0].withdraw(7000)
    list_bankacct[0].withdraw(3000)
    list_bankacct[1].withdraw(1000)
    list_bankacct[1].withdraw(2000)
    list_bankacct[1].withdraw(3000)




            


    

