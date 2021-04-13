from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC57e3934faeada9eae5b2808218509ea2"
# Your Auth Token from twilio.com/console
auth_token  = "82116d1a6bc21a751f520bb6a04fd7ff"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19177506960",
    from_="+12182033819",
    body="Hello husband from Python!")

print(message.sid)