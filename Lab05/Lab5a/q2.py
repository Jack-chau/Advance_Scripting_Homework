#No need to modify the student class
class Student :
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__list_module = list()
    def add_module(self, module):
        self.__list_module.append(module)
    def get_list_module(self):
        return self.__list_module
    def display(self):
        print (f"Student {self.__name} ({self.__id}) "
               f"enrolled the following module(s):")
        for module in self.__list_module:
            print (module)

class Module:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
    #implement your methods here
    def __str__(self):
        return f'\t{self.__id} - {self.__name}'
    def __eq__(self, other):
        if self.__id == other.__id:
            return True


#You are not allowed to modify the following program
if __name__ == "__main__":
    list_student = list()
    kelvin = Student("201234567","Kelvin")
    kelvin.add_module(Module("ITE3102", "Network Fundamentals"))
    kelvin.add_module(Module("ITP3915",
                             "Programming Fundamentals"))
    kelvin.add_module(Module("ITP4456", "Database Applications"))
    kelvin.add_module(Module("ITP4451", "IoT Fundamentals"))
    kelvin.add_module(Module("ITP4457", "Web Technologies"))
    kelvin.add_module(Module("ITP4458", "Wireless Technologies"))
    kelvin.add_module(Module("ITP4459",
                             "Advanced Scripting Technology"))
    
    peter = Student("202345678", "Peter")
    peter.add_module(Module("ITE3102", "Network Fundamentals"))
    peter.add_module(Module("ITP3915",
                            "Programming Fundamentals"))
    peter.add_module(Module("ITP4456", "Database Applications"))
    peter.add_module(Module("ITP4459",
                            "Advanced Scripting Technology"))
    peter.add_module(Module("ITP4410", "Internet Programming"))
    peter.add_module(Module("ITP4413", "Server Administration"))

    list_student.append(kelvin)
    list_student.append(peter)

    # display stduent information
    for student in list_student:
        student.display()

    # display student common modules
    print ("Both Kelvin and Peter studies in the following modules:")
    for module1 in kelvin.get_list_module():
        for module2 in peter.get_list_module():
            if module1 == module2:
                print (module1)
