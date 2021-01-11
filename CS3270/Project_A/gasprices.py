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
                month = int(month[1:])
            elif month.startswith('1'):
                month = int(month[:2])
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
        min_price = float(get_min(year_dict))
        max_price = float(get_max(year_dict))
        print(f'Low: {round(min_price, 3)}, Avg:___, High: {round(max_price, 3)}')

def get_min(year_dict):
    #min_key = min(year_dict, key=int)
    #temp = year_dict[min_key]
    #return min(temp)
    temp_min = float(year_dict[1][0])
    for lists in year_dict:
        for num in year_dict[lists]:
            if float(temp_min) > float(num):
                temp_min = num
                break
    return temp_min
    

def get_max(year_dict):
    #max_key = max(year_dict, key=int)
    #temp = year_dict[max_key]
    #return max(temp)
    temp_max = float(year_dict[1][0])  
    for lists in year_dict:
        for num in year_dict[lists]:
            if float(temp_max) < float(num):
                temp_max = num
    return temp_max

 
def get_average_year(year_dict):
    pass

def get_average_month():
    pass

#process_file()
test = {1: ['10.123', '30.34', '200.3423', '49.6', '4.92034'], 2: ['1.3', '48.234', '20', '5'], 3: ['12', '49.12342', '100.23']}
export_year_info(test, 1994)