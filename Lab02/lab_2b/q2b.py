#function called by main program to display menu
from q2a import Bread
def display_menu():
    print("\nBakery Shop Menu:")
    print(f"{'No':>2s}. | {'Bread Type':<15s} | "
          f"{'Price':<4s}" )
    for i in range ( len(list_bread) ):
        print (f"{i:>2}. | "
               f"{list_bread[i].get_name():<15s} | "
               f"${list_bread[i].get_price()}")

#function called by main program to display statistics
def display_statistics():
    print ("Statistics of Bakery Shop:")
    # Print Bread Name
    output_string = f"{'Bread Name':<20s}"
    for i in list_bread:
        output_string += f"| {i.get_name():<12s} "
    print (output_string)

    # Complete this part to print Price per Bread
    output_price = f"{'Price per Bread':<20s}"
    for i in list_bread:
        output_price += f"| { str( i.get_price()):>12s} "
    print( output_price )

    # Complete this part to print Total Quantity
    output_quantity = f"{'Total Quantity':<20s}"
    for i in list_bread:
        output_quantity += f"| { str( i.get_quantity()):>12s} "
    print( output_quantity )

    # Complete this part to print Total Sales
    output_sales = f"{'Total Sales':<20s}"
    for i in list_bread:
        output_sales += f"| { str( i.get_sales()):>12s} "
    print( output_sales )

    # Complete this part to print Total Sales Number
    output_sales_no = f"{'Total Sales Number':<20s}"
    for i in list_bread:
        output_sales_no += f"| { str( i.get_sales_no()):>12s} "
    print( output_sales_no )

        
if __name__ == "__main__":
    list_bread = list()
    list_bread.append(Bread("French Toast",25))
    list_bread.append(Bread("Cheese Loaf",30))
    list_bread.append(Bread("Lemon Tart",20))
    list_bread.append(Bread("Black Forest", 65))
    list_bread.append(Bread("Python Skin", 200))
    
    print("Welcome to Bakery Shop System.")
    display_menu()
    display_statistics()

    while True:
        while True:
            try:
                input_string=(f"Please input your choice."
                              f"(0 - {len(list_bread)-1}), "
                              f"s for statistics:")
                input_result = input(input_string)
                if input_result == "s":
                    display_statistics()
                    display_menu()
                    continue
                input_bread_type = int(input_result)
                if (input_bread_type < 0 or
                    input_bread_type >= len(list_bread)):
                    print ("Invalid input for choice")
                    continue
                break
            except:
                print ("Invalid input for choice.")
        # Modify the following part to validate
        # user's input on quantity
        try: 
            input_quantity = int( input("Please input quantity:") )
        except:
            print( "value error")

        selected_bread_type = list_bread[input_bread_type]
        sales = selected_bread_type.compute_sales(input_quantity)
        # Print the no. of pieces of bread, bread name and sales
        # of current order with reference from sample output

        print( f"The price of { input_quantity } pieces of { selected_bread_type.get_name() } is {sales:.1f} " )