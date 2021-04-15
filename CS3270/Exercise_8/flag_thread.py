'''Uses futures and threading to concurentlly grab each flag from list of countries.
Then reports the CPU time, script time, and bytes downloaded.
Created by: Steven Schoebinger 04/14/2021'''
# pylint: disable=invalid-name
# [X] Download all flag files into a local directory named flags
# [X] Report the number of bytes downloaded•
# [X] Report the execution time of the script(using time.perf_counter())•
# [X] Report the CPU time of the script (using time.process_time())
# [X] Send email using MIME and attach the US flag (with its filename) to chuck.allison@gmail.com
# [X] The text portion of the email should say 'Here you go, Professor Allison!'

import concurrent.futures
import os
import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import perf_counter, process_time

import requests

img_path = os.path.dirname(__file__) + '/flags/'
txt_path = os.path.dirname(__file__) + '/'

with open(txt_path + 'flags.txt', 'r') as f:
    flags = f.read().splitlines()
flags.pop()


def get_flag(country):
    '''Makes get requests for the flag of the country passed.'''
    flag_name = f'{country}.jpg'
    # headers = {
    #     '''User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'''}
    image = requests.get(
        'https://www.sciencekids.co.nz/images/pictures/flags96/' + flag_name)
    with open(img_path + flag_name, 'wb+') as img:
        img.write(image.content)
    return int(image.headers['Content-Length'])


def t_pool_submit():
    '''Creates thread pool and maps each country to the get_flag() function.
    Reports CPU time, script time, and bytes downloaded'''
    start = perf_counter()
    cpu_start = process_time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(get_flag, flags)
    sum_bytes = sum(results)
    end = perf_counter()
    cpu_end = process_time()
    print(
        f'Threading elapsed CPU Time: {round(cpu_end-cpu_start, 2)} seconds.')
    print(f'Threading elapsed Time: {round(end-start,2)} seconds.')
    # 405.652 Kbs
    print(f'Amount of bytes downloaded: {round(sum_bytes/1024, 3)} Kbs')


def send_mail():
    '''Sends email to professor with United States flag as attachment'''
    context = ssl.create_default_context()
    smtp_server = 'smtp.gmail.com'
    sender_email = os.environ.get('PROG_GMAIL')
    password = os.environ.get('GMAIL_PASS')
    receiver_email = 'steven.schoebinger@gmail.com'
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Exercise 8'
    message['From'] = 'Steven Schoebinger'
    message['To'] = receiver_email

    us_flag = 'United_States.jpg'
    text = MIMEText('Here you go, Professor Allison!', 'plain')
    img_data = open(img_path + us_flag, 'rb').read()
    img = MIMEImage(img_data, name=us_flag)
    message.attach(text)
    message.attach(img)
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print('Email sent!')


t_pool_submit()
#send_mail()
