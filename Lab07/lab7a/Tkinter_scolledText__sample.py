import tkinter
import tkinter.scrolledtext
class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Registration Form")
        self.geometry("370x160")
        list_student = [Student("Kelvin Yip", "Male", ["English","Chinese"]),
                             Student("Cow Leung", "Female", ["English",])]
        lbl_stu_list = tkinter.Label(self, text="Student's List", font=("bold",15))
        lbl_stu_list.place(x=20, y=10)
        
        txt_output = tkinter.scrolledtext.ScrolledText(self, width=40, height=5)
        txt_output.place(x=20, y=40)
        txt_output.delete("0.0", tkinter.END)        
        for i in list_student:
            txt_output.insert(tkinter.INSERT,i)
        
        btn_quit = tkinter.Button(self, text="Quit", width=6, command=self.destroy)
        btn_quit.place(x=290,y=130)


class Student:
    def __init__(self, name, gender, list_language):
        self.__name = name
        self.__gender = gender
        self.__list_language = list_language
    def __str__(self):
        language_output = ""
        for i in self.__list_language:
            if self.__list_language.index(i) == 0:
                language_output += i
            else:
                language_output += ", " + i
        return (f"Name: {self.__name}\n"+
                f"Gender: {self.__gender}\n"+
                f"Language: {language_output}\n")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
