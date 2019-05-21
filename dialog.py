from tkinter import Toplevel, Label, Entry, Button, Pack, Tk, Place, RIGHT, LEFT
import tkinter.messagebox

class MyDialog:

    def __init__(self, parent, label1, label2, label3, label4, label5):

        top = self.top = Toplevel(parent)

        L1 = Label(top, text=label1)
        L1.pack()
        L1.place(x=10,y=10)

        L2 = Label(top, text=label2)
        L2.pack()
        L2.place(x=10,y=35)

        L3 = Label(top, text=label3)
        L3.pack()
        L3.place(x=10,y=60)

        L4 = Label(top, text=label4)
        L4.pack()
        L4.place(x=10,y=85)

        L5 = Label(top, text=label5)
        L5.pack()
        L5.place(x=10,y=110)


        self.E1 = Entry(top)
        self.E1.pack(side = RIGHT)
        self.E1.place(x = 100 , y=10)

        self.E2 = Entry(top,show='*')
        self.E2.pack(side = RIGHT)
        self.E2.place(x = 100 , y=35)

        self.E3 = Entry(top)
        self.E3.pack(side = RIGHT)
        self.E3.place(x = 100 , y=60)

        self.E4 = Entry(top,show='*')
        self.E4.pack(side = RIGHT)
        self.E4.place(x = 100 , y=85)

        self.E5 = Entry(top)
        self.E5.pack(side = RIGHT)
        self.E5.place(x = 100 , y=110)


        b = Button(top, text="ENTER", command=self.ok)
        b.pack()
        b.place(x = 80 ,y= 140)

        self.values = dict()

    def ok(self):

        self.values['UfId'] = self.E1.get()
        self.values['UfPass'] = self.E2.get()
        self.values['Gmail'] = self.E3.get()
        self.values['GmailPass'] = self.E4.get()
        self.values['CourseCode'] = self.E5.get()

        self.top.destroy()

  
        
def InvalidLogIn():
    tops = Tk()
    tkinter.messagebox.showinfo("Error", "INVALID LOG IN, TRY AGAIN")
    tops.mainloop()
    tops.withdraw()
    