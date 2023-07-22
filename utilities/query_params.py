from datetime import datetime, timedelta

from URLSearchParams import URLSearchParams

src = URLSearchParams("https://api.privatbank.ua/p24api/exchange_rates?json")


# api_pb = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=01.12.2014'

def create_urls(number):
    urls = []
    for i in range(number):
        delta = timedelta(days=i)
        query_date = ((datetime.now() - delta).strftime('%d.%m.%Y'))
        query_param = src.append({"date": query_date})
        urls.append(query_param)
    return urls


if __name__ == "__main__":
    print(create_urls(2))
