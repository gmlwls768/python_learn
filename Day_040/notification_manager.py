import smtplib
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.smtp_server = os.environ.get("smtp_server")
        self.adder = os.environ.get("adder")
        self.pw = os.environ.get("pw")

    def noti(self, message, receiver):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            message = message.encode('utf-8')
            connection.starttls()
            connection.login(user=self.smtp_server, password=self.pw)
            for email in receiver:
                connection.sendmail(from_addr=self.adder,
                                    to_addrs=email, msg=message)
