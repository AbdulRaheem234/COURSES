class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")
harry = Employee()
harry.salary = 100000
harry.getSalary()
# harry.getSalary(harry)
