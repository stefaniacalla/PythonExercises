'''Write a Python class Employee with attributes like emp_id, emp_name, 
emp_salary, and emp_department 
and methods like calculate_emp_salary, emp_assign_department, 
and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, 
which is the number of hours worked by the employee. 
If the number of hours worked is more than 50, 
the method computes overtime and adds it to the salary. 
Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))'''


from typing import Any, Dict, List



class Employee:  
    def __init__(self,emp_id, emp_name, emp_department= None):
        self.emp_id: str = emp_id
        self.emp_name: str = emp_name
        self.emp_department: str = emp_department
        self.emp_salary: float = 0.0

    def assign_department (self, new_dep:str):
        self.emp_department= new_dep
        return self.emp_department
    
    def calculate_emp_salary (self, salary:float, hours_worked:float):
        overtime=0.0
        overtime_am=0.0
        hours_no_ov=hours_worked
        if(hours_worked>50.0):
            overtime=hours_worked-50
            overtime_am=(overtime* (salary/50))
            hours_no_ov=50
            self.emp_salary=(salary * hours_no_ov)+overtime_am
        else:
            self.emp_salary=(salary * hours_no_ov)
        return self.emp_salary

    def print_employee_details(self, emp_id):
        print(f"The employee {emp_id}: {self.emp_name} works in {self.emp_department} department with a salary of {self.emp_salary} euro.")


emp1=Employee("1","ADAMS")
emp1.print_employee_details("1")
emp1.assign_department("ACCOUNTING")
emp1.print_employee_details("1")
emp1.calculate_emp_salary( 10.0, 40.0)
emp1.print_employee_details("1")
emp1.assign_department("SALES")
emp1.calculate_emp_salary( 10.0, 65.5)
emp1.print_employee_details("1")