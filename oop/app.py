# oop is taking data and asscoiating behavior with it.
# employee1 = {"first_name": "Bran", "last_name": "Min", "salary": 78000}
# employee2 = {"first_name": "Val", "last_name": "Min", "salary": 88000}
# employee3 = {"first_name": "Neo", "last_name": "Min", "salary": 28000}
# employee4 = {"first_name": "Abra", "last_name": "Min", "salary": 38000}

# employees = [employee1, employee2, employee3, employee4]

# for employee in employees:
#     print(
#         f"{employee['first_name']} {employee['last_name']} - {employee['salary']}")

# employee4['last_name'] = 'Carl'

# for employee in employees:
#     print(
#         f"{employee['first_name']} {employee['last_name']} - {employee['salary']}")

class Department():

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)


class Employee():

    def __init__(self, first_name, last_name, salary, department, middle_name=None):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.middle_name = middle_name
        self.department = department
        department.add_employee((self))

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def increase_salary_by_percentage(self, percentage):
        if isinstance((percentage), float):
            if (percentage >= .8) and (percentage <= 1.1):
              # salary cannot change by less than .8 or more than 1.1
                self.salary = self.salary * percentage

    def __str__(self):
        return self.full_name()

    def __repr__(self):
        return f"{self.first_name[0]}. {self.last_name}"


department_a = Department(('Legal'), '104C')

employee_a = Employee('Bran', 'Min', 78000, department_a)
employee_b = Employee('Mat', 'Hawk', 138000, department_a)

first_employee_salary = department_a.employees[0].salary

# giving employee1 a new instance of our Employee class.
# employees = []
# employees.append(Employee('Bran', 'Min', 78000))
# employees.append(Employee('Mat', 'Hawk', 728000, 'Eli'))
# employees.append(Employee('Giggle', 'Chad', 128000))

# for employee in employees:
#     if employee.first_name == 'Bran' and employee.last_name == 'Min':
#         employee.increase_salary_by_percentage((1.02))
#         print(employee.salary)
