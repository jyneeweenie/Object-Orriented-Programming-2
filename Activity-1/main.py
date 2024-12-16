class Employee:
    # initializing (Constructor)
    def __init__(self):
        print('Employee created')
    # Deleting (Destructor)
    def __del__(self):
        print('Distructor called, Employee deleted')
obj = Employee()
del obj