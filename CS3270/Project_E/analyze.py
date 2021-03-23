import array as arr
import glob
import os
import sys

import matplotlib.pyplot as plt

# [X] Check for any .dat files in directory
# [X] Make .ini parser
# [] Make .dat parser
# [] Create jagged data and plot (Find pulse) pt_1
# [] Check for piggyback pt_2
# [] Create smoothed data and plot (Find area) pt_1
# [] Area is the sum of the of the values starting at the pulse start and going for width values, or till the start of next pulse

path = os.path.dirname(os.path.abspath(__file__)) + '/'
dat_files = []
ini_file = {}
dat_arr_dict_raw = {}


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
    dat_data = arr.array('i', [])
    for x in range(len(dat_files)):
        with open(path + dat_files[x], 'r') as f:
            for data in f.readlines():
                dat_data.append(int(data) * -1)
            dat_arr_dict_raw[dat_files[x]] = dat_data
    # plt.plot(dat_data)
    #plt.axis([0, len(dat_data), min(dat_data), max(dat_data)])
    # plt.show()
    # print(dat_arr_list)


def create_smooth():
    pass


def main():
    dat_parser()
    ini_parser('gage2scope.ini')  # sys.argv[1] for final product
    vt = ini_file['vt']
    width = ini_file['width']
    pulse_delta = ini_file['pulse_delta']
    drop_ratio = ini_file['drop_ratio']
    below_drop_ratio = ini_file['below_drop_ratio']
    create_jagged()


if __name__ == '__main__':
    main()
