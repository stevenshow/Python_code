import csv
import os
import pprint
import matplotlib.pyplot as plt
import numpy as np

path = os.path.dirname(__file__) + '/'

def main():
    filename = 'weather_data.csv'
    fields = []
    rows = []

    with open(path + filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        row_count = csvreader.line_num
        #print(f'Total number of rows {row_count}')
    # rows[entry][daily data]

    daily_temps = {}
    temps = []
    dates = []
    date = rows[0][0].split(' ')[0]
    for x in range(row_count - 1):
        if rows[x][0].split(' ')[0] == date:
            temps.append(float(rows[x][1]))
        else:
            daily_temps[date] = [min(temps), max(temps)]
            dates.append(date)
            date = rows[x][0].split(' ')[0]
            temps = []
    print(len(daily_temps))
    lows = []
    highs = []
    for x in dates:
        lows.append((daily_temps[x][0]))
        highs.append((daily_temps[x][1]))
    plt.plot(dates, highs, label="High")
    plt.plot(dates, lows, label="Low")
    plt.ylabel('Temperature (Farenheight)')
    plt.xlabel('Date')
    plt.xticks(dates, dates, rotation="vertical")
    plt.legend()
    plt.show()


    #TODO Working on getting bar chart looking good 
    # x = np.arange(len(dates))
    # width = 0.2

    # fig, ax = plt.subplots()
    # high_bar = ax.bar(x - width/2, highs, width, label="High")
    # low_bar = ax.bar(x + width/2, lows, width, label="Low")
    
    # ax.set_ylabel('Temperature (Farenheight)')
    # ax.set_xticks(x)
    # ax.set_xticklabels(dates)
    # ax.legend()

    # ax.bar_label(high_bar, padding=3)
    # ax.bar_label(low_bar, padding=3)

    # fig.tight_layout()
    # plt.show()


if __name__ == '__main__':
    main()