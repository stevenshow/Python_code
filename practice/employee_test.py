import os
from csv import reader
from collections import namedtuple
from payroll import *
employees = {}
path = os.path.dirname(__file__)

def load_employees():
    #list contains Employee objects
    #Hourly = 1
    #Salary = 2
    #Commissioned = 3
    with open(path + '/employees.csv', 'r') as f:
        #Get first line of csv and use it to set up named tuple
        csv_reader = reader(f)
        emps = namedtuple("Employee", next(csv_reader))
        #._make() is used to return a namedtuple() from the iterable passed as argument
        for emp in map(emps._make, csv_reader):
            if emp.Classification == '1':
                employees[emp.ID] = Employee(emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, emp.Classification, emp.PayMethod)
                Hourly()
        #print(employees['688997'].name) How to access employee data from dictionary
                    
        

def main():
    load_employees()
    


if __name__ == main():
    main()