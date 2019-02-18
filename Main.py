
from tkinter import *
from Store import Store
from Customer import Customer
from Staff import Staff
from Product import Product
from Order import Order

if __name__ == "__main__":

    root = Tk()
    root.geometry("1000x500")  # specify fixed size of the window
    root.resizable(0,0)  # make the resizable = False

    frameTop = Frame(root)
    frameMiddle = Frame(root)
    frameList = Frame(root)

    welcome_Label = Label(frameTop, text="Welcome to the Store Management System", font=("Courier", 20))
    name_Label = Label(frameMiddle, text="Staff name", font=("Courier", 12))
    customerId_Label = Label(frameMiddle, text="Customer ID", font=("Courier", 12))
    addProducts_Label = Label(frameMiddle, text="Add more products", font=("Courier", 12))
    add_Button = Button(frameMiddle, text="+", bg="#386fe5", fg="white", width=8, font=("Arial", 12, "bold"))

    productName_Label = Label(frameList, text="Product Name", font=("Courier", 12))
    productCode_Label = Label(frameList, text="Product Code", font=("Courier", 12))
    price_Label = Label(frameList, text="Price", font=("Courier", 12))
    quantity_Label = Label(frameList, text="Quantity", font=("Courier", 12))
    points_Label = Label(frameList, text="Points", font=("Courier", 12))

    entry_Name = Entry(frameMiddle)
    entry_CustomerID = Entry(frameMiddle)

    name_Label.grid(row=0)
    customerId_Label.grid(row=1)
    entry_Name.grid(row=0, column=1)
    entry_CustomerID.grid(row=1, column=1)
    addProducts_Label.grid(row=2)
    add_Button.grid(row=2, column=1)

    productName_Label.grid(row=0)
    productCode_Label.grid(row=0, column=1)
    price_Label.grid(row=0, column=2)
    quantity_Label.grid(row=0, column=3)
    points_Label.grid(row=0, column=4)

    frameTop.pack(pady=10)  # padding by y-axis
    frameMiddle.pack(pady=10)
    frameList.pack(pady=10)
    welcome_Label.pack()




    root.mainloop()