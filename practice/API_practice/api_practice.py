import requests
from twilio.rest import Client
account_sid = 'ACfc24531924305a41062999b18a96c35b'
auth_token = '0aa5651fe600699cc18efb7ad64bba30'

client = Client(account_sid, auth_token)

r = requests.get('http://api.open-notify.org/astros.json')
people = r.json()

number_iss = people['number']

Message = 'Hi!  Fun fact, the amount of people in space right now is ' + \
    str(number_iss)

message = client.messages.create(
    to="+18017094444", 
    from_="+19786911313", 
    body=Message)
print(message.sid)

def main():
    pass

if __name__ == main():
    main()
