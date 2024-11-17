import tkinter
import tkinter.scrolledtext
import tkinter.messagebox
import sys
class Order:
    LARGE_CUPE_PRICE = 5
    COLD_PRICE = 3
    COFFEE_LIST = [("Cappuccino",25),("Espresso",20),
    ("Latte",15),("Mocha",30)]
    __current_sales_list = list()
    #static variables used for statistics
    __total_number_sales = 0
    __lowest_sales_amount = sys.maxsize
    __highest_sales_amount = 0
    __total_sales_amount = 0
    __cups_of_coffee_sold = {"Cappuccino":0, "Espresso":0,
    "Latte":0, "Mocha":0}
    def __init__(self,name, quantity, large_cup, cold):
        self.__coffee_name = name
        self.__coffee_quantity = quantity
        self.__large_cup = large_cup
        self.__cold = cold
    def get_coffee_name(self):
        return self.__coffee_name
    def get_quantity(self):
     return self.__coffee_quantity
    def calculate_current_sales(self):
        sales = Order.get_coffee_price(self.__coffee_name)
        if self.__large_cup:
            sales += Order.LARGE_CUPE_PRICE
        if self.__cold:
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
    def get_cups_of_coffee_sold(coffee_name):
        return Order.__cups_of_coffee_sold.get(coffee_name,0)
    @staticmethod
    def get_coffee_price(coffee_name):
        for i in Order.COFFEE_LIST:
            if i[0]==coffee_name:
                return i[1]
    @staticmethod
    def confirm_order():
        Order.__total_number_sales += 1
        current_sales = Order.calculate_current_sales_total()
        if (Order.calculate_current_sales_total() <
            Order.__lowest_sales_amount):
            Order.__lowest_sales_amount = current_sales
        if (Order.calculate_current_sales_total() >
            Order.__highest_sales_amount):
            Order.__highest_sales_amount = current_sales
            Order.__total_sales_amount += current_sales
        for i in Order.__current_sales_list:
            Order.__cups_of_coffee_sold[i.get_coffee_name()] = Order.__cups_of_coffee_sold.get(i.get_coffee_name(),0) + i.get_quantity()
            #empty current sales list after order is confirmed
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
    def add_into_list(order):
        Order.__current_sales_list.append(order)
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
            "{self.__coffee_quantity} " +
            "cups{option}: " +
            "${self.calculate_current_sales():.2f}\n")
