
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import csv
plt.style.use('fivethirtyeight')

company="MCD/MCD"
#company="AAPL/AAPL"
#company="KO/KO"

company_name="MCD"
#company_name="AAPL"
#company_name="KO"


import pickle
# Load
with open(company+'_cleaned.pickle', 'rb') as f:
    new_dict = pickle.load(f)
print("Show the cleaned data")
print(new_dict)

df_Company =pd.read_csv(company+"_Price.csv")
print("Show the price data")
print(df_Company)

new_dict['Prices']=''

indx=0
for i in range (0,len(new_dict)):
    for j in range (0,len(df_Company)):
        get_tweet_date=new_dict.Date.iloc[i]
        get_stock_date=df_Company.Date.iloc[j]
        if(str(get_stock_date)==str(get_tweet_date)):
            #print(get_stock_date," ",get_tweet_date)
            # ccdata.set_value(i,'Prices',int(read_stock_p.Close[j]))
            new_dict['Prices'].iloc[i] = int(df_Company.Close[j])
print(new_dict)


#for i in range(0,len(new_dict)):
#    if(new_dict.Prices.iloc[i]==""):
#        new_dict.Prices.iloc[i]=new_dict.Prices.iloc[i-1]
#print(new_dict)

new_dict['Prices'].replace('', np.nan, inplace=True) #change null data to np.nan
new_dict.dropna(axis=0, how='any',inplace=True) #remove all null data
new_dict.reset_index(drop=True, inplace=True)
print(new_dict)

#Making "prices" column as integer so mathematical operations could be performed easily.
new_dict['Prices'] = new_dict['Prices'].apply(np.int64)

new_dict["Comp"] = ''
new_dict["Negative"] = ''
new_dict["Neutral"] = ''
new_dict["Positive"] = ''

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
sentiment_i_a = SentimentIntensityAnalyzer()
for indexx, row in new_dict.T.iteritems():
    try:
        sentence_i = unicodedata.normalize('NFKD', new_dict.loc[indexx, 'Tweet'])
        sentence_sentiment = sentiment_i_a.polarity_scores(sentence_i)
        new_dict['Comp'].loc[indexx] = sentence_sentiment['compound']
        new_dict['Negative'].loc[indexx] = sentence_sentiment['neg']
        new_dict['Neutral'].loc[indexx] = sentence_sentiment['neu']
        new_dict['Positive'].loc[indexx] = sentence_sentiment['compound']
    except TypeError:
        print (new_dict.loc[indexx, 'Tweet'])
        print (indexx)
print(new_dict)

train_Company=new_dict[['Date','Prices','Comp','Negative','Neutral','Positive']].copy()
print(train_Company)

test_end_index = 0
train_start_index = train_Company.shape[0]-1
train_end_index = int(train_Company.shape[0]*0.3)
test_start_index = train_end_index-1

train = train_Company.loc[train_end_index:train_start_index]
print(train)
test = train_Company.loc[test_end_index:test_start_index]
print(test)
sentiment_score_list = []
for date, row in train.T.iteritems():
    sentiment_score = np.asarray([train_Company.loc[date, 'Negative'],train_Company.loc[date, 'Positive']])
    sentiment_score_list.append(sentiment_score)
numpy_df_train = np.asarray(sentiment_score_list)
#print(numpy_df_train)
numpy_df_train.shape

sentiment_score_list = []
for date, row in test.T.iteritems():
    sentiment_score = np.asarray([train_Company.loc[date, 'Negative'],train_Company.loc[date, 'Positive']])
    sentiment_score_list.append(sentiment_score)
numpy_df_test = np.asarray(sentiment_score_list)
y_train = pd.DataFrame(train['Prices'])
y_test = pd.DataFrame(test['Prices'])


#use DT
from sklearn.tree import DecisionTreeClassifier

model=DecisionTreeClassifier(max_depth=2,criterion='entropy')
model.fit(numpy_df_train, y_train)
prediction = model.predict(numpy_df_test)
print(prediction)



idx=np.arange(int(test_end_index),int(test_start_index)+1)
predictions_df_ = pd.DataFrame(data=prediction[0:], index = idx, columns=['Prices'])
print(predictions_df_)

from sklearn.metrics import r2_score
print(r2_score(y_test, prediction))
r2score=r2_score(y_test, prediction)

ax = predictions_df_.rename(columns={"Prices": "predicted_price"}).plot(title=company_name+' Decision Tree predicted prices')#predicted value
ax.set_xlabel("Indexes")
ax.set_ylabel("Stock Prices")
fig = y_test.rename(columns={"Prices": "actual_price"}).plot(ax = ax).get_figure()#actual value
fig.savefig(company+"_Decision_Tree.png")

# Save
import gzip
with gzip.GzipFile(company+'_DecisionTree_model.pgz', 'w') as f:
    pickle.dump(model,f)
print("Model saved!")
with gzip.GzipFile(company+'_DecisionTree_Score.pgz', 'w') as e:
    pickle.dump(r2score,e)