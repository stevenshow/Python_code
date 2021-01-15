# pylint: disable=invalid-name
# [X] Open and Read file of gas prices
# [X] Separate the dates and prices for each year
# [X] Calculate low, average, and high for EACH YEAR
# [X] Calculate average price for each month
# [] Export report to file gas_report.txt
import calendar
from statistics import mean

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
            print_year_info(year_dict, curr_year)
            print_month_info(year_dict)
            year_counter += 1
            curr_year += 1
            year_dict = {}
            continue
    print_year_info(year_dict, curr_year)
    print_month_info(year_dict)
            

def print_year_info(year_dict, year):
    min_price = float(get_min(year_dict))
    max_price = float(get_max(year_dict))
    average = get_average_year(year_dict)
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_report.txt', 'a+') as out:
        out.write(f'\n{year}:')
        out.write(f'\tLow: ${round(min_price, 2)}, Avg: ${round(average, 2)}, High: ${round(max_price, 2)}\n')
        

def print_month_info(year_dict):
    #calendar.month_name[number of month 1-12]
    counter = 0
    curr_month = 1                              #Need to figure out how to get the dictionary key in the first slot ***
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_report.txt', 'a+') as out: 
        for line in year_dict:                      #Need to print the prices of the months gas average in a neat column
            counter == line
            while(line == curr_month):
                average_month = mean(float(n) if n else 0 for n in year_dict[line])
                out.write('\t\t{:<10s}${:.2f}\n'.format(calendar.month_name[curr_month],round(average_month, 2)))
                #print(f'\t{calendar.month_name[curr_month]}\t${round(average_month, 2)}')
                counter += 1
                curr_month += 1
                break
            else:
                break

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
    overall = 0
    counter = 0
    for lists in year_dict:
        for num in year_dict[lists]:
            counter += 1
            overall += float(num)
    if(overall > 0 and counter > 0):
        return (overall / counter)
    else:
        return 0

def get_average_month(year_dict):
    pass

process_file()
test = {1: ['10.123', '30.34', '200.3423', '49.6', '4.92034'], 2: ['1.3', '48.234', '20', '5'], 3: ['12', '49.12342', '1.13']}
test = {1: ['1', '2', '3', '4'], }
#export_year_info(test, 1994)
