
from Citizen import Citizen

class Customer(Citizen):
    def __init__(self, SSN, name, address, purchasing_points, tel, memberships=[]):
        super().__init__(SSN, name, address)
        self.__purchasing_points = purchasing_points
        self.__tel = tel
        self.__memberships = memberships

    @property
    def purchasing_points(self):
        return self.__purchasing_points

    @property
    def tel(self):
        return self.__tel

    @property
    def memberships(self):
        return self.__memberships

    @purchasing_points.setter
    def purchasing_points(self, value):
        if not isinstance(value, int):
            raise TypeError("Points must be int")
        self.__purchasing_points = value

    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("Tel must be int")
        self.__tel = value

    @memberships.setter
    def memberships(self, value):
        if not isinstance(value, str):
            raise TypeError("Memberships must be string")
        self.__memberships = value

    def __str__(self):
        return 'SSN: {0} \nName: {1} \nAddress: {2} \nPurchasing Points: {3} \nTel: {4} \nMemberships: {5}' \
            .format(self.SSN, self.name, self.address, self.purchasing_points, self.tel, self.memberships)

