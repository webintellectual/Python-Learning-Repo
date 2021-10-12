class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is unknown")
keet = Employee()
# keet.getSalary() equivalent to Employee.getSalary(keet)
keet.getSalary()