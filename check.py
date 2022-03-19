import requests
from pprint import pprint



def check_price(step_day:str,first_value:str, to_value:str) -> dict:
    apikey='B7P8H10YEGLPB72Q'
    url = 'https://www.alphavantage.co/query?function=FX_'+step_day+'&from_symbol='+first_value+'&to_symbol=' + to_value + "&apikey=" +apikey
    r = requests.get(url)
    data = r.json()
    print(data)
    return data



def get_database():
    from pymongo import MongoClient
    import pymongo


    
    

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://Biba_buba_13:Vgfgh4335RTF@huyaster.bi6ms.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Value']

def To_mongo_DB():
    dbname = get_database()
    
    
if __name__ == "main":
    res = check_price("DAILY", "USD", "RUB")
    pprint(res)