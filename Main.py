
from tkinter import *
from Store import Store
from Customer import Customer
from Staff import Staff
from Product import Product
from Order import Order

if __name__ == "__main__":

    row_counter = 1

    def list_products():  # function to add new entries for adding product information
        global row_counter
        row_counter = row_counter + 1
        entry_ProductName = Entry(frameList).grid(row=row_counter, column=0, padx=20, pady=10)
        entry_ProductCode = Entry(frameList).grid(row=row_counter, column=1, padx=20, pady=10)
        entry_Price = Entry(frameList).grid(row=row_counter, column=2, padx=20, pady=10)
        entry_Quantity = Entry(frameList).grid(row=row_counter, column=3, padx=20, pady=10)
        entry_Points = Entry(frameList).grid(row=row_counter, column=4, padx=20, pady=10)

    root = Tk()
    root.geometry("1000x500")  # specify fixed size of the window
    root.resizable(0,0)  # make the resizable = False


    # FRAMES
    frameTop = Frame(root)
    frameMiddle = Frame(root)
    frameList = Frame(root)
    frameBottom = Frame(root)

    #LABELS
    welcome_Label = Label(frameTop, text="Welcome to the Store Management System", font=("Courier", 20))
    name_Label = Label(frameMiddle, text="Staff name", font=("Courier", 12))
    customerId_Label = Label(frameMiddle, text="Customer ID", font=("Courier", 12))
    addProducts_Label = Label(frameMiddle, text="Add more products", font=("Courier", 12))

    productName_Label = Label(frameList, text="Product Name", font=("Courier", 12))
    productCode_Label = Label(frameList, text="Product Code", font=("Courier", 12))
    price_Label = Label(frameList, text="Price", font=("Courier", 12))
    quantity_Label = Label(frameList, text="Quantity", font=("Courier", 12))
    points_Label = Label(frameList, text="Points", font=("Courier", 12))

    #BUTTONS
    add_Button = Button(frameMiddle, text="+", bg="#386fe5", fg="white", width=8, font=("Arial", 12, "bold"),
                        command=list_products)
    print_Button = Button(frameBottom, text="Print", bg="#386fe5", fg="white", width=8, font=("Courier", 12, "bold"))
    close_Button = Button(frameBottom, text="Close", bg="#386fe5", fg="white", width=8, font=("Courier", 12, "bold"))
    entry_Name = Entry(frameMiddle)
    entry_CustomerID = Entry(frameMiddle)

    #GRID for middle frame
    name_Label.grid(row=0, pady=5)
    customerId_Label.grid(row=1, pady=5)
    entry_Name.grid(row=0, column=1)
    entry_CustomerID.grid(row=1, column=1)
    addProducts_Label.grid(row=2, pady=5)
    add_Button.grid(row=2, column=1)

    #GRID for list frame
    productName_Label.grid(row=0)
    productCode_Label.grid(row=0, column=1)
    price_Label.grid(row=0, column=2)
    quantity_Label.grid(row=0, column=3)
    points_Label.grid(row=0, column=4)



    #scrollbar = Scrollbar(frameList)
    #scrollbar.grid(row=0, column=5, sticky =N+S)
    #scrollbar.config(command=frameList.yview)
    #scrollbar.pack(side=RIGHT, fill=Y)


    #PACKing
    frameTop.pack(pady=10)  # padding by y-axis
    frameMiddle.pack(pady=10)

    frameList.pack(pady=10)
    frameBottom.pack(pady=10)
    welcome_Label.pack()
    print_Button.pack(side=LEFT, padx=50)
    close_Button.pack(side=LEFT)


    #callig functions
    list_products()
    root.mainloop()