import pickle
import gzip

company="MCD/MCD"
#company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_KNN_model_more_trend.pgz','r') as f:
    KNN_Model = pickle.load(f)

with gzip.open(company+'_KNN_more_trend_Score.pgz','r') as e:
    acc = pickle.load(e)

def predict(input):
    pred=KNN_Model.predict(input)[0][0]
    print(pred)
    return pred

def acc2():
    return acc