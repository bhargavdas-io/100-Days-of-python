import requests
from twilio.rest import Client

STOCK_NAME = "NVDA"
COMPANY_NAME = "NVIDIA Corp."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = '7JS8GTEWPEHS7R13'
NEWS_API_KEY = '8ebbd9261c3a402b9d1ed14b9fe3c225'
TWILIO_SID = ''
TWILIO_AUTH = ''


stock_parameters = {
    "apikey": STOCK_API_KEY,
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "outputsize": 'compact'
}
url = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = url.json()['Time Series (Daily)']
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_data = stock_data_list[0]
closing_price_yesterday = yesterday_data['4. close']

closing_price = float(closing_price_yesterday)

print(closing_price)

day_before_yesterday_data = stock_data_list[1]
closing_price_day_before_yesterday = day_before_yesterday_data['4. close']

closing_price_2 = float(closing_price_day_before_yesterday)

print(closing_price_2)

difference = float(closing_price - closing_price_2)
up_down = None
if difference > 0:
    up_down = '⬆️'
else:
    up_down = '⬇️'

change_percent = round(float(difference / closing_price_2) * 100)

if abs(change_percent) > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "sortBy": 'publishedAt',
        "language": 'en'
    }

    connection = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = connection.json()['articles']
    three_articles = news_data[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{change_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    client = Client(TWILIO_SID, TWILIO_AUTH)
    for article in formatted_articles:
        message = client.messages.create(
          from_='whatsapp:+14155238886',
          body=article,
          to='whatsapp:YOUR_PHONE_NUMBER'
        )

