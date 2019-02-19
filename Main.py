
from tkinter import *
import tkinter.messagebox

from Customer import Customer
from Order import Order
from Product import Product
from Staff import Staff
from Store import Store

if __name__ == "__main__":
    name_index = 0
    code_index = 1
    price_index = 2
    quantity_index = 3
    points_index = 4

    row_counter = 1
    products = []

    #FUNCTIONS
    def list_products():  # function to add new entries for adding product information
        global row_counter
        row_counter = row_counter + 1
        entry_ProductName = Entry(frameList)
        entry_ProductCode = Entry(frameList)
        entry_Price = Entry(frameList)
        entry_Quantity = Entry(frameList)
        entry_Points = Entry(frameList)
        entry_ProductName.grid(row=row_counter, column=0, padx=20, pady=10)
        entry_ProductCode.grid(row=row_counter, column=1, padx=20, pady=10)
        entry_Price.grid(row=row_counter, column=2, padx=20, pady=10)
        entry_Quantity.grid(row=row_counter, column=3, padx=20, pady=10)
        entry_Points.grid(row=row_counter, column=4, padx=20, pady=10)
        if not are_product_cells_empty():
            products.append([entry_ProductName, entry_ProductCode, entry_Price, entry_Quantity, entry_Points])
        else:
            tkinter.messagebox.showinfo("Warning!", "Firstly fill all the gaps, then add new item!")
    
    def are_product_cells_empty():
        for entries in products:
            if is_empty(entries):
                return True

        return False
    
    def is_empty(entries: [Entry]):
        is_empty_field = False
        
        for entry in entries:
            if entry.get() == "":
                is_empty_field = True
        
        return is_empty_field

    def are_product_cells_valid():
        for entries in products:
            if not is_valid(entries):
                return False
        
        return True
    
    def is_valid(entries: [Entry]):
        try:
            float(entries[2].get())
            int(entries[3].get())
            int(entries[4].get())
        except (ValueError, TypeError):
            return False
        else:
            return True
    
    def get_product(entries: [Entry]):
        product = Product(
            entries[name_index].get(), 
            entries[code_index].get(), 
            float(entries[price_index].get()), 
            int(entries[points_index].get())
        )

        return product

    def printing_receipt():
        # Dummy Data    
        store = Store(111, "Nozima's Store", "Zaytun street,45", 998908889900)
        staff = Staff(1234, 2222, entry_Name.get(), "blabla", "manager", 1234)
        customer = Customer(entry_CustomerID.get(), "ban", "ddd", 122, 23232323, ["VIP"])
        order = Order(store, customer, staff)

        if not are_product_cells_empty():
            if are_product_cells_valid():
                for entries in products:
                    product = get_product(entries)
                    quantity = int(entries[quantity_index].get())
                    order.add_product(product, quantity)

                # UI
                t = Toplevel()
                t.wm_title("Receipt")
                labeltest = Label(t, text=str(order.printReceipt()), font=("Courier", 12))
                labeltest.pack(side="top", fill="both", expand=True, padx=100, pady=100)
            else:
                tkinter.messagebox.showinfo("Warning!", "Price must be FLOAT or INTEGER\nPoints, Quantity - MUST be INTEGER")
        else:
            tkinter.messagebox.showinfo("Warning!", "Firstly fill all the gaps, then you can Print!")

    #Tkinter window
    root = Tk()
    root.geometry("1000x500")  # specify fixed size of the window
    root.resizable(0,0)  # make the resizable = False

    # FRAMES
    frameTop = Frame(root)
    frameMiddle = Frame(root)
    frameList = Frame(root)
    frameBottom = Frame(root)

    #ENTRY
    entry_Name = Entry(frameMiddle)
    entry_CustomerID = Entry(frameMiddle)

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
    print_Button = Button(frameBottom, text="Print", bg="#386fe5", fg="white", width=8, font=("Courier", 12, "bold"),
                          command=printing_receipt)
    close_Button = Button(frameBottom, text="Close", bg="#386fe5", fg="white", width=8, font=("Courier", 12, "bold"),
                          command= frameBottom.quit)

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