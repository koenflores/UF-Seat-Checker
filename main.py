from checkSeat import CheckSeat
from dialog import MyDialog
from tkinter import Button
from tkinter import Tk


root = Tk()
root.withdraw()
d = MyDialog(root,"UF ID", "UF Password", "Gmail", "Gmail Password ","Course Code")
root.wait_window(d.top)
CheckSeat(d.values)