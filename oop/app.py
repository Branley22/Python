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


class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary


# giving employee1 a new instance of our Employee class.

employees = []
employees.append(Employee('Bran', 'Min', 78000))
employees.append(Employee('Mat', 'Hawk', 728000))
employees.append(Employee('Giggle', 'Chad', 128000))

for employee in employees:
    print(f"{employee.first_name} {employee.last_name}")
