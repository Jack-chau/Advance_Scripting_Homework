import tkinter as tk

root = tk.Tk()
root.title( 'simple app' )

def on_click() :
    label.config( text="Button Clicked!")

label = tk.Label( root, text = "Label 1" )
label.grid( row=0, column=0 )

print( label.config().keys() )

btn = tk.Button( root, text = "Button 1", command = on_click )
btn.grid( row=0, column=1 )


root.mainloop()
root.mainloop()