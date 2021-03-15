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

class classification(Employee):
    def __init__(self, id, name, address, city, state, zipcode, classification, paymethod):
        self.classification = classification   
        Employee.__init__(self, id, name, address, city, state, zipcode, classification, paymethod)
    def compute_pay(self):
        pass

class Salaried(classification):
    def __init__(self, id, name, address, city, state, zipcode, classification, paymethod):
        super().__init__(id, name, address, city, state, zipcode, classification, paymethod)