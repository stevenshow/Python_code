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
dat_dict_raw = {}
dat_dict_smooth = {}


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
    file = dat_dict_raw['2_Record2308.dat']
    plt.plot(file)
    plt.axis([0, len(file), min(file), max(file)])
    plt.show()

def create_smooth():
    '''Starting with the 4th point of the file, and ending with the 4th from the last,
    replace each of those points with the following average in a new array
    (Pi-3 + 2Pi-2 + 3Pi-1 + 3Pi + 3∗Pi+1 + 2Pi+2 + Pi+3)//15'''
    s_data = arr.array('i', [])
    #end = len(dat_arr_dict_raw['as_ch01-0537xx_Record1042.dat'][3:-3])

    # Set up first 3 values in the smooth array
    for file in dat_dict_raw.keys():
        for x in range(0, len(dat_dict_raw[file])):
            if x < 3:
                s_data.append(dat_dict_raw[file][x])
                #dat_dict_smooth[file] = s_data
            elif x < len(dat_dict_raw[file]) -3:
                s_data.append((dat_dict_raw[file][x-3]
                            + 2*dat_dict_raw[file][x-2]
                            + 3*dat_dict_raw[file][x]
                            + 3*dat_dict_raw[file][x+1]
                            + 2*dat_dict_raw[file][x+2]
                            + dat_dict_raw[file][x+3]) //15)
            else:
                s_data.append(dat_dict_raw[file][x])
        #print(s_data)
        dat_dict_smooth[file] = s_data
        s_data = arr.array('i', [])
    #print(dat_dict_smooth['2_Record2308.dat'])
    file = dat_dict_smooth['2_Record2308.dat']
    plt.plot(file)
    plt.axis([0, len(file), min(file), max(file)])
    plt.show()

def main():
    dat_parser()
    ini_parser('gage2scope.ini')  # sys.argv[1] for final product
    vt = ini_file['vt']
    width = ini_file['width']
    pulse_delta = ini_file['pulse_delta']
    drop_ratio = ini_file['drop_ratio']
    below_drop_ratio = ini_file['below_drop_ratio']
    create_jagged()
    create_smooth()


if __name__ == '__main__':
    main()
