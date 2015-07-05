__author__ = 'steve'
class Employee:
    'Common base class for all employees'
    empCount = 0
    'class variable value shared with all instances'

    def __init__(self, name, salary):
        'Special initialization method called when create new instance'
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        'we have another employee'

    def displayCount(self):
        """like other functions but always have 'self argument. This automatically added when calling function"""
        print("Total Employee {}" .format(Employee.empCount))

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

"This creates first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee {}" .format(Employee.empCount))

print("end")

