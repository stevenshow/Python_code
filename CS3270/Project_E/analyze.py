import array as arr
import glob
import itertools
import os
import sys

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# [X] Check for any .dat files in directory
# [X] Make .ini parser
# [X] Make .dat parser
# [X] Create jagged data and plot (Find Area) pt_1
# [] Check for piggyback pt_2
# [X] Create smoothed data and plot (Find Pulse) pt_1
# [X] Area is the sum of the of the values starting at the pulse start and going for width values, or till the start of next pulse

path = os.path.dirname(os.path.abspath(__file__)) + '/'
dat_files = []
ini_file = {}
dat_dict_raw = {}
dat_dict_smooth = {}
pulses = {}
piggy_pulse = {}


def ini_parser(file):
    '''Gets the .ini file from command line and parses data into ini_file'''
    with open(path + file, 'r') as f:
        lines = f.read().splitlines()
        for x in range(5):
            line = lines[x].split('=')
            ini_file[line[0]] = line[1]


def dat_parser():
    '''Gets all .dat files in the working directory, then parses data'''
    os.chdir(path)
    for file in glob.glob('*.dat'):
        dat_files.append(file)


def create_jagged():
    ''''When adjacentpulses begin within pulse_deltapositions of each other, 
    find how many points between the peak of the first pulse and the start of the second pulse 
    fall below drop_ratiotimes the peak of the first pulse. If the number exceeds below_drop_ratio, 
    omit the first pulse from further consideration—it is not a pulse of interest.'''
    raw_dat_data = arr.array('i', [])
    for x in range(len(dat_files)):
        with open(path + dat_files[x], 'r') as f:
            for data in f.readlines():
                raw_dat_data.append(int(data) * -1)
            dat_dict_raw[dat_files[x]] = raw_dat_data
            raw_dat_data = arr.array('i', [])
    # Creates pdf for each raw graph
    # for fname in dat_dict_raw:
    #     file = dat_dict_raw[fname]
    #     plot1 = plt.figure()
    #     plt.plot(file)
    #     plt.axis([0, len(file), min(file), max(file)])
    #     # plt.show()
    #     plot1.savefig(path + fname.replace('.dat', '_raw.pdf'),
    #                   bbox_inches='tight')


