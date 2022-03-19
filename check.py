import requests


def check_price(step_day:str,first_value:str, to_value:str) -> dict:
    apikey='B7P8H10YEGLPB72Q'
    url = 'https://www.alphavantage.co/query?function=FX_'+step_day+'&from_symbol='+first_value+'&to_symbol=' + to_value + "&apikey=" +apikey
    r = requests.get(url)
    data = r.json()

    return data

