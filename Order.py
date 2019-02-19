
from Store import Store
from Customer import Customer
from Staff import Staff
from Product import Product
import datetime


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

    def printReceipt(self):

        date = datetime.datetime.now()

        receipt = "\tWelcome to {0}\n\t\tStaff: {1}\n\tCustomer ID: {2}\n\n" \
                  "\t\tRECEIPT\n\t\t{3}\n\t\t{4}\n\t\tST # {5}" \
            .format(self.store.storeName, self.staff.name, self.customer.SSN, \
                    date.date(), date.time(), self.store.Id)

        total_price = 0
        total_points = 0
        total_quantity = 0
        receipt += '\nProduct name\tProduct Code\t\tPrice\t\tQuantity\t\tPoints'
        for product in self.products:
            product_quantity = self.products[product]
            receipt += "\n{0}\t\t\t{1}\t\t{2}\t\t{3}\t\t{4}" \
                .format(product.name, product.productCode, product.price, product_quantity, product.points)
            total_price += product.price * product_quantity
            total_points += product.points * product_quantity
            total_quantity += product_quantity

        receipt += "\n\n\tTOTAL:\t{0}\n" \
                   "\t# ITEMS SOLD: {1}" \
                   "\n\tTotal Points: {2}\n" \
                   "\t\t***CUSTOMER COPY***".format(total_price, total_quantity, total_points)
        self.customer.purchasing_points += total_points

        return receipt




