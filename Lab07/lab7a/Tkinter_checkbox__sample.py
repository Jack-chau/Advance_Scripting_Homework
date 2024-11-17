import tkinter
class Application(tkinter.Tk):
    def reset_form (self):
        self.__var_name.set("")
        self.__var_lang_eng.set(-1)
        self.__var_lang_chi.set(3)
    def submit(self):
        list_language = list()
        if self.__var_lang_eng.get()==1:
            list_language.append("English")
        if self.__var_lang_chi.get()==1:
            list_language.append("Chinese")
        student = Student(self.__var_name.get(), list_language)
        print (student)
        self.reset_form()
    def __init__(self):
        super().__init__()
        self.title("Student Registration Form")
        self.geometry("370x140")
        ## lbl_reg_form, lbl_name, self.__var_name and ent_name omitted here
        lbl_reg_form = tkinter.Label(self, text="Student Registration Form", font=("bold",15))
        lbl_reg_form.place(x=20, y=10)
        lbl_name = tkinter.Label(self, text="Name", font=("bold",10))
        lbl_name.place(x=20, y=50)
        self.__var_name = tkinter.StringVar()
        ent_name = tkinter.Entry(self, textvariable=self.__var_name, width=40)
        ent_name.place(x=100, y=50)
        lbl_gender = tkinter.Label(self, text="Gender", font=("bold",10))
        lbl_gender.place(x=20, y=80)
        self.__var_gender = tkinter.StringVar()
        # rdo_gender_m = tkinter.Radiobutton(self, text="Male", variable=self.__var_gender, value="Male")
        # rdo_gender_m.place(x=100,y=80)
        # rdo_gender_f = tkinter.Radiobutton(self, text="Female", variable=self.__var_gender, value="Female")
        # rdo_gender_f.place(x=180,y=80)
        # self.__var_gender.set(" ")      
        lbl_language = tkinter.Label(self, text="Language", font=("bold",10))
        lbl_language.place(x=20, y=80)
        self.__var_lang_eng = tkinter.IntVar()
        chk_lang_eng = tkinter.Checkbutton(self,text="English", variable=self.__var_lang_eng)
        chk_lang_eng.place(x=100,y=80)
        self.__var_lang_chi = tkinter.IntVar()
        chk_lang_chi = tkinter.Checkbutton(self,text="Chinese", variable=self.__var_lang_chi)
        chk_lang_chi.place(x=180,y=80)
        btn_confirm = tkinter.Button(self, text="Submit", width=6, command=self.submit)
        btn_confirm.place(x=230,y=110)
        btn_quit = tkinter.Button(self, text="Quit", width=6, command=self.destroy)
        btn_quit.place(x=290,y=110)
        self.reset_form()
class Student:
    def __init__(self, name, region):
        self.__name = name
        self.__region = region
    def __str__(self):
        return f"Name: {self.__name}\nRegion: {self.__region}"


if __name__ == "__main__":
    app = Application()
    app.mainloop()
