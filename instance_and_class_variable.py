class Company:
  Company_name = "google"
  Employees = 0

  def __init__(self, name, id):
    self.name = name
    self.id = id
    Company.Employees += 1

  def showdetails(self):
    print(
        f"The name of Employee: {self.name} id is {self.id} company name is {self.Company_name} eployees are {self.Employees} {Company.Employees}{Company.Company_name}"
    )


e1 = Company("shoaib khan", 1)
e1.showdetails()

e2 = Company("skj", 2)
e2.Company_name = "google pakistan"
e2.showdetails()

Company.Company_name = "apple"

e2 = Company("skj", 2)
e2.Company_name = "google pakistan"
e2.showdetails()
