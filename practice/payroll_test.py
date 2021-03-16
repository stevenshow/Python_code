from abc import ABCMeta
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
        pass
    def make_salary(self, salary):
        pass
    def make_commissioned(self, salary, rate):
        pass
    def mail_method(self):
        pass
    def direct_method(self, route, account):
        pass
    def issue_payment(self):
        pass

#Is this necessary?  
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
        pass

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        self.salary = salary
        self.receipts = []
        self.commission_rate = commission_rate

    def add_receipt(self, amount):
        pass

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