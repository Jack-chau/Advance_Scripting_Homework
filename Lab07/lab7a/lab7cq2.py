import tkinter
import tkinter.scrolledtext
class Student:
    def __init__(self, name, email, gender, region, list_language):
        self.__name = name
        self.__email = email
        self.__gender = gender
        self.__region = region
        self.__list_language = list_language
        def __str__(self):
            language_output = ""
            for i in self.__list_language:
                if self.__list_language.index(i) == 0:
                    language_output += i
                else:
                    language_output += ", " + i
            return (f"Name: {self.__name}\n" +
    f"Email: {self.__email}\n" +
    f"Gender: {self.__gender}\n" +
    f"Region: {self.__region}\n" +
    f"Language: {language_output}\n")
class Application(tkinter.Tk):
    def reset_form(self):
        self.ent_name.delete(0, tkinter.END)
        self.ent_email.delete(0, tkinter.END)
        self.var_gender.set(" ")
        self.var_region.set("Select your Region")
        self.var_lang_eng.set(0)
        self.var_lang_chi.set(0)
    def submit(self):
        list_language = list()
        if self.var_lang_eng.get()==1:
            list_language.append("English")
        if self.var_lang_chi.get()==1:
            list_language.append("Chinese")
            self.list_student.append(Student(self.ent_name.get(), self.ent_email.get(),
            self.var_gender.get(), self.var_region.get(), list_language))
            self.txt_output.delete("0.0", tkinter.END)
        for i in self.list_student:
            self.txt_output.insert(tkinter.INSERT,i)
            self.reset_form()
    def clear(self):
        self.list_student = list()
        self.txt_output.delete("0.0", tkinter.END)
    def __init__(self):
        super().__init__()
        self.title("Student Registration Form")
        self.geometry("520x260")
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.rowconfigure(5, pad=5)
        self.rowconfigure(6, pad=5)
        self.lbl_reg_form = tkinter.Label(self, text="Student Registration Form", font=("bold",15))
        self.lbl_reg_form.grid(row=0, column=0, columnspan=3)
        self.lbl_name = tkinter.Label(self, text="Name", font=("bold",10))
        self.lbl_name.grid(row=1, column=0)
        self.ent_name = tkinter.Entry(self)
        self.ent_name.grid(row=1, column=1, columnspan=2, sticky=tkinter.W+tkinter.E)
        self.lbl_email = tkinter.Label(self, text="Email", font=("bold",10))
        self.lbl_email.grid(row=2, column=0)
        self.ent_email = tkinter.Entry(self)
        self.ent_email.grid(row=2, column=1, columnspan=2, sticky=tkinter.W+tkinter.E)
        self.lbl_gender = tkinter.Label(self, text="Gender", font=("bold",10))
        self.lbl_gender.grid(row=3, column=0)
        self.var_gender = tkinter.StringVar()
        self.rdo_gender_m = tkinter.Radiobutton(self, text="Male", variable=self.var_gender,
        value="Male")
        self.rdo_gender_m.grid(row=3, column=1)
        self.rdo_gender_f = tkinter.Radiobutton(self, text="Female", variable=self.var_gender,
        value="Female")
        self.rdo_gender_f.grid(row=3, column=2)
        self.lbl_region = tkinter.Label(self, text="Region", font=("bold",10))
        self.lbl_region.grid(row=4, column=0)
        list_of_region=['Hong Kong', 'Macau', 'US', 'UK', 'Japan']
        self.var_region = tkinter.StringVar()
        self.lst_region=tkinter.OptionMenu(self, self.var_region, *list_of_region)
        self.lst_region.grid(row=4, column=1, columnspan=2, sticky=tkinter.W+tkinter.E)
        self.lbl_language = tkinter.Label(self, text="Language", font=("bold",10))
        self.lbl_language.grid(row=5, column=0)
        self.var_lang_eng = tkinter.IntVar()
        self.chk_lang_eng = tkinter.Checkbutton(self,text="English", variable=self.var_lang_eng)
        self.chk_lang_eng.grid(row=5, column=1)
        self.var_lang_chi = tkinter.IntVar()
        self.chk_lang_chi = tkinter.Checkbutton(self,text="Chinese", variable=self.var_lang_chi)
        self.chk_lang_chi.grid(row=5, column=2)
        self.btn_confirm = tkinter.Button(self, text="Submit", width=6, command=self.submit)
        self.btn_confirm.grid(row=6, column=2, sticky=tkinter.E)
        self.lbl_stu_list = tkinter.Label(self, text="Student's List", font=("bold",10))
        self.lbl_stu_list.grid(row=1, column=3)
        self.txt_output = tkinter.scrolledtext.ScrolledText(self, height=10, width=30)
        self.txt_output.grid(row=2, column=3, rowspan=4)
        self.btn_clear = tkinter.Button(self, text="Clear", width=6, command=self.clear)
        self.btn_clear.grid(row=6, column=3, sticky=tkinter.E)
        self.reset_form()
        self.list_student = list()
if __name__ == "__main__":
    app = Application()
    app.mainloop()