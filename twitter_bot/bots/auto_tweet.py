import tweepy
import time
from config import create_api
try:
  # For Python 3.0 and later
  from urllib.request import urlopen
except ImportError:
  # Fall back to Python 2's urllib2
  from urllib2 import urlopen

import json

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def main():
  #connect to twitter api
  api = create_api()
  counter = 1 
  #get the stock index data
  url = ("https://financialmodelingprep.com/api/v3/quotes/index?apikey=c7980289fb590120767b2b61fb70de61")
  data = get_jsonparsed_data(url)
  (next(item for item in data if item["symbol"] == "^DJI"))
  while (True):
    tweet = ""
  # DOWJONES
    if (counter%3 == 1):
      index = (next(item for item in data if item["symbol"] == "^DJI"))
      tweet = "                   ** DOW JONES update ** \n\n" + "Price:" + str(index["price"]) + "\nChange:"+ str(index["change"])  + "\nDay low:" + str(index["dayLow"]) +"\nDay High:" + str(index["dayHigh"]) +"\nOpen:" + str(index["open"]) + "\nLast close:" + str(index["previousClose"]) +"\n\n          **Updates every 30 minutes**\n" +"              *All data is in real time*"

    # NASDAQ
    elif (counter%3 == 2):
      index = (next(item for item in data if item["symbol"] == "^IXIC"))
      tweet = "                   ** NASDAQ Composite update ** \n\n" + "Price:" + str(index["price"]) + "\nChange:" + str(index["change"]) +"\nDay low:" + str(index["dayLow"]) +"\nDay High:" + str(index["dayHigh"]) +"\nOpen:" + str(index["open"]) + "\nLast close:" + str(index["previousClose"]) +"\n\n          **Updates every 30 minutes**\n" +"              *All data is in real time*"

    # 500
    else:
      index = (next(item for item in data if item["symbol"] == "^GSPC"))
      tweet = "                   ** S and P 500 update ** \n\n" + "Price:" + str(index["price"]) + "\nChange:"  +"\nDay low:" + str(index["dayLow"]) +"\nDay High:" + str(index["dayhigh"]) +"\nOpen:" + str(index["open"]) + "\nLast close:" + str(index["previousClose"]) +"\n\n          **Updates every 30 minutes**\n" +"              *All data is in real time*"

    counter += 1
  
    try:
      api.update_status(tweet)
    except tweepy.TweepError as error:
    #make exception for duplicate tweets
      if (error.api_code != 187):
        raise error

    # only post once every 10 mins 
    time.sleep(600)

if  __name__ =='__main__':main()