def get_values(p):
    while True:
        try:
            value = int(input(p))
            return value
        except ValueError:
            print('Please enter a number')

class Employee:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def after_increment(self):
        return self.salary + (self.salary * (self.increment / 100))

print('--- Employee Data Entry System ---')
print('Type "stop" as the name to end the program.\n')

while True:
    n = input('Enter Employee name: ')
    if n.strip().lower() == "stop":
        print("\nExiting and saving all data... ")
        break

    s = get_values('Enter salary: ')
    i = get_values('Enter increment : ')

    emp = Employee(n, s, i)

    
    print(f'\nEmployee Recorded:')
    print(f'Employee name: {emp.name}')
    print(f'Salary after increment: {emp.after_increment}\n')

    # Append to file
    with open('employee_data.txt', 'a') as file:
        file.write(f"\n--- New Employee ---\n")
        file.write(f"Employee Name: {emp.name}\n")
        file.write(f"Base Salary: {emp.salary}\n")
        file.write(f"Increment: {emp.increment}%\n")
        file.write(f"Salary after increment: {emp.after_increment}\n")

    print('--- Ready for next entry ---\n')
