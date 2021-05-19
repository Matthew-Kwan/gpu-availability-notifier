from decouple import config
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = config('TWILIO_ACCOUNT_SID')
# auth_token = config('TWILIO_AUTH_TOKEN')
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Hello, there!',
#                               to='whatsapp:+14167383838'
#                           )

# print(message.sid)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!',
                              from_='+13654008424',
                              to='+14167383838'
                          )

print(message.sid)