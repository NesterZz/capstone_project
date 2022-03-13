
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


from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.utils.vis_utils import plot_model
from keras.layers import Dense, LSTM, Dropout, TimeDistributed, Flatten, Bidirectional

#Scaling
scaler = MinMaxScaler()
feature_transform_train = scaler.fit_transform(numpy_df_train)
#feature_transform_train= pd.DataFrame(columns=features, data=feature_transform)
#feature_transform_train.head(7)
feature_transform_test = scaler.fit_transform(numpy_df_test)
#feature_transform_test= pd.DataFrame(columns=features, data=feature_transform)
#feature_transform_test.head(7)

#Process the data for LSTM
trainX =np.array(numpy_df_train)
testX =np.array(numpy_df_test)
X_train = trainX.reshape(numpy_df_train.shape[0], 1, numpy_df_train.shape[1])
X_test = testX.reshape(numpy_df_test.shape[0], 1, numpy_df_test.shape[1])
print(numpy_df_train)
#Building the LSTM Model
lstm = Sequential()


lstm.add(LSTM(16, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=True))
lstm.add(Dropout(0.1))
lstm.add(LSTM(32, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=True))
lstm.add(Dropout(0.1))
lstm.add(LSTM(64, input_shape=(1, trainX.shape[1]), activation='relu', return_sequences=False))
lstm.add(Dropout(0.1))
lstm.add(Dense(1))
lstm.compile(loss='mean_squared_error', optimizer='adam')

#Model Training
history=lstm.fit(X_train, y_train, epochs=200, batch_size=8, verbose=1, shuffle=False)

#LSTM Prediction
y_pred= lstm.predict(X_test)
print(y_pred)

#Predicted vs True Adj Close Value – LSTM
plt.plot(y_test, label='True Value')
plt.plot(y_pred, label='LSTM Value')
plt.title('Prediction by LSTM')
plt.xlabel('Time Scale')
plt.ylabel('Scaled USD')
plt.legend()
plt.savefig(company+"_LSTM.png")



from sklearn.metrics import r2_score

print(r2_score(y_test, y_pred))

# Save
import gzip
with gzip.GzipFile(company+'_LSTM_model.pgz', 'w') as f:
    pickle.dump(lstm,f)
print("Model saved!")