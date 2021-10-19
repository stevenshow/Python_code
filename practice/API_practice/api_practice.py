import requests
from twilio.rest import Client
account_sid = TWILIO_SID
auth_token = TWILIO_TOKEN

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = 'Hi!  Fun fact, the amount of people in space right now is ' + \
    str(number_iss)

message = client.messages.create(
    to= MY_PHONE_NUMBER, 
    from_="+19786911313", 
    body=Message)
print(message.sid)

def main():
    pass

if __name__ == main():
    main()
