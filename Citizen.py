class Citizen:
    def __init__(self, SSN, name, address):
        self.__ssn = SSN
        self.__name = name
        self.__address = address

    @property
    def SSN(self):
        return self.__ssn

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @SSN.setter
    def SSN(self, value):
        self.__ssn = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        self.__name = value

    @address.setter
    def address(self, value):
        self.__address = value