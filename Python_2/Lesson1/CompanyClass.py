"""Code from the class"""
class Company:

    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def hire(self, employee, position, salary):

        if employee in self.employee_list:
            raise Exception('{} is already working in {}'.format(employee, self))

        elif employee.company is not None:
            raise Exception('{} can not hire {}. Already employed'.format(self, employee))

        print('{} is hiring {}'.format(self, employee))

        employee.position = position
        employee.salary = salary
        employee.company = self

        self.employee_list.append(employee)

    def fire(self, employee, reason = None, has_left = False):

        if employee.company.company_id != self.company_id:
            raise Exception('{} can not fire {}. Not employed in this company'.format(self, employee))

        resignation_message = ""
        if has_left == True:
            resignation_message = "The employee {} has left {} voluntarily".format(employee, self)
        else:
            resignation_message = "The employee {} was fired by {}.".format(employee, self)
        
        if reason is not None:
            resignation_message += ", because {} ".format(reason)
            
        print(resignation_message)
        

        self.employee_list.remove(employee)

        employee.company = None
        employee.salary = None
        employee.position = None

    def get_salary_costs(self):
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

    def __str__(self):
        return self.name


class Employee:
    
    def __init__(self, first_name, last_name, email, embg):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.embg = embg
        Employee.validate_embg(embg)
        
        self.salary = None
        self.position = None
        self.company = None

    def full_name(self):
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name

    def __str__(self):
        return self.full_name()
    
    def resign(self):
        if self.company is None:
            raise Exception ("Cannot resign from unemployment :)")
        else:
            reason = (input("Please provide a reason for your resignation: "))
            self.company.fire(self, reason, True)
            
    @staticmethod       
    def validate_embg (embg):
        if type(embg) != str:
            raise Exception("Only input in string format is acceptable.")
    
        if len(embg) != 13: 
            raise Exception ("EMBG consist of 13 digits.")
    
        if embg.isdigit() == False:
            raise Exception ("EMBG contains only numbers")
        
import datetime
        
class Offer:
    
    def __init__(self, company, employee, position, salary):
        self.company = company
        self.employee = employee
        self.position = position
        self.salary = salary
        self.date = datetime.datetime.now()
        self.response = None
        
    def __str__(self):
        return " Company: {} \n Employee: {} \n Position: {} \n Salary: {} \n Offer send date: {} \n Response: {}".format(self.company, self.employee, self.position, self.salary, self.date, self.response)


print('### CODE EXECUTION STARTS HERE ###')

# Valid EMBG
semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu XXX", "1234")
petko = Employee("Petko", "Petkov", "petko@mailinator.com", "0111992450015")  
semos.hire(petko, 'Developer', 30000)
petko.resign()

# Invalid EMBG
semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu XXX", "1234")
stanko = Employee("Stanko", "Stankov", "stanko@mailinator.com", "140998945001")  
semos.hire(stanko, 'Developer', 30000)
stanko.resign()

# semos = Company("Semos Edukacija", "Kuzman Josifovski Pitu XXX", "1234")
# quipu = Company('Quipu', 'Ilindenska XXX', "3456")

# petko = Employee("Petko", "Petkov", "petko@mailinator.com")
# janko = Employee("Janko", "Jankov", "janko@mailinator.com")
# stanko = Employee("Stanko", "sankov", "stanko@mailinator.com")

# semos.hire(petko, 'Developer', 30000)
# quipu.hire(janko, 'Developer', 40000)
# semos.hire(stanko, 'Accountant', 50000)

# print('SEMOS LIST', semos.employee_list)
# print('QUIPU LIST', quipu.employee_list)

# for emp in semos.employee_list:
#    print('SEMOS EMP', emp)

# for emp in quipu.employee_list:
#    print('QUIPU EMP', emp)


# print(semos)
# print(quipu)

# print(petko.__dict__)
# print(janko.__dict__)
# print(stanko.__dict__)


# print('TSC:',semos.get_salary_costs())


# semos.fire(stanko)

# print('SEMOS LIST 2', semos.employee_list)

# print(stanko.__dict__)

# print('TSC:',semos.get_salary_costs())
# print('TSC:',quipu.get_salary_costs())
