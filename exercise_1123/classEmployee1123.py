class employee:
    def __init__(self,id,name,salary,department):
        self.emp_id = id
        self.emp_name = name
        self.emp_salary = salary
        self.emp_department = department

    def calculate_emp_salary(self,worked_hours):
        if worked_hours >50:
            overtime =worked_hours-50
            overtime_amount = overtime * (self.emp_salary / 50)
            worked_amount = self.emp_salary + overtime_amount
            print(worked_amount)
            return worked_amount
        else:
            print(self.emp_salary)
            return self.emp_salary
    
    def emp_assign_department(self,assign_department):
        self.emp_department = assign_department
        print(self.emp_department)

    def print_emp_detail(self):
        print(self.emp_name,self.emp_id,self.emp_salary,self.emp_department)

employee1 = employee('E7876','ADAMS',50000,'ACCOUNTING')
employee2 = employee('E7499','JONES',45000,'RESEARCH')
employee3 = employee('E7900','MARTIN',50000,'SALES')
employee4 = employee('E7698','SMITH',55000,'OPERATIONS')

# employee.print_emp_detail(employee1)
# employee.calculate_emp_salary(employee1,40)
# employee.print_emp_detail(employee2)
# employee.calculate_emp_salary(employee2,50)
# employee.print_emp_detail(employee3)
# employee.calculate_emp_salary(employee3,60)
employee.print_emp_detail(employee4)
employee.calculate_emp_salary(employee4,70)
employee.emp_assign_department(employee4,'SALES')


