class Employee:
    company = "google"

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(
            f"The name of Employee: {self.name} is {self.id} company is {self.company}"
        )

    #@classmethod #change the class variable
    def changeCompany(cls, newCompany):
        cls.company = newCompany


e1 = Employee("shoaib", 1)
e1.showDetails()
print(Employee.company)
e1.changeCompany("apple")
e1.showDetails()
print(Employee.company)
