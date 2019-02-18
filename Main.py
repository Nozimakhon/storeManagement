
from tkinter import *
from Store import Store
from Customer import Customer
from Staff import Staff
from Product import Product
from Order import Order

if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x500")

    frameTop = Frame(root)
    frame2 = Frame(root)
    welcome_Label = Label(frameTop, text="Welcome to the Store Management System", bg="#93cbbd")
    welcome_Label.config(font=("Courier", 20))
    name_Label = Label(frame2, text="Staff name")
    customerId_Label = Label(frame2, text="Customer ID")

    entry_Name = Entry(frame2)
    entry_CustomerID = Entry(frame2)

    name_Label.grid(row=0)
    customerId_Label.grid(row=1)
    entry_Name.grid(row=0, column=1)
    entry_CustomerID.grid(row=1, column=1)

    frameTop.pack()
    frame2.pack()
    welcome_Label.pack(fill=X)

    # topFrame = Frame(root)
    # topFrame.pack()
    #
    # bottomFrame = Frame(root)
    # bottomFrame.pack(side=BOTTOM)
    #
    # button1 = Button(topFrame, text="Button1", fg="red")
    # button2 = Button(topFrame, text="Button2", fg="blue")
    # button3 = Button(topFrame, text="Button3", fg="green")
    # button4 = Button(bottomFrame, text="Button4", fg="purple")
    #
    # button1.pack(side=LEFT)
    # button2.pack(side=LEFT)
    # button3.pack(side=LEFT)
    # button4.pack(side=RIGHT)

    root.mainloop()