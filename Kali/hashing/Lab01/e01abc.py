import subprocess
from tkinter import *
import threading
import time 
from tkinter import ttk

root = Tk()
root.title( 'subprocess + Tkinter' )

def startcommand():
    t = threading.Thread( target=runcommand )
    t.start()

    
def runcommand():
    cmd = cmdtextbox.get()
    cmdtextbox.config( state="disabled", readonlybackground='gray')
    cmdtextbox.grid( row=0, column=1, padx=2, pady=10, sticky=W )
    running_label = Label( root, text='Running....' )
    running_label.grid( row=2, column=0, padx=10, sticky=W)
    progress_bar = ttk.Progressbar( root, mode='indeterminate' )
    progress_bar.grid( row=3, column=0, padx=10, sticky=W)
    progress_bar.start()
    time.sleep(2)
    cmd_result = subprocess.run( cmd, shell = True, capture_output=True, text=True )
    output = cmd_result.stdout
    outputtextbox.insert( END, output )
    running_label.config( text='completed')
    progress_bar.destroy()

cmdlabel = Label( root, text='CMD: ', fg='red', font=( 'Consoleas', 14) )
cmdlabel.grid( row=0, column=0, padx=5, sticky=W )
cmdtextbox = Entry( root, width=30 )
cmdtextbox.grid( row=0, column=1, padx=2, pady=10, sticky=W )
runbtn = Button( root, text='RUN', fg='blue', command=startcommand )
runbtn.grid( row=1, column=1, padx=5 )
outputlabel = Label( root, text='OUTPUT:', fg='green', font=('Consolas', 10 ) )
outputlabel.grid( row=1, column=0, padx=10, sticky=W)



outputtextbox = Text(root,height=10,width=60,font=('Consolas',9))
outputtextbox.grid(row=4,column=0,columnspan=3,padx=10,pady=10,sticky=W)


root.mainloop()