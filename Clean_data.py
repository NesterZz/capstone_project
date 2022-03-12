import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import csv
plt.style.use('fivethirtyeight')


non_place_data = pd.read_csv(r"C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_scraped_tweets.csv", header=0,            
                  names=["date","tweet","tweet_id"])
print(non_place_data)
non_place_data['date'] = non_place_data['date'].replace({'date':''}) #remove redundant date
non_place_data['tweet'] = non_place_data['tweet'].replace({'tweet':''}) #remove redundant tweet
non_place_data['tweet_id'] = non_place_data['tweet_id'].replace({'tweet_id':''}) #remove redundant tweet_id
non_place_data['date'].replace('', np.nan, inplace=True) #change null data to np.nan
non_place_data.dropna(axis=0, how='any',inplace=True) #remove all null data

print (non_place_data.isnull().sum()) #check is there are any null data


non_place_data.to_csv(r"C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_placed_data.csv",index=False) #output the csv file by cleaning data in first step
abc=pd.read_csv(r"C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_placed_data.csv")
print(abc)

non_place_data.sort_values('date',ascending=False,inplace=True)
print(non_place_data)

#non_place_data['date'] =pd.to_datetime(non_place_data.date)
#non_place_data.sort('date', format="%d/%m/%Y") # This now sorts in date order

header = ['Tweet_Id','Date','Tweet']
with open(r'C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_cleaned.csv','w',encoding='utf-8', newline='') as data_csv:
    write=csv.writer(data_csv)
    write.writerow(header)
    
    for index,row in non_place_data.iterrows():
        stre=row["tweet"]
        if(type(stre)==str):
            clear_string = re.sub('[^a-zA-Z0-9]','',stre)
        else:
            clear_string=""
        import_array=[row["tweet_id"],row["date"],clear_string]
        write.writerow(import_array)


        
Test3 = pd.read_csv(r"C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_cleaned.csv")
Test3['Date']= Test3['Date'].str.split(" ", expand = True)[0] #reformat the data
Test3['Date'] = Test3['Date'].str.replace('/','-')

adata=pd.DataFrame(columns=['Date','Tweet'])
total=100
index=0
for index,row in Test3.iterrows():
    stre=row["Tweet"]
    my_new_string = re.sub('[^a-zA-Z0-9]', '', stre)
    temp_df = pd.DataFrame([[Test3["Date"].iloc[index], 
                            my_new_string]], columns = ['Date','Tweet'])
    adata = pd.concat([adata, temp_df], axis = 0).reset_index(drop = True)
    # index=index+1
#print(cdata.dtypes)



aadata=pd.DataFrame(columns=['Date','Tweet'])
pp=0
indx=0
get_tweet=""
for i in range(0,len(adata)-1):
    get_date=adata.Date.iloc[i]
    next_date=adata.Date.iloc[i+1]
    if(str(get_date)==str(next_date)):
        get_tweet=get_tweet+adata.Tweet.iloc[i]+" "
    if(str(get_date)!=str(next_date)):
        temp_df = pd.DataFrame([[get_date, 
                                get_tweet]], columns = ['Date','Tweet'])
       
        aadata = pd.concat([aadata, temp_df], axis = 0).reset_index(drop = True) #error
        get_tweet=" "
        

print(aadata)
aadata.to_csv(r"C:\Users\may\Desktop\FYP_VS\AAPL\Final_AAPL_cleaned.csv",index=False)

import pickle

#save

with open(r'C:\Users\may\Desktop\FYP_VS\AAPL\AAPL_cleaned.pickle', 'wb') as f:
    pickle.dump(aadata, f)

        
