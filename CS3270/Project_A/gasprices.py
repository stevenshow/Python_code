# pylint: disable=invalid-name
# [X] Open and Read file of gas prices
# [X] Separate the dates and prices for each year
# [] Calculate low, average, and high for EACH YEAR
# [] Calculate average price for each month
# [] Export report to file gas_report.txt

def read_file():
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_prices.txt', 'r') as f:
        file = f.read()
    return file
    #print(file)

def process_file():
    file = read_file()
    lines = file.split()
    year_dict = {}
    curr_year = int(lines[0].split(':')[0][-4:])
    year_counter = 0 
    month = 0
    for line in lines:                              #creates a list with [0] being the date string and [1] being the price string
        month_data = line.split(':')
        year_counter = int(month_data[0][-4:])
        if year_counter == curr_year:               #grabs month from date string
            month = month_data[0][:2]
            if month.startswith('0'):
                month = month[1:]
            if month not in year_dict.keys():
                year_dict[month] = [month_data[1]]
            else:    
                year_dict[month].append(month_data[1])
        else:
            export_year_info(year_dict, curr_year)
            year_counter += 1
            break
            

def export_year_info(year_dict, year):
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_report.txt', 'a+') as out:
        min_price = get_min(year_dict)
        

def get_min(year_dict):
    min_key = min(year_dict, key=year_dict.get)
    temp = year_dict[min_key]
    return min(temp)
    

def get_max(year_dict):
    max_key = max(year_dict, key=year_dict.get)
    temp = year_dict[max_key]
    return max(temp)
 
def get_average_year(year_dict):
    pass

def get_average_month():
    pass

process_file()
test = {'1': [10,30,50], '2': [50,20,5], '3': [0,50,100]}
#export_year_info(test, 1994)