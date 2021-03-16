import os
import shutil
from abc import ABCMeta
from collections import namedtuple
from csv import reader


path = os.path.dirname(__file__)
PAY_LOGFILE = '/paylog.txt'
employees = {}


class Employee:
    def __init__(self, id, name, address, city, state, zipcode, classification, paymethod):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification
        self.paymethod = paymethod

    def make_hourly(self, hourly_rate):
        self.classification = Hourly(hourly_rate)

    def make_salaried(self, salary):
        self.classification = Salaried(salary)

    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)

    def mail_method(self):
        self.paymethod = MailMethod(self)

    def direct_method(self, route, account):
        self.paymethod = DirectMethod(self, route, account)

    def issue_payment(self):
        pay = 0.0
        pay = "{:.2f}".format(self.classification.compute_pay())
        self.paymethod.issue(pay)


class classification(metaclass=ABCMeta):
    def compute_pay(self):
        pass


class Salaried(classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return float(self.salary) / 24


class Hourly(classification):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecards = []

    def compute_pay(self):
        pay = 0.0
        for time in self.timecards:
            pay += float(time) * float(self.hourly_rate)
        self.timecards = []
        return pay

    def add_timecard(self, hours):
        self.timecards.append(hours)


class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        self.salary = salary
        self.receipts = []
        self.commission_rate = commission_rate

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        commission = 0.0
        pay = 0.0
        for receipt in self.receipts:
            commission += float(receipt) * float(self.commission_rate)
        self.receipts = []
        pay = float(self.salary) / 24 + (commission * .01)
        return pay


class PayMethod(metaclass=ABCMeta):
    def __init__(self, emp):
        self.emp = emp

    def issue(self, pay):
        pass


class DirectMethod(PayMethod):
    def __init__(self, emp, route, account):
        super().__init__(emp)
        self.route = route
        self.account = account

    def issue(self, pay):
        with open(path + PAY_LOGFILE, 'a') as f:
            f.write('Transferred ' + str(pay) + ' for ' + self.emp.name +
                    ' to ' + self.account + ' at ' + self.route + '\n')


class MailMethod(PayMethod):
    def __init__(self, emp):
        super().__init__(emp)

    def issue(self, pay):
        with open(path + PAY_LOGFILE, 'a') as f:
            f.write('Mailing ' + str(pay) + ' to ' + self.emp.name + ' at ' + self.emp.address +
                    ' ' + self.emp.city + ' ' + self.emp.state + ' ' + self.emp.zipcode + '\n')


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
    # loop through employee dictionary.  Check employee ID and return Employee object
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
