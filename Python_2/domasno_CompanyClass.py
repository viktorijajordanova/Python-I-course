class Company:

    def __init__(self, name, address, company_id):

        self.address = address
        self.name = name
        self.company_id = company_id
        self.employee_list = []

    def hire(self, employee, offer):

        if employee in self.employee_list:
            print(f"{employee} is already working in {self.name}")
            #raise Exception(f"{employee} is already working in {self.name}")
        elif employee.company is not None:
            print(f"{self.name} cannot hire {employee}. Already employed in {employee.company}")
            #raise Exception(f"{self} cannot hire {employee}. Already employed")
        else:
            if employee.response(offer, self) == True:

                employee.company = self.name
                employee.salary = offer.salary
                employee.position = offer.position
                employee.company_id = self.company_id
                print(f"{self.name} is hiring {employee} as {employee.position} for salary: {employee.salary}")
                self.employee_list.append(employee)

            else:
                print(f"{employee} has rejected the offer from {self.name} as {offer.position} for salary: {offer.salary}")


    def fire(self, employee):

        if employee.company_id != self.company_id:
            print(f'{self.name} cannot fire {employee}. Not employed in this company.')
            #raise Exception(f'{self.name} cannot fire {employee}. Not employed in this company.')
        else:
            print(f'{self.name} is firing {employee}')

            self.employee_list.remove(employee)

            employee.position = None
            employee.salary = None

    def salary_costs(self):
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

#-----------------------------------------------------------------------------------------------------------------

class Employee:

    minimum_pay = 14000
    def __init__(self, first_name, last_name, email, company_id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.company_id = company_id

        self.salary = None
        self.position = None
        self.company = None

        self.embg = input(f"Vnesi EMBG za {self.full_name()}: ")

        while True:
            if self.validate_embg() == True:
                break
            self.embg = input("Vneseniot EMBG e nevaliden. Obidi se potorno: ")


    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name

    def yearly_pay(self):
        return self.minimum_pay * 12

    def __str__(self):
        return self.full_name()

    def response(self, offer, company):
        answer = input(f'Job offer for {self.full_name()}:\nCompany: {company.name}\nSalary: {offer.salary}\nPosition: {offer.position}\nDo you accept this offer? Y/N\n')
        if answer == 'y':
            return True
        else:
            return False

    def validate_embg(self):

        #DDMMYYYRRBBBK

        embg = int(self.embg)

        if not len(self.embg) == 13 or embg == False:
            #print("FALSE")
            return False
        else:
            j = []
            for i in self.embg:
                j.append(int(i))
            v = 11 - ((7*(j[0]+j[6])+6*(j[1]+j[7])+5*(j[2]+j[8])+4*(j[3]+j[9])+3*(j[4]+j[10])+2*(j[5]+j[11]))%11)
            return v == j[12]  #vrakja True ili False

    def quit(self, company):

        if  self.company_id != company.company_id:
            print(f'{self.full_name()} cannot quit {company.name}. Not employed in this company.')
            #raise Exception(f'{self.name} cannot fire {employee}. Not employed in this company.')
        else:
            print(f'{self.full_name()} is quiting {company.name}')

            company.employee_list.remove(self)

            self.position = None
            self.salary = None
            self.company_id = None


#------------------------------------------------------------------------------------------------------------

class Offer:

    def __init__(self, salary, position):
        self.salary = salary
        #self.company = company.name
        self.position = position


#--------------------------------------------------------------------------------------------------------------

#Companies
seavus = Company("SEAVUS", 'ilindenska', 152)
semos = Company("SEMOS", "partizanska", 222)

#Potential employees
stanko = Employee("Stanko", 'Stankov', 'stanko1@majmunce.com')
petko = Employee("Petko", "Petkovski", 'petko@email.com')
rajko = Employee("Rajko", "Zinzifov", "rajko@mail.com")

#Offers
offer1 = Offer(20000,  "IT")
offer2 = Offer(30000,  "QA")

#Company Job Offers
semos.hire(stanko, offer1)
semos.hire(rajko, offer2)
seavus.hire(petko, offer2)
semos.hire(petko, offer2)

#Employee quiting
stanko.quit(semos)

#Company firing
semos.fire(petko)