def create_smooth():
    '''Starting with the 4th point of the file, and ending with the 4th from the last,
    replace each of those points with the following average in a new array
    (Pi-3 + 2Pi-2 + 3Pi-1 + 3Pi + 3∗Pi+1 + 2Pi+2 + Pi+3)//15'''
    s_data = arr.array('i', [])
    # Set up first 3 values in the smooth array
    for file in dat_dict_raw.keys():
        for x in range(0, len(dat_dict_raw[file])):
            if x < 3:
                s_data.append(dat_dict_raw[file][x])
                #dat_dict_smooth[file] = s_data
            elif x < len(dat_dict_raw[file]) - 3:
                s_data.append((dat_dict_raw[file][x-3]
                               + 2*dat_dict_raw[file][x-2]
                               + 3*dat_dict_raw[file][x]
                               + 3*dat_dict_raw[file][x+1]
                               + 2*dat_dict_raw[file][x+2]
                               + dat_dict_raw[file][x+3]) // 15)
            else:
                s_data.append(dat_dict_raw[file][x])
        dat_dict_smooth[file] = s_data
        s_data = arr.array('i', [])
    # Creates pdf for each smooth graph
    # for fname in dat_dict_smooth:
    #     file = dat_dict_smooth[fname]
    #     plot1 = plt.figure()
    #     plt.plot(file)
    #     plt.axis([0, len(file), min(file), max(file)])
    #     # plt.show()
    #     plot1.savefig(path + fname.replace('.dat',
    #                                        '_smooth.pdf'), bbox_inches='tight')


def find_pulse(vt, width, pulse_delta, drop_ratio, below_drop_ratio):
    '''Find a pulse by looking for a rise over 3 consecutive points (Yi, Yi+1, Yi+2)
    if the rise (Yi+2 - Yi) exceeds vt, then a pulse begins at position i.  After finding
    a pulse, move forward through the data starting at Yi+2 until the sample starts to decrease
    before looking for next pulse.

    Check for piggyback pulses (a weak pulse followed quickly by another pulse).  When adjacent
    pulses begin within pulse_delta positions of each other, find how many points between the peak
    of the first pulse and the start of the second pulse fall below drop_ratio times the peak
    of the first pulse.  If the number exceeds below_drop_ratio, omit the first pulse.'''
    #file = dat_dict_smooth['as_ch01-0537xx_Record1042.dat']
    #pulses = []
    # TODO Need to figure out why file 3388 is the only file that is off on pulse location
    # print(dat_dict_smooth['2_record3388.dat'][0])
    not_considered = []
    for file in dat_files:
        pulses[file] = []
        #pulse_start = []
        for y in range(len(dat_dict_smooth[file]) - 2):
            # If a rise over 3 points (yi, yi+1, yi+2) is greater than vt, a pulse starts at i 
            if dat_dict_smooth[file][y+2] - dat_dict_smooth[file][y] > vt and y not in not_considered:
                pulses[file].append(y)
                not_considered.append(dat_dict_smooth[file][y+1])
                # Traverse from y+2 until a decrease before looking for next pulse
                for x in range(y+1, len(dat_dict_smooth[file])):
                    if dat_dict_smooth[file][x] < dat_dict_smooth[file][x+1]:
                        not_considered.append(x)
                    else:
                        break
        not_considered = []
    piggy_back(pulse_delta, drop_ratio, below_drop_ratio)
    print('pulse at: ' + str(pulses))


def piggy_back(pulse_delta, drop_ratio, below_drop_ratio):
    for file in dat_files:
        for x in range(len(pulses)-1):
            if pulses[x] - pulses[x+1] <= pulse_delta:
                counter = 0
                search_array = dat_dict_smooth['as_ch01-0537xx_Record1042.dat'][pulses[x]:pulses[x+1]]
                peak = max(search_array)
                p_index = search_array.index(peak)
                search_array = search_array[p_index:]
                for y in range(len(search_array)):
                    if y < drop_ratio * peak:
                        counter += 1
                    if counter > below_drop_ratio:
                        piggy_pulse[file][0].append([pulses[x]])
                        # pulses.remove(pulses[x])
                        counter = 0
                        print(piggy_pulse)
                #print(f'Peak between {pulses[x]} and {pulses[x+1]} = ', peak)
        # print(pulses_to_remove)
        for pulse in piggy_pulse[file]:
            pulses.remove(pulse)
        print(pulses)
        # pulses.remove(pulses[x])


def find_area(pulses, width):
    '''The area is the sum of the values starting at the pulse start and going for width samples,
    or until the start of the next pulse, whichever comes first. Use raw data for area computation'''
    file = dat_dict_raw['as_ch01-0537xx_Record1042.dat']
    counter = 0
    area = 0
    for pulse in pulses:
        while counter < width:
            area += file[pulse+counter]
            counter += 1
            if pulse+counter in pulses:
                print(area)
                area = 0
                counter = 0
                break
    print(area)


def main():
    dat_parser()
    ini_parser('gage2scope.ini')  # sys.argv[1] for final product
    vt = int(ini_file['vt'])
    width = int(ini_file['width'])
    pulse_delta = int(ini_file['pulse_delta'])
    drop_ratio = float(ini_file['drop_ratio'])
    below_drop_ratio = float(ini_file['below_drop_ratio'])
    create_jagged()
    create_smooth()
    find_pulse(vt, width, pulse_delta, drop_ratio, below_drop_ratio)
    find_area(pulses, width)

    with open('ch01Smooth.dat', 'a') as f:
        for x in dat_dict_smooth['as_ch01-0537xx_Record1042.dat']:
            f.write(str(x)+'\n')


if __name__ == '__main__':
    main()
