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

non_place_data = pd.read_csv(company+"_scraped_tweets.csv", header=0,            
                  names=["date","tweet","tweet_id"])
print(non_place_data)
non_place_data['date'] = non_place_data['date'].replace({'date':''}) #remove redundant date
non_place_data['tweet'] = non_place_data['tweet'].replace({'tweet':''}) #remove redundant tweet
non_place_data['tweet_id'] = non_place_data['tweet_id'].replace({'tweet_id':''}) #remove redundant tweet_id
non_place_data['date'].replace('', np.nan, inplace=True) #change null data to np.nan
non_place_data.dropna(axis=0, how='any',inplace=True) #remove all null data

print (non_place_data.isnull().sum()) #check is there are any null data


non_place_data.to_csv(company+"_placed_data.csv",index=False) #output the csv file by cleaning data in first step
abc=pd.read_csv(company+"_placed_data.csv")
print(abc)

non_place_data.sort_values('date',ascending=False,inplace=True)
print(non_place_data)

#non_place_data['date'] =pd.to_datetime(non_place_data.date)
#non_place_data.sort('date', format="%d/%m/%Y") # This now sorts in date order

header = ['Tweet_Id','Date','Tweet']
with open(company+"_cleaned.csv",'w',encoding='utf-8', newline='') as data_csv:
    write=csv.writer(data_csv)
    write.writerow(header)
    
    for index,row in non_place_data.iterrows():
        stre=row["tweet"]
        if(type(stre)==str):
            clear_string = re.sub('[^a-zA-Z0-9]',' ',stre)
        else:
            clear_string=""
        import_array=[row["tweet_id"],row["date"],clear_string]
        write.writerow(import_array)


        
Test3 = pd.read_csv(company+"_cleaned.csv")
Test3['Date']= Test3['Date'].str.split(" ", expand = True)[0] #reformat the data
Test3['Date'] = Test3['Date'].str.replace('/','-')

adata=pd.DataFrame(columns=['Date','Tweet'])
total=100
index=0
for index,row in Test3.iterrows():
    stre=row["Tweet"]
    my_new_string = re.sub('[^a-zA-Z0-9]', ' ', stre)
    temp_df = pd.DataFrame([[Test3["Date"].iloc[index], 
                            my_new_string]], columns = ['Date','Tweet'])
    adata = pd.concat([adata, temp_df], axis = 0).reset_index(drop = True)
    # index=index+1
#print(cdata.dtypes)

print(adata)

adata["Comp"] = ''
adata["Negative"] = ''
adata["Neutral"] = ''
adata["Positive"] = ''

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import unicodedata
sentiment_i_a = SentimentIntensityAnalyzer()
for indexx, row in adata.T.iteritems():
    try:
        sentence_i = unicodedata.normalize('NFKD', adata.loc[indexx, 'Tweet'])
        sentence_sentiment = sentiment_i_a.polarity_scores(sentence_i)
        adata['Comp'].loc[indexx] = sentence_sentiment['compound']
        adata['Negative'].loc[indexx] = sentence_sentiment['neg']
        adata['Neutral'].loc[indexx] = sentence_sentiment['neu']
        adata['Positive'].loc[indexx] = sentence_sentiment['compound']
    except TypeError:
        print (adata.loc[indexx, 'Tweet'])
        print (indexx)
print(adata)


aadata=pd.DataFrame(columns=['Date','Comp','Negative','Neutral','Positive'])
count=0
comp=0
neg=0
neu=0
pos=0
for i in range(0,len(adata)-1):
    get_date=adata.Date.iloc[i]
    next_date=adata.Date.iloc[i+1]
    if(str(get_date)==str(next_date)):
        comp=adata.Comp.iloc[i+1]+adata.Comp.iloc[i]
        neg=adata.Negative.iloc[i+1]+adata.Negative.iloc[i]
        neu=adata.Neutral.iloc[i+1]+adata.Neutral.iloc[i]
        pos=adata.Positive.iloc[i+1]+adata.Positive.iloc[i]
        count=count+1
    if(str(get_date)!=str(next_date)):
        comp=comp/count
        neg=neg/count
        neu=neu/count
        pos=pos/count
        temp_df = pd.DataFrame([[get_date, 
                                comp,neg,neu,pos]], columns = ['Date','Comp','Negative','Neutral','Positive'])
       
        aadata = pd.concat([aadata, temp_df], axis = 0).reset_index(drop = True) #error
        count=0
        comp=0
        neg=0
        neu=0
        pos=0
        

print(aadata)


        
df_Company =pd.read_csv(company+"_Price.csv")
print("Show the price data")
print(df_Company)

aadata['Prices']=''

indx=0
for i in range (0,len(aadata)):
    for j in range (0,len(df_Company)):
        get_tweet_date=aadata.Date.iloc[i]
        get_stock_date=df_Company.Date.iloc[j]
        if(str(get_stock_date)==str(get_tweet_date)):
            #print(get_stock_date," ",get_tweet_date)
            # ccdata.set_value(i,'Prices',int(read_stock_p.Close[j]))
            aadata['Prices'].iloc[i] = int(df_Company.Close[j])
print(aadata)


#for i in range(0,len(new_dict)):
#    if(new_dict.Prices.iloc[i]==""):
#        new_dict.Prices.iloc[i]=new_dict.Prices.iloc[i-1]
#print(new_dict)

aadata['Prices'].replace('', np.nan, inplace=True) #change null data to np.nan
aadata.dropna(axis=0, how='any',inplace=True) #remove all null data
aadata.reset_index(drop=True, inplace=True)
print(aadata)



test_end_index = 0
train_start_index = aadata.shape[0]-1
train_end_index = int(aadata.shape[0]*0.3)
test_start_index = train_end_index-1

train = aadata.loc[train_end_index:train_start_index]
print(train)
test = aadata.loc[test_end_index:test_start_index]
print(test)
sentiment_score_list = []
for date, row in train.T.iteritems():
    sentiment_score = np.asarray([aadata.loc[date, 'Negative'],aadata.loc[date, 'Positive']])
    sentiment_score_list.append(sentiment_score)
numpy_df_train = np.asarray(sentiment_score_list)
#print(numpy_df_train)
numpy_df_train.shape

sentiment_score_list = []
for date, row in test.T.iteritems():
    sentiment_score = np.asarray([aadata.loc[date, 'Negative'],aadata.loc[date, 'Positive']])
    sentiment_score_list.append(sentiment_score)
numpy_df_test = np.asarray(sentiment_score_list)
y_train = pd.DataFrame(train['Prices'])
y_test = pd.DataFrame(test['Prices'])


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report,confusion_matrix
#use RandomForest train
rf = RandomForestRegressor()
rf.fit(numpy_df_train, y_train)
prediction = rf.predict(numpy_df_test)
print(prediction)
print(prediction.shape)


idx=np.arange(int(test_end_index),int(test_start_index)+1)
predictions_df_ = pd.DataFrame(data=prediction[0:], index = idx, columns=['Prices'])
print(predictions_df_)


from sklearn.metrics import r2_score
print(r2_score(y_test, prediction))




