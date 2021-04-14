# [] Download all flag files into a local directory named flags
# [] Report the number of bytes downloaded•
# [] Report the execution time of the script(using time.perf_counter())•
# [] Report the CPU time of the script (using time.process_time())

import os
import requests
from time import perf_counter


img_path = os.path.dirname(__file__) + '/flags/'
txt_path = os.path.dirname(__file__) + '/'

# Populate flags list with all flag names
with open(txt_path + 'flags.txt', 'r') as f:
    flags = f.read().splitlines()

def get_flags():
    start = perf_counter()
    for country in flags:        
        flag_name = country + '.jpg'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
        image = requests.get('https://www.sciencekids.co.nz/images/pictures/flags96/' + flag_name,headers=headers)
        open(img_path + flag_name, 'wb+').write(image.content)
    end = perf_counter()
    print(f'Elapsed Time: {round(end-start,2)} seconds.')

get_flags()