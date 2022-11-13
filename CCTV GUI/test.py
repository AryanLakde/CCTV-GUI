from tkinter import *
from PIL import ImageTk, Image
from record import record


root = Tk()
root.title("Control Panel")
root.iconbitmap("C:/Users/aryan/Downloads/aj11.ico")
root.geometry('1080x600')

def support():
    con = Toplevel()
    con.title("Contact")
    con.geometry('350x200')
    t = Label(con,text="Contact",font=('Helvetica 20 underline'))
    t.grid(row=0, column=0,pady=15)
 
    # Number1 
    c1Label = Label(con, text="Thane region : + 022 2542 1373",font=(20))
    c1Label.grid(row=1, column=0,padx=10)


    # Number2 
    c2Label = Label(con, text="Mumbai region : + 022 2542 1562",font=(20))
    c2Label.grid(row=2, column=0, padx=10)
    mainloop()



# main frame
myFrame = Frame(root,bd=2)
label_title = Label(myFrame,text = "Live Camera", font=('Helvitica', 40, 'bold'))
label_title.grid(padx=(1,2), column=1)

icon_1 = Image.open("icons/24.png")
icon_1 = icon_1.resize((70,70), Image.ANTIALIAS)
icon_1 = ImageTk.PhotoImage(icon_1)
label_icon_1 = Label(myFrame,image=icon_1)
label_icon_1.grid(row=0, pady=(1,2), column=0)

icon_spy = Image.open("icons/spa.png")
icon_spy = icon_spy.resize((180,180), Image.ANTIALIAS)
icon_spy = ImageTk.PhotoImage(icon_spy)
label_icon_spay = Label(myFrame,image=icon_spy)
label_icon_spay.grid(row=1, pady=(5,10), column=1)


#Record Button
icon_rec = Image.open("icons/recording.png")
icon_rec = icon_rec.resize((30,30), Image.ANTIALIAS)
icon_rec = ImageTk.PhotoImage(icon_rec)


btn_image = Button(myFrame, text=" VideoRecord", height=90, width=270, fg='black',font=('Helvitica',25, 'bold'), image=icon_rec, compound='left',command=record)
btn_image.grid(row=2,pady=(1,2),column=0)

#Monitor button
icon_rec1 = Image.open("icons/main.png")
icon_rec1 = icon_rec1.resize((30,30), Image.ANTIALIAS)
icon_rec1 = ImageTk.PhotoImage(icon_rec1)


btn_image1 = Button(myFrame, text=" Monitor", height=90, width=270, fg='black',font=('Helvitica',25, 'bold'), image=icon_rec1, compound='left')
btn_image1.grid(row=2,pady=(20,10),column=3)

#Website Button
icon_rec2 = Image.open("icons/web.png")
icon_rec2 = icon_rec2.resize((30,30), Image.ANTIALIAS)
icon_rec2 = ImageTk.PhotoImage(icon_rec2)


btn_image2 = Button(myFrame, text=" Website", height=90, width=270, fg='black',font=('Helvitica',25, 'bold'), image=icon_rec2, compound='left')
btn_image2.grid(row=3,pady=(20,10),column=3)

#Help Button
icon_rec3 = Image.open("icons/contact.png")
icon_rec3 = icon_rec3.resize((50,50), Image.ANTIALIAS)
icon_rec3 = ImageTk.PhotoImage(icon_rec3)


btn_image3 = Button(myFrame, text=" Support", height=90, width=270, fg='red',font=('Helvitica',25, 'bold'), image=icon_rec3, compound='left', command=support)
btn_image3.grid(row=3,pady=(20,10),column=0)


#Exit Button

exit_btn = Button(myFrame, text="Exit",command=root.quit, height=2, width=10, fg='red')
exit_btn.grid(row=4, column=1)


myFrame.pack()


root.mainloop()