class Statistics(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("ABC Cafe Statistics")
        self.geometry("300x430")
        self.lbl_statistics = tkinter.Label(self, text="Coffee Shop Statistics", font=("bold",15))
        self.lbl_statistics.place(x=20, y=10)

        self.lbl_total_number_sales = tkinter.Label(self, text=f"Total number sales = {Order.get_total_number_sales()}", font=("bold",10))
        self.lbl_total_number_sales.place(x=20, y=50)
        self.lbl_lowest_sales_amount = tkinter.Label(self, text=f"Lowest sales Amount = {Order.get_lowest_sales_amount():.2f}", font=("bold",10))
        self.lbl_lowest_sales_amount.place(x=20, y=80)
        self.lbl_highest_sales_amount = tkinter.Label(self, text=f"Highest sales Amount = {Order.get_highest_sales_amount():.2f}", font=("bold",10))
        self.lbl_highest_sales_amount.place(x=20, y=110)
        self.lbl_total_sales_amount = tkinter.Label(self, text=f"Total sales Amount = {Order.get_total_sales_amount():.2f}", font=("bold",10))
        self.lbl_total_sales_amount.place(x=20, y=140)
        self.lbl_average_sales_amount = tkinter.Label(self, text=f"Average sales Amount = {(Order.get_total_sales_amount() / Order.get_total_number_sales()):.2f}", font=("bold",10))
        self.lbl_average_sales_amount.place(x=20, y=170)
        self.lbl_list_coffee_sold = tkinter.Label(self, text="List of number of cups coffee sold:",
        font=("bold",10))
        self.lbl_list_coffee_sold.place(x=20, y=230)
        self.lbl_cappuccino = tkinter.Label(self, text=f" Cappuccino: {Order.get_cups_of_coffee_sold('Cappuccino')}", font=("bold",10))
        self.lbl_cappuccino.place(x=20, y=260)
        self.lbl_espresso = tkinter.Label(self, text=f" Espresso: {Order.get_cups_of_coffee_sold('Espresso')}", font=("bold",10))
        self.lbl_espresso.place(x=20, y=290)
        self.lbl_latte = tkinter.Label(self, text=f" Latte: {Order.get_cups_of_coffee_sold('Latte')}",
        font=("bold",10))
        self.lbl_latte.place(x=20, y=320)
        self.lbl_mocha = tkinter.Label(self, text=f" Mocha: {Order.get_cups_of_coffee_sold('Mocha')}", font=("bold",10))
        self.lbl_mocha.place(x=20, y=350)
        self.btn_quit = tkinter.Button(self, text="Quit", width=12, command=self.destroy)
        self.btn_quit.place(x=190,y=370)
class Application(tkinter.Tk):
    def reset_form(self):
        self.ent_quantity.delete(0, tkinter.END)
        self.var_coffee.set(Order.COFFEE_LIST[0][0])
        self.var_options_large.set(0)
        self.var_options_cold.set(0)
        self.lbl_current_sales_total_large = tkinter.Label(self,
        text=f"{Order.calculate_current_sales_total():.2f} ", font=("bold",15))
        self.lbl_current_sales_total_large.place(x=140, y=510)
    def confirm_item(self):
        try:
            options_large = False
            options_cold = False
            if self.var_options_large.get()==1:
                options_large = True
            if self.var_options_cold.get()==1:
                options_cold = True
            current_order=Order(self.var_coffee.get(), int(self.ent_quantity.get()), options_large,
            options_cold)
            Order.add_into_list(current_order)
            self.txt_current_order.delete("0.0", tkinter.END)
            for i in Order.get_current_sales_list():
                self.txt_current_order.insert(tkinter.INSERT,i)
            self.reset_form()
        except ValueError as e:
            tkinter.messagebox.showwarning("Warning","Incorrect input for quantity.\nPlease input again!")

    def confirm_order(self):
        if len(Order.get_current_sales_list())==0:
            tkinter.messagebox.showinfo("Information", "No items bought for this order yet!")
            return
        Order.confirm_order()
        self.btn_statistics.config(state=tkinter.NORMAL)
        self.txt_current_order.delete("0.0", tkinter.END)
        self.reset_form()
    def show_statistics_form(self):
        Statistics()
    def __init__(self):
        super().__init__()
        self.title("ABC Cafe")
        self.geometry("550x600")
        self.lbl_menu = tkinter.Label(self, text="Coffee Shop Menu", font=("bold",10))
        self.lbl_menu.place(x=20, y=10)
        self.var_coffee = tkinter.StringVar()
        self.rdo_coffee_cappuccino = tkinter.Radiobutton(self, text=f"{Order.COFFEE_LIST[0]
        [0]}\t${Order.COFFEE_LIST[0][1]:.2f}", variable=self.var_coffee,
        value=Order.COFFEE_LIST[0][0])
        self.rdo_coffee_cappuccino.place(x=20,y=40)
        self.rdo_coffee_espresso = tkinter.Radiobutton(self, text=f"{Order.COFFEE_LIST[1][0]}\t\t${Order.COFFEE_LIST[1][1]:.2f}", variable=self.var_coffee, value=Order.COFFEE_LIST[1][0])
        self.rdo_coffee_espresso.place(x=20,y=70)
        self.rdo_coffee_latte = tkinter.Radiobutton(self, text=f"{Order.COFFEE_LIST[2][0]}\t\t${Order.COFFEE_LIST[2][1]:.2f}", variable=self.var_coffee, value=Order.COFFEE_LIST[2][0])
        self.rdo_coffee_latte.place(x=20,y=100)
        self.rdo_coffee_mocha = tkinter.Radiobutton(self, text=f"{Order.COFFEE_LIST[3][0]}\t\t${Order.COFFEE_LIST[3][1]:.2f}", variable=self.var_coffee, value=Order.COFFEE_LIST[3][0])
        self.rdo_coffee_mocha.place(x=20,y=130)
        self.lbl_quantity = tkinter.Label(self, text="Quantity:", font=("bold",10))
        self.lbl_quantity.place(x=20, y=170)
        self.ent_quantity = tkinter.Entry(self, width=5)
        self.ent_quantity.place(x=100, y=170)
        self.lbl_options = tkinter.Label(self, text="Options:", font=("bold",10))
        self.lbl_options.place(x=20, y=210)
        self.var_options_large = tkinter.IntVar()
        self.chk_options_large = tkinter.Checkbutton(self,text="Large Cup + $5.00",
        variable=self.var_options_large)
        self.chk_options_large.place(x=20,y=240)
        self.var_options_cold = tkinter.IntVar()
        self.chk_options_cold = tkinter.Checkbutton(self,text="Cold +$3.00",
        variable=self.var_options_cold)
        self.chk_options_cold.place(x=20,y=270)
        self.btn_confirm_item = tkinter.Button(self, text="Confirm Item", width=12,
        command=self.confirm_item)
        self.btn_confirm_item.place(x=430,y=270)
        self.lbl_current_order = tkinter.Label(self, text="Current Order:", font=("bold",10))
        self.lbl_current_order.place(x=20, y=310)
        self.txt_current_order = tkinter.scrolledtext.ScrolledText(self, width=60, height=10)
        self.txt_current_order.place(x=20, y=340)
        self.lbl_current_sales_total = tkinter.Label(self, text="Current Sales Total:", font=("bold",10))
        self.lbl_current_sales_total.place(x=20, y=515)
        self.btn_confirm_order = tkinter.Button(self, text="Confirm Order", width=12,
        command=self.confirm_order)
        self.btn_confirm_order.place(x=430,y=515)
        self.btn_statistics = tkinter.Button(self, text="Show Statistics", state=tkinter.DISABLED,
        width=12, command=self.show_statistics_form)
        self.btn_statistics.place(x=330,y=555)
        self.btn_quit = tkinter.Button(self, text="Quit", width=12, command=self.destroy)
        self.btn_quit.place(x=430,y=555)
        self.reset_form()
if __name__ == "__main__":
    app = Application()
    app.mainloop()