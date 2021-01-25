from twilio.rest import Client

account_sid = "AC43c457eee9225fcfb23aed7ccfd542af"
auth_token  = "eee49d37f8fbe7baf7823666f0df818a"

client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+38978369330",
#     from_="+17346723629",
#     body="Hi, how are you today?")

msg_previous_sid = "SMbb475ee0639d48f59022dca7368b02bc"
#sid od prethodnata poraka, za da ne isprakja poraki celo vreme


msg_ctx = client.messages.get(msg_previous_sid).fetch()
msg_instance = msg_ctx.fetch()
print("\n", msg_instance.from_, msg_instance.to, msg_instance.body, "\n")


messages = client.messages.list(limit=20)

for i, record in enumerate(messages):
    to = record.to
    status = record.status
    date = record.date_sent.date()
    sid = record.sid
    body = record.body.replace("Sent from your Twilio trial account - ","")
    print(i+1,to, date, status, body)



