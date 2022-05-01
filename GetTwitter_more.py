import requests
import pandas as pd
import numpy as np
from datetime import timedelta, date
import calendar;
import time;
from nltk.sentiment import SentimentIntensityAnalyzer
import sys
import json
import pandas_datareader as pdr
from datetime import datetime, date
import dataframe_image as dfi
import re


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

pos=tweet_df['Positive'].mean()

neg=tweet_df['Negative'].mean()



def trytry(input):
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHLhXAEAAAAAemrz8VFE6iDwMRS5JYSNkYqlks0%3Di9w32blE8vZ2VEPRzYXrqBU0AyizhpAWyqgRpBFKHYPcDbUVZr"

    today_date = date.today()
    start_day_date = today_date - timedelta(days=8)

    today = today_date.strftime("%Y-%m-%d")
    start_day = start_day_date.strftime("%Y-%m-%d")

    datelist = pd.date_range(start = start_day ,end = today)
    tweet_df = pd.DataFrame()

    keyword = input

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
    
    pos=tweet_df['Positive'].mean()
   
    neg=tweet_df['Negative'].mean()
    
    return pos

def trytry2(input):
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAHLhXAEAAAAAemrz8VFE6iDwMRS5JYSNkYqlks0%3Di9w32blE8vZ2VEPRzYXrqBU0AyizhpAWyqgRpBFKHYPcDbUVZr"

    today_date = date.today()
    start_day_date = today_date - timedelta(days=8)

    today = today_date.strftime("%Y-%m-%d")
    start_day = start_day_date.strftime("%Y-%m-%d")

    datelist = pd.date_range(start = start_day ,end = today)
    tweet_df = pd.DataFrame()

    keyword = input

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
    
    pos=tweet_df['Positive'].mean()
    
    neg=tweet_df['Negative'].mean()
    

    df2=tweet_df[['text','Positive','Negative']]
    print(df2)


    adata=pd.DataFrame()
    aadata=pd.DataFrame()
    for index,row in df2.iterrows():
        stre=row["text"]
        my_new_string = re.sub('[^a-zA-Z0-9:/@#-.% ]', '', stre)
        temp_df = pd.DataFrame([[my_new_string,df2['Positive'].iloc[index],df2['Negative'].iloc[index]]], columns = ['Tweet','Pos','Neg'])
        adata = pd.concat([adata, temp_df], axis = 0).reset_index(drop = True)
    print(adata)
    for x in range(0,9):
        temp_df = pd.DataFrame([[adata['Tweet'].iloc[x],adata['Pos'].iloc[x],adata['Neg'].iloc[x]]], columns = ['Tweet','Pos','Neg'])
        aadata = pd.concat([aadata, temp_df], axis = 0).reset_index(drop = True)
    print(aadata)

    pd.options.display.max_colwidth=500
    dfi.export(aadata, 'more_dataframe.png',max_rows=1000)

    return neg    

def trytry3(input):
    if input=='aapl':
        input="AAPL"
    elif input=='mcd':
        input="MCD"
    
    yesterday = date.today() - timedelta(days = 1)

    ibm = pdr.get_data_yahoo(symbols=input, start = yesterday, end = yesterday)
    close=ibm['Close'][0]
    return close

def trytry4(input): 
    if input=='aapl':
        input="AAPL"
    elif input=='mcd':
        input="MCD"

    yesterday = date.today() - timedelta(days = 1)

    ibm = pdr.get_data_yahoo(symbols=input, start = yesterday, end = yesterday)
    vol=ibm['Volume'][0]
    return vol