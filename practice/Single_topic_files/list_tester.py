from csv import reader
import os
employees = []
path = os.path.dirname(__file__)

def process_timecards():
    with open(path + '/timecards.txt', 'r') as f:
        csv_reader = reader(f)
        for hour_list in csv_reader:
            print(hour_list[0])

process_timecards()