class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by: Php{amount:.2f}. New salary: Php{self.salary:.2f}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: Php{self.salary:.2f}")

# Create an employee
employee = Employee(name="John Pakidua", position="Aerospace Engineer", salary=75000)

# Give the employee a raise
employee.give_raise(5000)  # Increase salary

# Display employee details
employee.display_employee()