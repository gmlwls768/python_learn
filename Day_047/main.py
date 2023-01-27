from bs4 import BeautifulSoup
import requests
import smtplib
import os
uri = "https://www.amazon.com/CORSAIR-MK-2-Mechanical-Gaming-Keyboard/dp/B07D5S54C6/ref=sr_1_1?keywords=k70&qid=1674796195&sprefix=%2Caps%2C307&sr=8-1&th=1"
response = requests.get(
    uri,
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
             "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"})
soup = BeautifulSoup(response.text, "lxml")
dollar = soup.find(name="span", class_="a-price-whole").getText()
cent = soup.find(name="span", class_="a-price-fraction").getText()
# User-Agent
dollar = dollar.split(" ")[0]
money = float(dollar + cent)
setmoney = 159

if money <= setmoney:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        my_email = os.environ.get("my_email")
        password = os.environ.get("password")
        receiver = os.environ.get("receiver")
        title = "Amazon Price Alert!"
        product_name = soup.find(name="span", id="productTitle").getText()

        body = f"hot deal! \n name:{product_name} is now {money} \n uri:{uri}"
        connection.ehlo()
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver, msg=f"Subject:{title} \n\n {body}")
