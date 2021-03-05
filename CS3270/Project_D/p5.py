from payroll import *
import os
import shutil
employees = []
PAY_LOGFILE = 'paylog.txt'

def load_employees():
    with open('employees.csv', 'r') as f:
        data = [i for i in f.readlines()]
        for i in data[:-1]:
            emp = Employee(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print(emp)

def process_timecards():
    pass
def process_receipts():
    pass

def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees:
        emp.issue_payment()

def find_employee_by_id(id):
    for employee in employees:
        if employee.id == id:
            return employee

def main():
    load_employees()
    process_timecards()
    process_receipts()
    run_payroll()

#Save copy of payroll file; delete old file
shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
if os.path.exists(PAY_LOGFILE):
    os.remove(PAY_LOGFILE)

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

if __name__ == '__main__':
    main()