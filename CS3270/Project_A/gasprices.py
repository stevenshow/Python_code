'''Grabs contents of a gasprices file and returns the year by year
analysis of the high, low, and averages
Created by: Steven Schoebinger CS3270 01/12/2021'''
import calendar
from statistics import mean
# pylint: disable=invalid-name
# [X] Open and Read file of gas prices
# [X] Separate the dates and prices for each year
# [X] Calculate low, average, and high for EACH YEAR
# [X] Calculate average price for each month
# [X] Export report to file gas_report.txt

def read_file():
    '''Opens the files and returns the read file'''
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_prices.txt', 'r') as f:
        file = f.read()
    return file

def process_file():
    '''Calls function to open the file and populates the year
    dictionary, then calls the outputting functions'''
    file = read_file()
    lines = file.split()
    year_dict = {}
    curr_year = int(lines[0].split(':')[0][-4:])
    year_counter = 0
    month = 0
    #creates a list with [0] being the date string and [1] being the price string
    for line in lines:
        month_data = line.split(':')
        year_counter = int(month_data[0][-4:])
        #grabs month from date string
        if year_counter == curr_year:
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
    '''Takes in dictionary of the years data and prints
    the years high, low, and average prices'''
    min_price = float(get_min(year_dict))
    max_price = float(get_max(year_dict))
    average = get_average_year(year_dict)
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_report.txt', 'a+') as out:
        out.write(f'\n{year}:')
        out.write(f'\tLow: ${round(min_price, 2)}, Avg: ${round(average, 2)},'
                f' High: ${round(max_price, 2)}\n')

def print_month_info(year_dict):
    '''Takes dictionary of the years data and prints
    the months info'''
    #calendar.month_name[number of month 1-12]
    counter = 0
    curr_month = 1
    with open('/home/steven/Documents/Python_code/CS3270/Project_A/gas_report.txt', 'a+') as out:
        for line in year_dict:
            #counter == line
            while line == curr_month:
                average_month = mean(float(n) if n else 0 for n in year_dict[line])
                out.write('\t\t{:<10s}${:.2f}\n'.format(
                        calendar.month_name[curr_month],round(average_month, 2)))
                counter += 1
                curr_month += 1
                break
            else:
                break

def get_min(year_dict):
    '''Takes dictionary of the years gas prices
    and returns the min value'''
    temp_min = float(year_dict[1][0])
    for lists in year_dict:
        for num in year_dict[lists]:
            if float(temp_min) > float(num):
                temp_min = num
                break
    return temp_min

def get_max(year_dict):
    '''Takes dictionary of the years gas prices
    and returns the max value'''
    temp_max = float(year_dict[1][0])
    for lists in year_dict:
        for num in year_dict[lists]:
            if float(temp_max) < float(num):
                temp_max = num
    return temp_max

def get_average_year(year_dict):
    '''Takes dictionary of the years gas prices
    and returns the average over the year'''
    overall = 0
    counter = 0
    for lists in year_dict:
        for num in year_dict[lists]:
            counter += 1
            overall += float(num)
    if(overall <= 0 or counter <= 0):
        return 0
    return overall / counter

process_file()
