class Employee:
    salary = 1000
    increament = 1.5

    @property
    def salaryAfterIncreament(self):
        return self.salary * self.increament

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self, sai):
        self.increament = sai/self.salary


e = Employee()
print(e.salaryAfterIncreament)
print(e.increament)
e.salaryAfterIncreament = 2000
print(e.increament)
