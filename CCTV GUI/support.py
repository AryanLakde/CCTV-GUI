from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Contacts")
root.iconbitmap("C:/Users/aryan/Desktop/Project/icons/contact.ico")
root.geometry('400x400')

t = Label(text="Contact",font=('Helvetica 20 underline'))
t.grid(row=0, column=0,pady=20)

# Number1 
c1Label = Label(text="Thane region : + 022 2542 1373",font=(20))
c1Label.grid(row=1, column=0)


# Number2 
c2Label = Label(text="Mumbai region : + 022 2542 1562",font=(20))
c2Label.grid(row=2, column=0)



root.mainloop()