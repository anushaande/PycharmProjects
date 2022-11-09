import requests
from datetime import date
from datetime import timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_KEY = "EP74CQWPD70RXM6R"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_KEY = "562cfb9bb8114892a3241a2c416ca944"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
today = date.today()  # - timedelta(days=8)
yesterday = today - timedelta(days=1)
previous_day = today - timedelta(days=2)
try:
    original_price = float(data["Time Series (Daily)"][str(previous_day)]['4. close'])
    yesterday_price = float(data["Time Series (Daily)"][str(yesterday)]['4. close'])
    if yesterday_price - original_price > 0:
        increased = True
    else:
        increased = False

    price_diff = abs(yesterday_price - original_price)

    percent_diff = (price_diff / original_price) * 100
    print(f"Percentage of difference between {yesterday} and {previous_day} is {percent_diff}")
except KeyError:
    print("Stock prices are stable.")
    percent_diff = 0.00

## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
news_params = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY
}

news = requests.get(NEWS_ENDPOINT, params=news_params)
news.raise_for_status()
news_data = news.json()
article_list = news_data["articles"][:3]
if percent_diff > 5:
    for article in article_list:
        if price_diff is increased:
            print(f"TSLA: 🔺{percent_diff}%")
        if price_diff is not increased:
            print(f"TSLA: 🔻{percent_diff}%")
        print(f"Headline: {article['title']} \nBrief: {article['description']}")
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
