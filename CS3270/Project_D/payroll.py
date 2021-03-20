'''Loads employees from CSV file.  Processes them and uses the receipts.txt
and the timecards.txt to then run payroll and write their pay to a file.
Created by: Steven Schoebinger 03/10/2021'''
import os
from abc import ABCMeta
from collections import namedtuple
from csv import reader

# pylint: disable=invalid-name
path = os.path.dirname(__file__)
PAY_LOGFILE = '/paylog.txt'
employees = {}


class Employee:
    '''Generic docstring'''

    def __init__(self, id, name, address, city, state, zipcode, classification, paymethod):
        '''Generic docstring'''
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
        self.paymethod = paymethod

    def make_hourly(self, hourly_rate):
        '''Generic docstring'''
        self.classification = Hourly(hourly_rate)

    def make_salaried(self, salary):
        '''Generic docstring'''
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        '''Generic docstring'''
        self.classification = Commissioned(salary, rate)

    def mail_method(self):
        '''Generic docstring'''
        self.paymethod = MailMethod(self)

    def direct_method(self, route, account):
        '''Generic docstring'''
        self.paymethod = DirectMethod(self, route, account)

    def issue_payment(self):
        '''Generic docstring'''
        pay = 0.0
        pay = "{:.2f}".format(self.classification.compute_pay())
        self.paymethod.issue(pay)


class classification(metaclass=ABCMeta):
    '''Generic docstring'''

    def compute_pay(self):
        '''Generic docstring'''


class Salaried(classification):
    '''Generic docstring'''

    def __init__(self, salary):
        '''Generic docstring'''
        self.salary = salary

    def compute_pay(self):
        '''Generic docstring'''
        return float(self.salary) / 24


class Hourly(classification):
    '''Generic docstring'''

    def __init__(self, hourly_rate):
        '''Generic docstring'''
        self.hourly_rate = hourly_rate
        self.timecards = []

    def compute_pay(self):
        '''Generic docstring'''
        pay = 0.0
        for time in self.timecards:
            pay += float(time) * float(self.hourly_rate)
        self.timecards = []
        return pay

    def add_timecard(self, hours):
        '''Generic docstring'''
        self.timecards.append(hours)


class Commissioned(Salaried):
    '''Generic docstring'''

    def __init__(self, salary, commission_rate):
        '''Generic docstring'''
        self.salary = salary
        self.receipts = []
        self.commission_rate = commission_rate

    def add_receipt(self, amount):
        '''Generic docstring'''
        self.receipts.append(amount)

    def compute_pay(self):
        '''Generic docstring'''
        commission = 0.0
        pay = 0.0
        for receipt in self.receipts:
            commission += float(receipt) * float(self.commission_rate)
        self.receipts = []
        pay = float(self.salary) / 24 + (commission * .01)
        return pay


class PayMethod(metaclass=ABCMeta):
    '''Generic docstring'''

    def __init__(self, emp):
        '''Generic docstring'''
        self.emp = emp

    def issue(self, pay):
        '''Generic docstring'''


class DirectMethod(PayMethod):
    '''Generic docstring'''

    def __init__(self, emp, route, account):
        '''Generic docstring'''
        super().__init__(emp)
        self.route = route
        self.account = account

    def issue(self, pay):
        '''Generic docstring'''
        with open(path + PAY_LOGFILE, 'a') as f:
            f.write('Transferred ' + str(pay) + ' for ' + self.emp.name +
                    ' to ' + self.account + ' at ' + self.route + '\n')


class MailMethod(PayMethod):
    '''Generic docstring'''

    def __init__(self, emp):
        '''Generic docstring'''
        super().__init__(emp)

    def issue(self, pay):
        '''Generic docstring'''
        with open(path + PAY_LOGFILE, 'a') as f:
            f.write('Mailing ' + str(pay) + ' to ' + self.emp.name + ' at ' + self.emp.address +
                    ' ' + self.emp.city + ' ' + self.emp.state + ' ' + self.emp.zipcode + '\n')


def load_employees():
    '''Loads employees'''
    # list contains Employee objects
    # Hourly = 1
    # Salary = 2
    # Commissioned = 3
    # Direct Deposit = 1
    # Mail Method = 2def process_timecards():
    with open(path + '/employees.csv', 'r') as f:
        # Get first line of csv and use it to set up named tuple
        csv_reader = reader(f)
        emps = namedtuple("Employee", next(csv_reader))
        # ._make() is used to return a namedtuple() from the iterable passed as argument
        for emp in map(emps._make, csv_reader):
            if emp.Classification == '1':
                hourly = Hourly(emp.Hourly)
                employees[emp.ID] = Employee(
                    emp.ID, emp.Name, emp.Address, emp.City,
                    emp.State, emp.Zip, hourly, emp.PayMethod)
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
                    emp.ID, emp.Name, emp.Address, emp.City,
                    emp.State, emp.Zip, salary, emp.PayMethod)
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
                    emp.ID, emp.Name, emp.Address, emp.City,
                    emp.State, emp.Zip, commission, emp.PayMethod)
                if emp.PayMethod == '1':
                    direct = DirectMethod(
                        employees[emp.ID], emp.Route, emp.Account)
                    employees[emp.ID].paymethod = direct
                else:
                    mail = MailMethod(employees[emp.ID])
                    employees[emp.ID].paymethod = mail


def find_employee_by_id(id):
    '''Find employee by ID'''
    # loop through employee list.  Check employee.id and return Employee object
    if id in employees:
        return employees[id]
    return -1


def process_timecards():
    '''Process time cards'''
    with open(path + '/timecards.txt', 'r') as f:
        csv_reader = reader(f)
        for hour_list in csv_reader:
            id = hour_list.pop(0)
            employees[id].classification.timecards = hour_list


def process_receipts():
    '''Process receipts'''
    with open(path + '/receipts.txt', 'r') as f:
        csv_reader = reader(f)
        for receipt_list in csv_reader:
            id = receipt_list.pop(0)
            employees[id].classification.receipts = receipt_list


def run_payroll():
    '''Runs payroll'''
    if os.path.exists(path + PAY_LOGFILE):
        os.remove(path + PAY_LOGFILE)
    for emp in employees:
        employees[emp].issue_payment()
