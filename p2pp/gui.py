from Tkinter import *
import Tkinter
import tkMessageBox

root = Tk()
root.iconbitmap('favicon.ico')
root.iconify()

def center(win, width, height):
    win.update_idletasks()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def clicked():
    root.destroy()

def usererror(  bodyText ):
    tkMessageBox.askcancel("P2PP - Error Occurred", bodyText)


def showwarnings(  warningList ):
    root.title("P2PP - Process Warnings")
    center(root, 800, 600)
    root.deiconify()


    lbl = Label(root, text="P2PP - Process Warnings", padx=5, pady=5, font=("Arial Bold", 24), fg="red")
    lbl.pack(side=TOP, fill=Y)

    canvas = Canvas(root)
    canvas.pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)
    sb = Scrollbar(canvas)
    list = Text(canvas)

    sb.pack(side = RIGHT, fill=Y)
    for warning in range(len(warningList)-4):
        list.insert(END, warningList[warning+4][1:])
    list.pack(side=LEFT, fill=BOTH, expand=1)
    sb.config(command = list.yview)


    btn = Button(root,text='Close', command=clicked)
    btn.pack(side=BOTTOM, fill=Y, pady=10)
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)
    root.mainloop()




