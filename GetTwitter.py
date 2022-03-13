import requests
import pandas as pd
import numpy as np
from datetime import timedelta, date
import calendar;
import time;
from nltk.sentiment import SentimentIntensityAnalyzer


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

bearer_token = "AAAAAAAAAAAAAAAAAAAAAHLhXAEAAAAAemrz8VFE6iDwMRS5JYSNkYqlks0%3Di9w32blE8vZ2VEPRzYXrqBU0AyizhpAWyqgRpBFKHYPcDbUVZr"

today_date = date.today()
start_day_date = today_date - timedelta(days=8)

today = today_date.strftime("%Y-%m-%d")
start_day = start_day_date.strftime("%Y-%m-%d")

datelist = pd.date_range(start = start_day ,end = today)

def get_tweets_data(tweet):
    data = {
        'id': tweet['id_str'],
        'created_at': tweet['created_at'],
        'text': tweet['full_text']
    }
    return data

tweet_df = pd.DataFrame()

keyword = 'AAPL'

for until_date in datelist:
    params = {'q': keyword,
            'tweet_mode': 'extended',
            'lang':'en',
            'count':'100',
            'until': until_date.strftime("%Y-%m-%d")}

    r = requests.get(
        'https://api.twitter.com/1.1/search/tweets.json', params=params,
        headers={
                'authorization': 'Bearer ' + bearer_token
            }
    )

    for tweet in r.json()['statuses']:
        row = get_tweets_data(tweet)
        tweet_df = tweet_df.append(row, ignore_index=True)

pd.set_option("max_rows", 10)



tweet_df["Comp"] = ''
tweet_df["Negative"] = ''
tweet_df["Neutral"] = ''
tweet_df["Positive"] = ''

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
sentiment_i_a = SentimentIntensityAnalyzer()
for indexx, row in tweet_df.T.iteritems():
    try:
        sentence_i = unicodedata.normalize('NFKD', tweet_df.loc[indexx, 'text'])
        sentence_sentiment = sentiment_i_a.polarity_scores(sentence_i)
        tweet_df['Comp'].loc[indexx] = sentence_sentiment['compound']
        tweet_df['Negative'].loc[indexx] = sentence_sentiment['neg']
        tweet_df['Neutral'].loc[indexx] = sentence_sentiment['neu']
        tweet_df['Positive'].loc[indexx] = sentence_sentiment['compound']
    except TypeError:
        print (tweet_df.loc[indexx, 'tweet'])
        print (indexx)
print(tweet_df)
pos=tweet_df['Positive'].mean()
print(tweet_df['Positive'].mean())
neg=tweet_df['Negative'].mean()
print(tweet_df['Negative'].mean())

