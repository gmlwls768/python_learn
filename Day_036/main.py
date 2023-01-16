import requests
import datetime as dt
from twilio.rest import Client
import os

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
my_number = os.environ.get("my_number")
twilio_number = os.environ.get("twilio_number")
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
stock_api_key = os.environ.get("stock_api_key")
news_api_key = os.environ.get("news_api_key")
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": stock_api_key,
    "outputsize": "compact"
}
url = 'https://www.alphavantage.co/query'
response = requests.get(url=url, params=parameters)
response.raise_for_status()
read = response.json()["Time Series (Daily)"]
yesterday = list(read.keys())[0]
day_berfore_yesterday = list(read.keys())[1]
yesterday_value = float(read[yesterday]["4. close"])
day_berfore_yesterday_value = float(read[day_berfore_yesterday]["4. close"])
difference = float(yesterday_value) - float(day_berfore_yesterday_value)
dif_per = (difference/yesterday_value) * 100
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# https://newsapi.org/v2/everything?q=Apple&from=2023-01-13&sortBy=popularity&apiKey=API_KEY
if abs(dif_per) >= 5:
    parameters = {
        "q": COMPANY_NAME,
        "from": day_berfore_yesterday,
        "to": yesterday,
        "apikey": news_api_key,
        "pageSize": 3
    }
    response = requests.get(
        "https://newsapi.org/v2/everything", params=parameters)
    response.raise_for_status()
    article = response.json()["articles"]
    three_article = article[:3]
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if difference >= 0:
    symbol = "🔺"
else:
    symbol = "🔻"
dif_per = round(dif_per, 2)
symbol_text = f"{symbol}{dif_per}%"
news_text = [
    f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_article]

client = Client(account_sid, auth_token)
message = client.messages \
    .create(
        body=f"{symbol_text} /n {news_text}",
        from_=twilio_number,
        to=my_number
    )
print(message.status)
# Optional: Format the SMS message like this:
"""

TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
