
from twilio.rest import Client
client = Client("AC8524e480f521715997282f87d6879cf0", "302f4c8c7dca0fdd448f255ace993337")

msg="billid:1\ndate-2\To use SMS, you will need a phone number from Twilio. \nOn your trial account \nyou can\n get one free USA or Canada phone number. To get local phone number outside of the USA or Canada, you may need to upgrade your account and meet regulatory requirements"
client.messages.create(to="+919379067642", 
                       from_="+12546553126", 
                       body=msg)