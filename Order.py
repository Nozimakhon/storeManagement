
from Store import Store
from Customer import Customer
from Staff import Staff
from Product import Product
import datetime

class Order:
    def __init__(self, store, customer, staff, products=None, quantity=None):
        self.__store = store
        self.__customer = customer
        self.__staff = staff
        self.__products = products or {}
        self.__quantity = quantity or 0

    @property
    def store(self):
        return self.__store

    @property
    def customer(self):
        return self.__customer

    @property
    def staff(self):
        return self.__staff

    @property
    def products(self):
        return self.__products

    @property
    def quantity(self):
        return self.__quantity

    def addProduct(self, product):
        if product in self.products:
            self.__products[product] += 1
            self.__quantity += 1
        else:
            self.__products[product] = 1
            self.__quantity += 1

    # MARK: - Receipt

    def calculate_receipt(self, products):
        price = 0
        product_quantity = 0
        purchasing_points = 0

        for product in products:
            price += product.price * products[product]
            product_quantity += product.points * products[product]
            purchasing_points += products[product]
        
        return (price, product_quantity, purchasing_points)

    def generate_receipt_header(self):
        receipt_header = "\tWelcome to the Store Management System\n"\
            "\nStaff Name:\t{0}"\
            "\nCustomer ID:\t{1}\n\n"\
                .format(self.staff.name, self.customer.SSN)

        return receipt_header

    def generate_receipt_body(self):
        receipt_body = '\nProduct name\tProduct Code\t\tPrice\t\tQ'

        for product in self.products:
            receipt_body += '\n{0}\t\t{1}\t\t{2}\t\t{3}' \
                .format(product.name, product.productCode, product.price, self.products[product])
        
        return receipt_body

    def generate_receipt_footer(self, price, product_quantity, purchasing_points):
        receipt_footer = "\n\nTOTAL:\t\t{0}" \
                   "\n# ITEMS SOLD:\t{1}" \
                   "\nTotal Points:\t{2}\n" \
                   "\n\t\t***CUSTOMER COPY***".format(price, product_quantity, purchasing_points)

        return receipt_footer
    
    def generate_formatted_receipt(self):
        (price, purchasing_points, product_quantity) = self.calculate_receipt(self.products)
        self.customer.purchasing_points += purchasing_points

        receipt = self.generate_receipt_header()
        receipt += self.generate_receipt_body()
        receipt += self.generate_receipt_footer(price, product_quantity, purchasing_points)

        return receipt

