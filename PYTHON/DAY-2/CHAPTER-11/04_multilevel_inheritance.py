class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing....")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckily breathing...")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(Self):
        print(f"No salary to programmers")

    def takeBreath(self):
        print("I am an Programmer so I am  breathing++...")


p = Person()
p.takeBreath()
print(p.country)
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
