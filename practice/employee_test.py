import os
from csv import reader
from collections import namedtuple
from payroll_test import *
employees = {}
path = os.path.dirname(__file__)

def load_employees():
    #list contains Employee objects
    #Hourly = 1
    #Salary = 2
    #Commissioned = 3
    #Direct Deposit = 1
    #Mail Method = 2
    with open(path + '/employees.csv', 'r') as f:
        #Get first line of csv and use it to set up named tuple
        csv_reader = reader(f)
        emps = namedtuple("Employee", next(csv_reader))
        #._make() is used to return a namedtuple() from the iterable passed as argument
        for emp in map(emps._make, csv_reader):
            if emp.Classification == '1':
                hourly = Hourly(emp.Hourly)
                employees[emp.ID] = Employee(emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, hourly, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].PayMethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].PayMethod = mail
            elif emp.Classification == '2':
                salary = Salaried(emp.Salary)
                employees[emp.ID] = Employee(emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, salary, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].PayMethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].PayMethod = mail
            elif emp.Classification == '3':
                commission = Commissioned(emp.Salary, emp.Commission)
                employees[emp.ID] = Employee(emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, salary, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].PayMethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].PayMethod = mail
        
                    
def find_employee_by_id(id):
    #loop through employee list.  Check employee.id and return Employee object
    if id in employees:
        return employees[id]
    return -1

def main():
    load_employees()

if __name__ == main():
    main()