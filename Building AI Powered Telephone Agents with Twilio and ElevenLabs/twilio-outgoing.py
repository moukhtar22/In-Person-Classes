from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

account_sid = os.getenv("SID")
auth_token = os.getenv("TOKEN")
client = Client(account_sid, auth_token)

# The phone number to call (recipient)
to_phone_number = "+18283651111" # Replace with the actual recipient's number
# Your Twilio phone number (must be purchased and voice-enabled in Twilio)
from_phone_number = "+1844431111" # Replace with your Twilio number

call = client.calls.create(
    twiml='''<Response>
                <Say>Hello, World. This is the Twilio bot calling!</Say>
                <Pause length="2"/>
                <Say>That was fun! Goodbye</Say>
                <Pause length="2"/>
            </Response>''',
    to=to_phone_number,
    from_=from_phone_number
)

print(call.sid)
