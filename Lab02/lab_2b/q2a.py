class Bread:
    def __init__( self, name : str, price : float ):
        self.__name = name
        self.__price = price
        self.__total_quantity = 0
        self.__total_sales = 0
        self.__total_sales_no = 0
    
    def get_name( self ):
        return self.__name

    def get_price( self ):
        return self.__price

    def get_quantity( self ) :
        return int( self.__total_quantity )
    
    def get_sales( self ):
        return float( self.__total_sales )
    
    def get_sales_no( self ):
        return int( self.__total_sales_no )
    
    def compute_sales( self, quantity : float ):
        sales = self.__price * quantity
        self.__total_sales_no += 1
        self.__total_sales += sales
        self.__total_quantity += quantity
        return float( sales )