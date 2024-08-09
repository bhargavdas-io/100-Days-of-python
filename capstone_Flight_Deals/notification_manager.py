import os
from twilio.rest import Client


class NotificationManager:
    def __init__(self):
        self.twilio_sid = os.environ['TWILIO_SID']
        self.twilio_token = os.environ['TWILIO_TOKEN']
        self.client = Client(self.twilio_sid, self.twilio_token)

    def send_message(self, message_body):
        message = self.client.messages.create(
            from_=os.environ['TWILIO_NUMBER'],
            body=message_body,
            to=os.environ['REGISTERED_NUMBER'],
        )
        print(message.sid)
