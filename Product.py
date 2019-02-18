class Product:
    def __init__(self, name, productCode, price, points):
        self.__name = name
        self.__productCode = productCode
        self.__price = price
        self.__points = points

    @property
    def productCode(self):
        return self.__productCode

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def points(self):
        return self.__points

    @productCode.setter
    def productCode(self, value):
        self.__productCode = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        self.__name = value

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be float")
        self.__price = value

    @points.setter
    def points(self, value):
        if not isinstance(value, int):
            raise TypeError("Points must be integer")
        self.__points = value

    def __str__(self):
        return 'Product Code: {0} \nName: {1} \nPrice: {2} \nPoints: {3}' \
            .format(self.name, self.productCode, self.price, self.points)
