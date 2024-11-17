from abc import ABC, abstractmethod
import random

class BankAcct( ABC ):
    def __init__( self, id : str, name : str ):
        self.__id = id
        self.__name = name
        self.__transaction_list = list()

    @abstractmethod
    def service_charge( self ):
        return NotImplemented
    
    def get_balance( self ):
        if len( self.__transaction_list ) > 0:
            return self.__transaction_list[-1].get_balance()
        else :
            return 0
        
    def deposit( self, amount ):
        if amount > 0 :
            self.__transaction_list.append( Transaction( Transaction.TYPE['DEPOSIT'],amount,self.get_balance( ) ) )
        else :
            print( f"{self.name}, deposit of {amount} is not successful" )
    
    def withdraw( self, amount ):
        if amount > 0 and self.get_balance() >= ( amount + self.service_charge() ) :
            self.__transaction_list.append( Transaction( Transaction.TYPE["WITHDRAW"], amount, self.get_balance( ) ) ) 
        else :
            print( f"Customer {self.__name} withdraw {amount} from account {self.__id} is not successful" )

        if self.service_charge() > 0:
            self.__transaction_list.append( Transaction( Transaction.TYPE["SERVICE"], self.service_charge(), self.get_balance( ) ) )
    
    def display_transaction_history( self ):
        print( f"Transaction History of Customer {self.__name} with Account {self.__id}")
        print( f"   {'Transaction Type':<17}|{'Amount':>7}|{'Balance':>8}")
        balance = 0
        for i in self.__transaction_list:
            print( f"   {i.get_type():<17}|{i.get_amount():>7}|{i.get_balance():>8}")
    
class SavingAcct( BankAcct ):
    NO_OF_FREE_WITHDRAW = 2
    AMOUNT_OF_CHARGES = 20

    def __init__( self, name ):
        super().__init__("S" + str( random.randint( 100000, 999999)), name )
        self.__no_of_withdraw = 0

    def service_charge( self ):
        if self.__no_of_withdraw > SavingAcct.NO_OF_FREE_WITHDRAW:
            return SavingAcct.AMOUNT_OF_CHARGES
        else :
            return 0
    def withdraw( self, amount ):
        self.__no_of_withdraw += 1
        super().withdraw( amount )


class CurrentAcct( BankAcct ):
    NO_OF_CHARGED_CHEQUE = 2
    AMOUNT_OF_CHARGES = 10
    def __init__( self, name ):
        super().__init__( "C"+str(random.randint(100000, 999999)), name )
        self.__no_of_cheque = 0


    def service_charge( self ):
        if self.__no_of_cheque <= CurrentAcct.NO_OF_CHARGED_CHEQUE:
            return CurrentAcct.AMOUNT_OF_CHARGES
        else :
            return 0

    def withdraw( self, amount ):
        self.__no_of_cheque += 1
        super().withdraw( amount )

class Transaction :
    TYPE = {"DEPOSIT":"deposit", "WITHDRAW":"withdraw", "SERVICE":"service charge"}
    def __init__( self, type, amount, previous_balance ):
        self.__type = type
        self.__amount = amount
        if type == Transaction.TYPE["DEPOSIT"]:
            self.__balance = previous_balance + amount
        else:
            self.__balance = previous_balance - amount
        
    def get_type( self ):
        return self.__type
    def get_amount( self ):
        return self.__amount
    def get_balance( self ):
        return self.__balance


if __name__ == "__main__":
    list_bankacct = list()
    list_bankacct.append(SavingAcct("Kelvin"))
    list_bankacct.append(CurrentAcct("Mary"))
    list_bankacct[0].deposit(10000)
    list_bankacct[1].deposit(8000)
    list_bankacct[0].withdraw(12000)
    list_bankacct[0].withdraw(7000)
    list_bankacct[0].withdraw(3000)
    list_bankacct[1].withdraw(1000)
    list_bankacct[1].withdraw(2000)
    list_bankacct[1].withdraw(3000)

    for i in list_bankacct:
        i.display_transaction_history()
