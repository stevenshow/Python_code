import os
import shutil
from collections import namedtuple
from csv import reader

from payroll_test import *

path = os.path.dirname(__file__)
PAY_LOGFILE = '/paylog.txt'
employees = {}


def load_employees():
    # list contains Employee objects
    # Hourly = 1
    # Salary = 2
    # Commissioned = 3
    # Direct Deposit = 1
    # Mail Method = 2def process_timecards():
    pass
    with open(path + '/employees.csv', 'r') as f:
        # Get first line of csv and use it to set up named tuple
        csv_reader = reader(f)
        emps = namedtuple("Employee", next(csv_reader))
        # ._make() is used to return a namedtuple() from the iterable passed as argument
        for emp in map(emps._make, csv_reader):
            if emp.Classification == '1':
                hourly = Hourly(emp.Hourly)
                employees[emp.ID] = Employee(
                    emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, hourly, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(
                        employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].paymethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].paymethod = mail
            elif emp.Classification == '2':
                salary = Salaried(emp.Salary)
                employees[emp.ID] = Employee(
                    emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, salary, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(
                        employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].paymethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].paymethod = mail
            elif emp.Classification == '3':
                commission = Commissioned(emp.Salary, emp.Commission)
                employees[emp.ID] = Employee(
                    emp.ID, emp.Name, emp.Address, emp.City, emp.State, emp.Zip, commission, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(
                        employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].paymethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].paymethod = mail


def find_employee_by_id(id):
    # loop through employee list.  Check employee.id and return Employee object
    if id in employees:
        return employees[id]
    return -1


def process_timecards():
    with open(path + '/timecards.txt', 'r') as f:
        csv_reader = reader(f)
        for hour_list in csv_reader:
            id = hour_list.pop(0)
            employees[id].classification.timecards = hour_list


def process_receipts():
    with open(path + '/receipts.txt', 'r') as f:
        csv_reader = reader(f)
        for receipt_list in csv_reader:
            id = receipt_list.pop(0)
            employees[id].classification.receipts = receipt_list


def run_payroll():
    if os.path.exists(path + PAY_LOGFILE):
        os.remove(path + PAY_LOGFILE)
    for emp in employees:
        employees[emp].issue_payment()


def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

    # Save copy of payroll file; delete old file
    shutil.copyfile(path + PAY_LOGFILE, 'paylog_old.txt')
    if os.path.exists(path + PAY_LOGFILE):
        os.remove(path + PAY_LOGFILE)

    # Change Karina Gay to Salaried and MailMethod by changing her Employee object:
    emp = find_employee_by_id('688997')
    emp.make_salaried(45884.99)
    emp.mail_method()
    emp.issue_payment()

    # Change TaShya Snow to Commissioned and DirectMethod; add some receipts
    emp = find_employee_by_id('522759')
    emp.make_commissioned(50005.50, 25)
    emp.direct_method('30417353-K', '465794-3611')
    clas = emp.classification
    clas.add_receipt(1109.73)
    clas.add_receipt(746.10)
    emp.issue_payment()

    # Change Rooney Alvarado to Hourly; add some hour entries
    emp = find_employee_by_id('165966')
    emp.make_hourly(21.53)
    clas = emp.classification
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    clas.add_timecard(8.0)
    emp.issue_payment()


if __name__ == main():
    main()
