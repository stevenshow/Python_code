from abc import ABCMeta
#What is left?
# [] issue_payment for Employee
# [] compute_pay for Hourly
# [] compute_pay for Salaried 
# [] compute_pay for Commissioned
# [] issue for DirectMethod
# [] issue for MailMethod

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
    
    def make_salary(self, salary):
        self.classification = Salaried(salary)
    
    def make_commissioned(self, salary, rate):
        self.classification = Commissioned(salary, rate)
    
    def mail_method(self):
        self.paymethod = MailMethod(self)
    
    def direct_method(self, route, account):
        self.paymethod = DirectMethod(self, route, account)
    
    def issue_payment(self):
        pass

class classification(metaclass=ABCMeta):
    def compute_pay(self):
        pass

class Salaried(classification):
    def __init__(self, salary):
        self.salary = salary
    
    def compute_pay(self):
        pass

class Hourly(classification):
    def __init__(self, hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecards = []

    def compute_pay(self):
        pass

    def add_timecards(self, hours):
        self.timecards.append(hours)

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        self.salary = salary
        self.receipts = []
        self.commission_rate = commission_rate

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        pass



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
        pass

class MailMethod(PayMethod):
    def __init__(self, emp):
        super().__init__(emp)
    
    def issue(self, pay):
        pass