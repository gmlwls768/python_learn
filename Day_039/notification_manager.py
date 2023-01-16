from twilio.rest import Client
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.account_sid = os.environ.get("account_sid")
        self.auth_token = os.environ.get("auth_token")
        self.my_num = os.environ.get("my_num")
        self.twilio = os.environ.get("twilio")

    def noti(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=f"{message}",
                from_=self.twilio,
                to=self.my_num
            )
        print(message.status)
