import requests
import json
import smtplib, ssl

port = 587
password = 'python_programming_is_fun7'
smtp_server = 'smtp.gmail.com'
sender_email = 'programmer.steve7@gmail.com'

#Create a secure SSL context
context = ssl.create_default_context()
data = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=3')
facts = data.json()


def get_fact():
    fact_list = []
    for fact in facts:
        if fact['status']['verified']:
            if len(fact_list) < 1:
                fact_list.append(fact['text'])
    return fact_list


def send_mail(message):
    #Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo() # can be omitted
        server.starttls(context = context) #secure the connection
        server.ehlo()
        server.login(sender_email, password)
        #TODO: send email here
        server.sendmail(sender_email, 'kayla.schoebinger@gmail.com', message)
    except Exception as e:
        print(e)
    finally:
        server.quit()

message = get_fact()
send_mail(message[0])