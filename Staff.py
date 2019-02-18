
from Citizen import Citizen

class Staff(Citizen):
    def __init__(self, Id, SSN, name, address, jobTitle, salary):
        super().__init__(SSN, name, address)
        self.__id = Id
        self.__jobTitle = jobTitle
        self.__salary = salary

    @property
    def Id(self):
        return self.__id

    @property
    def jobTitle(self):
        return self.__jobTitle

    @property
    def salary(self):
        return self.__salary

    @Id.setter
    def Id(self, value):
        self.__id = value

    @jobTitle.setter
    def jobTitle(self, value):
        self.__jobTitle = value

    @salary.setter
    def salary(self, value):
        if not isinstance(value, float):
            raise TypeError("Salary must be float")
        self.__salary = value

    def __str__(self):
        return 'ID: {0} \nSSN: {1} \nName: {2} \nAddress: {3} \nJobTitle: {4} \nSalary: {5}' \
            .format(self.Id, self.SSN, self.name, self.address, self.jobTitle, self.salary)

