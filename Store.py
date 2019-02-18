# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 21:32:50 2019

@author: Nozima
"""


class Store:
    def __init__(self, Id, storeName, address, tel):
        self.__id = Id
        self.__storeName = storeName
        self.__address = address
        self.__tel = tel

    @property
    def Id(self):
        return self.__id

    @Id.setter
    def Id(self, value):
        self.__id = value

    @property
    def storeName(self):
        return self.__storeName

    @storeName.setter
    def storeName(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        self.__storeName = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value):
        if not isinstance(value, int):
            raise TypeError("Tel must be int")
        self.__tel = value

    def __str__(self):
        return 'ID: {0} \nName: {1} \nAddress: {2} \nTel: {3}'.format(self.Id, self.storeName, self.address, self.tel)
