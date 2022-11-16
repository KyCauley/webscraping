import key2
from twilio.rest import Client

client = Client(key2.accountSID,key2.authToken)

twilionumber = '+13236121761'
myCellphone = '+18325256779'

textmsg = client.messages.create(to=myCellphone,from_=twilionumber,body = "Hey there!")

print(textmsg.status)

call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml',to=myCellphone,from_=twilionumber)