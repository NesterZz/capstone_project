import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import csv
plt.style.use('fivethirtyeight')

#company="MCD"
company="AAPL"
#company="KO"


consumer_key = 'orpXLO360oW1Gd6NVubof3he1'
consumer_secret = 'pUsywlNahbUGD73OFmMFo17qGu3ouuMsmZku2UaeCi4gdWTG7p'
access_token = '1457356059195023370-rHAuDBlBW2QNFoSVvlUsOmx0EX4UjI'
access_token_secret = 'mhTBH2EvsmyC5FiMsL3xM7W09fyTGKnSo8xHrAFM2u52Z'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweet_url = pd.read_csv(r'C:\Users\may\Desktop\AAPL.txt', index_col= None, header = None, names = ["tweet_urls"])
tweet_url.head()

#Extract the tweet id
af = lambda x: x["tweet_urls"].split("/")[-1]
#store tweet id in another column
tweet_url['tweet_id'] = tweet_url.apply(af, axis=1)

tweet_url.head()
ids = tweet_url['tweet_id'].tolist()

total_count = len(ids)
chunks = (total_count - 1) // 50 + 1
chunks


def fetch_tw(ids):
    tw_statuses = api.lookup_statuses(ids, tweet_mode= "extended")
    data = pd.DataFrame()
    for status in tw_statuses:
            tweet_elem = {"date":status.created_at,
                     "tweet":status.full_text,
                     "tweet_id": status.id
                     }
            data = data.append(tweet_elem, ignore_index = True)
    data.to_csv("C:/Users/may/Desktop/FYP_VS/"+company+"/AAPL_scraped_tweets.csv", mode="a")

for i in range(chunks):
        try:
                lst = ids[i*100:(i+1)*100]
                result = fetch_tw(lst)
        except:
                print('')

