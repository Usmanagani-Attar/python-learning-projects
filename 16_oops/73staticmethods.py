class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
#instance method
    def get_info(self):
        print(f"{self.name} = {self.position}")
    
    #static method
    @staticmethod
    def is_valid(position):
        valid=["Manager","Cashier","cook"]
        return position in valid

employee2=Employee("sam","CM")       #If static methid is their no need to call it
employee1= Employee("abd","head")
employee3=Employee("dev","faculty")

print(Employee.is_valid("trainer"))
print(Employee.is_valid("cook"))
print(Employee.is_valid("shopkeeper"))
print(Employee.is_valid("Cashier"))
print(Employee.is_valid("checker"))

print()

employee1.get_info()
employee2.get_info()
employee3.get_info()