import json
import os
import smtplib
import ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import concurrent.futures
import threading
import time


# API key for the catapi

api_key = '2fe5b288-d44d-45b5-ac2e-e8a5d81524db'

path = os.path.dirname(__file__) + '/Images'

# Gets the cat_fact json from the cat-fact api

fact_data = requests.get(
    'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=3')
facts = fact_data.json()

# Gets the image URL from the catapi

cat_image = requests.get(
    'https://api.thecatapi.com/v1/images/search?api_key='+api_key)
image_json = cat_image.json()
url = image_json[0]['url']

# Grabs the global URL and checks to see if there is an image in the image folder
# If there is, it deletes it and downloads the new one, if not it just downloads it


def get_image():
    r = requests.get(url, allow_redirects=True)
    if 'cat.jpg' not in path:
        with open(path + '/cat.jpg', 'wb') as f:
            f.write(r.content)
        print('Successfully downloaded and saved cat.jpg')
    else:
        os.remove(path + 'cat.jpg')
        print('deleted old cat.jpg')
        with open(path + '/cat.jpg', 'wb') as f:
            f.write(r.content)
        print('saved new cat.jpg')

# Gets a single verified cat fact and returns the fact


def get_fact():
    fact_list = []
    for fact in facts:
        if fact['status']['verified']:
            if len(fact_list) < 1:
                fact_list.append(fact['text'])
    return fact_list

# Sets up the secure email service and places the fact and image to be sent in the email


def send_mail(receiver_email):
    context = ssl.create_default_context()
    smtp_server = 'smtp.gmail.com'
    sender_email = 'programmer.steve7@gmail.com'
    password = 'python_programming_is_fun7'
    #receiver_email = ['steven.schoebinger@gmail.com', '10627666@my.uvu.edu']
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Daily Cat Fact'
    message['From'] = 'Cat Fax'
    message['To'] = receiver_email

    part1 = MIMEText(cat_fact[0], 'plain')
    img_data = open(path + '/cat.jpg', 'rb').read()
    part2 = MIMEImage(img_data)
    message.attach(part1)
    message.attach(part2)
    with smtplib.SMTP_SSL(smtp_server, 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

email_list = ['steven.schoebinger@gmail.com', '10627666@my.uvu.edu']
cat_fact = get_fact()
get_image()
with concurrent.futures.ThreadPoolExecutor(max_workers=min(50, len(email_list))) as executor:
    results = executor.map(send_mail, email_list)