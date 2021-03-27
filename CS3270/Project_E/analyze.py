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
area_dict = {}


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


def pdf_output():
    for fname in dat_files:
        with PdfPages(path + fname.replace('.dat', '.pdf')) as export_pdf:
            raw_file = dat_dict_raw[fname]
            plot1 = plt.figure()
            plt.title(fname)
            plt.ylabel('Raw')
            plt.plot(raw_file)
            plt.axis([0, len(raw_file), min(raw_file), max(raw_file)])
            plt.show()
            export_pdf.savefig(plot1)
            plt.close()

            smooth_file = dat_dict_smooth[fname]
            plot2 = plt.figure()
            plt.ylabel('Smooth')
            plt.plot(smooth_file)
            plt.axis([0, len(smooth_file), min(smooth_file), max(smooth_file)])
            plt.show()
            export_pdf.savefig(plot2)
            plt.close()


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
            elif x < len(dat_dict_raw[file]) - 3:
                s_data.append((dat_dict_raw[file][x-3]
                               + 2*dat_dict_raw[file][x-2]
                               + 3*dat_dict_raw[file][x-1]
                               + 3*dat_dict_raw[file][x]
                               + 3*dat_dict_raw[file][x+1]
                               + 2*dat_dict_raw[file][x+2]
                               + dat_dict_raw[file][x+3]) // 15)
            else:
                s_data.append(dat_dict_raw[file][x])
        dat_dict_smooth[file] = s_data
        s_data = arr.array('i', [])


def find_pulse(vt, width, pulse_delta, drop_ratio, below_drop_ratio):
    '''Find a pulse by looking for a rise over 3 consecutive points (Yi, Yi+1, Yi+2)
    if the rise (Yi+2 - Yi) exceeds vt, then a pulse begins at position i.  After finding
    a pulse, move forward through the data starting at Yi+2 until the sample starts to decrease
    before looking for next pulse.

    Check for piggyback pulses (a weak pulse followed quickly by another pulse).  When adjacent
    pulses begin within pulse_delta positions of each other, find how many points between the peak
    of the first pulse and the start of the second pulse fall below drop_ratio times the peak
    of the first pulse.  If the number exceeds below_drop_ratio, omit the first pulse.'''
    not_considered = []
    for file in dat_files:
        pulses[file] = []
        not_considered = []
        # pulse_start = []
        for y in range(len(dat_dict_smooth[file]) - 2):
            # If a rise over 3 points (yi, yi+1, yi+2) is greater than vt, a pulse starts at i
            if dat_dict_smooth[file][y+2] - dat_dict_smooth[file][y] > vt and y not in not_considered:
                #print(dat_dict_smooth[file][y], dat_dict_smooth[file][y+1], dat_dict_smooth[file][y+2], dat_dict_smooth[file][y+3])
                pulses[file].append(y)
                not_considered.append(dat_dict_smooth[file][y+1])
                # Traverse from y+2 until a decrease before looking for next pulse
                for x in range(y+1, len(dat_dict_smooth[file])):
                    if dat_dict_smooth[file][x] < dat_dict_smooth[file][x+1]:
                        not_considered.append(x)
                    else:
                        break
    piggy_back(pulse_delta, drop_ratio, below_drop_ratio)


def piggy_back(pulse_delta, drop_ratio, below_drop_ratio):
    for file in dat_files:
        piggy_pulse[file] = []
        for x in range(len(pulses[file])-1):
            if pulses[file][x] - pulses[file][x+1] <= pulse_delta:
                counter = 0
                search_array = dat_dict_smooth[file][pulses[file]
                                                     [x]:pulses[file][x+1]]
                peak = max(search_array)
                p_index = search_array.index(peak)
                search_array = search_array[p_index:]
                for y in range(len(search_array)):
                    if search_array[y] < drop_ratio * peak:
                        counter += 1
                    if counter > below_drop_ratio:
                        piggy_pulse[file].append(pulses[file][x])
                        counter = 0
        for pulse in piggy_pulse[file]:
            pulses[file].remove(pulse)


def find_area(pulses, width):
    '''The area is the sum of the values starting at the pulse start and going for width samples,
    or until the start of the next pulse, whichever comes first. Use raw data for area computation'''
    file = dat_dict_raw['as_ch01-0537xx_Record1042.dat']
    counter = 0
    area = 0
    for file in dat_files:
        area_dict[file] = []
        for pulse in pulses[file]:
            area = 0
            counter = 0
            while counter < width:
                area += dat_dict_raw[file][pulse+counter]
                counter += 1
                if pulse+counter in pulses[file]:
                    break
            area_dict[file].append(area)


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
    pdf_output()
    for file in dat_files:
        print(file + ':')
        for x in range(len(piggy_pulse[file])):
            print('Found piggyback at ' + str(piggy_pulse[file][x]))
        for y in range(len(pulses[file])):
            print(str(pulses[file][y]) + ' (' + str(area_dict[file][y]) + ')')
        print('\n')


if __name__ == '__main__':
    main()
