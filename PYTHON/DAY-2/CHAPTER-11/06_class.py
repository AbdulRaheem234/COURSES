class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

    # def changesSalary(self, sal):
    #     self.__class__.salary = sal
    
    @classmethod
    def changesSalary(cls, sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changesSalary(455)
print(e.salary)
print(Employee.salary)
