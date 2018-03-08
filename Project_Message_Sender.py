from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5e2fe565c5c374f82fde0e5b7b3375ea"
# Your Auth Token from twilio.com/console
auth_token  = "enter your TOKEN of twilio"

client = Client(account_sid, auth_token)


message = client.messages.create(
    to="+918210352696",
    from_="+18059208119",
    body="Hello python!!")

print message.sid
