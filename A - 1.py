from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Denomination Calculator')
root.configure(bg='light green')
root.geometry('400x400')

label1 = Label(root, text="Welcome to Denominator Counter Application.",bg="light green")
label1.place(relx=0.5, y=140, anchor=CENTER) 

def msg():
    MsgBox = messagebox.showinfo("Alert", "Click on OK to continue")
    if MsgBox == 'ok':
        topwin()

Button1 = Button(root, text="Click to Start!", command=msg, bg='green', fg = 'white')
Button1.place(x=160,y=260)

def topwin():
    top = Toplevel()
    top.title('Denominations Calculator')
    top.configure(bg='light blue')
    top.geometry('600x500')
    label=Label(top,text="Enter Total Amount")
    entry=Entry(top)
    lbl = Label(top, text="Number of Notes are as given")   
    l1 = Label(top,text="2000")
    l2 = Label(top, text='500')
    l3 = Label(top,text = "100")
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    def calculator():

        global amount
        amount = int(entry.get())
        note2000= amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0,END)
        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))
    btn = Button(top, text='Calculate', command=calculator, bg='Brown', fg = 'white')
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()

root.mainloop()