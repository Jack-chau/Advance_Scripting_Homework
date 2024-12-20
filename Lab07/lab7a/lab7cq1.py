import tkinter
class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("Review")
        frm_base = tkinter.Frame(self)
        frm_base.pack(fill=tkinter.BOTH, expand=True)
        frm_title = tkinter.Frame(frm_base)
        frm_title.pack(fill=tkinter.BOTH)
        lbl_title = tkinter.Label(frm_title, text="Title", anchor=tkinter.W, width=6)
        lbl_title.pack(side=tkinter.LEFT, padx=5, pady=5)
        ent_title = tkinter.Entry(frm_title)
        ent_title.pack(fill=tkinter.X, padx=5, expand=True)
        frm_author = tkinter.Frame(frm_base)
        frm_author.pack(fill=tkinter.BOTH)
        lbl_author = tkinter.Label(frm_author, text="Author", anchor=tkinter.W, width=6)
        lbl_author.pack(side=tkinter.LEFT, padx=5, pady=5)
        ent_author = tkinter.Entry(frm_author)
        ent_author.pack(fill=tkinter.X, padx=5, expand=True)
        frm_review = tkinter.Frame(frm_base)
        frm_review.pack(fill=tkinter.BOTH, expand=True)
        lbl_review = tkinter.Label(frm_review, text="Review", anchor=tkinter.W, width=6)
        lbl_review.pack(side=tkinter.LEFT, anchor=tkinter.N, padx=5, pady=5)
        txt_review = tkinter.Text(frm_review, height=1)
        txt_review.pack(fill=tkinter.BOTH, anchor=tkinter.N, pady=5, padx=5, expand=True)
        frm_button = tkinter.Frame(frm_base)
        frm_button.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        self.btn_close = tkinter.Button(frm_button, text="Close")
        self.btn_close.pack(side=tkinter.RIGHT, padx=5, pady=5)
        self.btn_ok = tkinter.Button(frm_button, text="OK")
        self.btn_ok.pack(side=tkinter.RIGHT)
if __name__ == '__main__':
    app = Application()
    app.mainloop()