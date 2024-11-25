from tkinter import *
from tkinter import messagebox

root = Tk()
root.title="Registration"

Label(text="Email").grid(row=1,column=0,padx=5,pady=5)
Label(text="Password").grid(row=2,column=0,padx=5,pady=5)
email_entry=Entry(root)
pass_entry=Entry(root)

root.mainloop()
