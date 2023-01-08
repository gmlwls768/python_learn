from pandas import *
import random
import smtplib
import datetime as dt

my_email = "email@gmail.com"
password = "pw"  # google app pw
default_receiver = "email@naver.com"

now = dt.datetime.now()
now_year = now.year
now_month = now.month
now_date = now.day
now_day_of_week = now.weekday()


def send_email(title, body, receiver):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver, msg=f"Subject:{title} \n\n {body}")


quote_list = []
if now_day_of_week == 0:  # monday_quote
    with open("Day_032/quotes.txt") as quote:
        for line in quote:
            line = line.strip("\n")
            quote_list.append(line)

    pick = random.choice(quote_list)
    send_email("cheer up", pick, default_receiver)

csv_read = read_csv("Day_032/birthdays.csv")
csv_read = csv_read.to_dict("records")


for birth in csv_read:  # birthday email
    if birth['month'] == now_month and birth['day'] == now_date:
        random_letter_num = random.randint(1, 3)
        with open(f"Day_032/letter_templates/letter_{random_letter_num}.txt") as template:
            lines = template.read()
            lines = lines.replace("[NAME]", birth['name'])
        send_email("Happy birthday", lines, birth['email'])
