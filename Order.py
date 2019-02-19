import datetime

from Customer import Customer
from Product import Product
from Staff import Staff
from Store import Store

class Order:
    def __init__(self, store: Store, customer: Customer, staff: Staff, products: dict = {}, quantity=0):
        self.__store = store
        self.__customer = customer
        self.__staff = staff
        self.__products = products
        self.__quantity = quantity

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

    def add_product(self, product: Product, quantity=1):
        if product in self.products:
            self.__products[product] += quantity
            self.__quantity += quantity
        else:
            self.__products[product] = quantity
            self.__quantity += quantity

    def calculate_receipt(self, products):
        price = 0
        product_quantity = 0
        purchasing_points = 0

        for product in products:
            price += product.price * products[product]
            purchasing_points += product.points * self.products[product]
            product_quantity += self.products[product]

        
        return (price, product_quantity, purchasing_points)
    
    def generate_receipt_header(self):
        date = datetime.datetime.now()

        receipt_header = "Welcome to {0}\n"\
            "\nStaff Name: {1}"\
            "\nCustomer ID: {2}\n"\
            "\nDate: {3}"\
            "\nTime: {4}\n\n"\
                .format(self.store.storeName, self.staff.name, self.customer.SSN, date.date(), date.time())

        return receipt_header
    
    def generate_receipt_body(self):
        receipt_body = '\nProduct Name\tProduct Code\tPrice\tQuantity\tPoints'

        for product in self.products:
            receipt_body += '\n{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}' \
                .format(product.name, product.productCode, product.price, self.products[product], product.points)

        return receipt_body

    def generate_receipt_footer(self, price, product_quantity, purchasing_points):
        receipt_footer = "\n\nTOTAL: {0} $" \
                   "\n# ITEMS SOLD: {1}" \
                   "\nTotal Points: {2}\n" \
                   "\n***CUSTOMER COPY***".format(price, product_quantity, purchasing_points)

        return receipt_footer
    
    def generate_receipt(self):
        (price, product_quantity, purchasing_points) = self.calculate_receipt(self.products)
        self.customer.purchasing_points += purchasing_points

        receipt = self.generate_receipt_header()
        receipt += self.generate_receipt_body()
        receipt += self.generate_receipt_footer(price, product_quantity, purchasing_points)

        return receipt
