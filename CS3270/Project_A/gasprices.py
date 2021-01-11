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
    curr_year = lines[0].split(':')[0][-4:]
    year_counter = 0 
    month = 0
    for line in lines:                              #creates a list with [0] being the date string and [1] being the price string
        month_data = line.split(':')
        year_counter = month_data[0][-4:]
        if year_counter == curr_year:   #grabs month from date string
            month = month_data[0][:2]
            year_dict[month] = month_data[1]
        else:
            export_year_info(year_dict)
            year_counter += 1
            break
            

def export_year_info(year_dict):
    pass

process_file()