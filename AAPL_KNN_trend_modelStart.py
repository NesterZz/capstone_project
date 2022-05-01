import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_KNN_model_trend.pgz','r') as f:
    KNN_Model = pickle.load(f)

def predict(input):
    pred=KNN_Model.predict(input)[0]
    print(pred)
    return pred

with gzip.open(company+'_KNN_trend_Score.pgz','r') as e:
    acc = pickle.load(e)

def acc2():
    return acc