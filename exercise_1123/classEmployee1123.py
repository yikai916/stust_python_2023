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
        print('Name:',self.emp_name)
        print('ID:',self.emp_id)
        print('Salary:',self.emp_salary)
        print('Department:',self.emp_department)
        print('----------------------')



employee1 = employee('E7876','Adams',50000,'Accounting')
employee2 = employee('E7499','Jones',45000,'Research')
employee3 = employee('E7900','Martin',50000,'Sales')
employee4 = employee('E7698','Smith',55000,'Operations')

employee.print_emp_detail(employee1)
#employee.calculate_emp_salary(employee1,40)
employee.print_emp_detail(employee2)
#employee.calculate_emp_salary(employee2,50)
employee.print_emp_detail(employee3)
#employee.calculate_emp_salary(employee3,60)
employee.print_emp_detail(employee4)
#employee.calculate_emp_salary(employee4,70)
#employee.emp_assign_department(employee4,'Sales')


