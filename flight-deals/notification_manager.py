from twilio.rest import Client

TWILIO_SID = "AC88897ff8379be7a661f3f2b5a5e37fdc"
TWILIO_AUTH_TOKEN = "9df3337106d12b3930e3a98c3ae6621b"
TWILIO_VIRTUAL_NUMBER = "+15393287306"
TWILIO_VERIFIED_NUMBER = "+17706566929"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)