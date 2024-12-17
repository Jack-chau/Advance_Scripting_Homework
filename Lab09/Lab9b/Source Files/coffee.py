from flask import Flask, request, render_template
import sys

class Order:
    LARGER_CUPE_PRICE = 5
    COLD_PRICE = 3
    COFFEE_LIST = [ ( "Cappuccino", 25 ),
                    ( "Espresso", 20 ),
                    ( "Latte", 15 ),
                    ( "Mocha", 30 )
                  ]
    __current_sales_list = list()
    #static variables used for statistics
    __total_number_sales = 0
    __lowest_sales_amount = sys.maxsize
    __highest_sales_amount = 0
    __total_sales_amount = 0
    __cups_of_coffee_sold = { "Cappuccino" : 0, "Espresso" : 0, "Latte" : 0, "Mocha" : 0 }
    def __init__( self, name, quantity, large_cup, cold ) :
        self.__coffee_name = name
        self.__coffee_quantity = quantity
        self.__large_cup = large_cup
        self.__cold = cold
    def get_coffee_name( self ):
        return self.__coffee_name
    
    def get_quantity( self ):
        return self.__coffee_quantity
    
    def calculate_current_sales( self ):
        sales = Order.get_coffee_price( self.__coffee_name )
        if self.__large_cup :
            sales += Order.LARGER_CUPE_PRICE
        if self.__cold :
            sales += Order.COLD_PRICE
        return sales * self.__coffee_quantity

    @staticmethod
    def get_total_number_sales():
        return Order.__total_number_sales
    @staticmethod
    def get_lowest_sales_amount():
        return Order.__lowest_sales_amount
    @staticmethod
    def get_highest_sales_amount():
        return Order.__highest_sales_amount
    @staticmethod
    def get_total_sales_amount():
        return Order.__total_sales_amount
    @staticmethod
    def get_cups_of_coffee_sold( coffee_name ):
        return Order.__cups_of_coffee_sold.get( coffee_name, 0 )
    @staticmethod
    def get_coffee_price( coffee_name ):
        for i in Order.COFFEE_LIST:
            if i[0] == coffee_name:
                return i[1]
    @staticmethod
    def confirm_order():
        Order.__total_number_sales += 1
        current_sales = Order.calculate_current_sales_total()
        if( Order.calculate_current_sales_total() < Order.__lowest_sales_amount ):
            Order.__lowest_sales_amount = current_sales
        if( Order.calculate_current_sales_total() > Order.__highest_sales_amount ):
            Order.__highest_sales_amount = current_sales
        Order.__total_sales_amount += current_sales
        for i in Order.__current_sales_list:
            Order.__cups_of_coffee_sold[i.get_coffee_name()] = Order.__cups_of_coffee_sold.get( i.get_coffee_name(),0) + i.get_quantity()

        # empty current sales list after order is confirmed
        Order.__current_sales_list = list()

    @staticmethod
    def calculate_current_sales_total():
        total = 0
        for i in Order.__current_sales_list:
            total += i.calculate_current_sales()
        return total

    @staticmethod
    def get_current_sales_list():
        return Order.__current_sales_list
    
    @staticmethod
    def add_into_list( order ):
        Order.__current_sales_list.append( order )

    #Used for display sales records in current order text area
    def __str__(self):
        option = ""
        if self.__large_cup or self.__cold:
            option += " with option "
        if self.__large_cup:
            option += "LARGE CUP"
        if self.__large_cup and self.__cold:
            option += " and "
        if self.__cold:
            option += "COLD"
        return (f"{self.__coffee_name} " +
                f"{self.__coffee_quantity} " +
                f"cups{option}: " +
                f"${self.calculate_current_sales():.2f}\n")

app = Flask( __name__ )
@app.route( '/' )
@app.route( '/', methods = ["POST"] )
def coffee_confirm():
    if request.method == "POST":
        if request.form['action'] == "Confirm Item" :
            coffee = request.form['coffee']
            quantity = int( request.form['quantity'] )
            large = request.form.get( 'large' )
            if large :
                large = True
            else :
                large = False
            cold = request.form.get('cold')
            if cold:
                cold = True
            else :
                cold = False
            Order.add_into_list(Order(coffee, quantity, large, cold))
        elif request.form["action"]=="Confirm Order":
            Order.confirm_order()
    return render_template("coffee_form.html", current_sales_list = Order.get_current_sales_list(), current_sales_total = Order.calculate_current_sales_total())

@app.route("/statistics")
def coffee_statistics():
    list_statistics = list()
    list_statistics.append(Order.get_total_number_sales())
    list_statistics.append(Order.get_lowest_sales_amount())
    list_statistics.append(Order.get_highest_sales_amount())
    list_statistics.append(Order.get_total_sales_amount())
    list_statistics.append(Order.get_total_sales_amount()/Order.get_total_number_sales())
    for coffee in Order.COFFEE_LIST:
        list_statistics.append(coffee[0]+":"+str(Order.get_cups_of_coffee_sold(coffee[0])))
    return render_template("coffee_statistics.html", html_list = list_statistics)

if __name__ == "__main__":
    app.run()
