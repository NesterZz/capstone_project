import pickle
import gzip

company="MCD/MCD"
#company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_DecisionTree_model_trend.pgz','r') as f:
    Dt_Model = pickle.load(f)

def predict(input):
    pred=Dt_Model.predict(input)[0]
    print(pred)
    return pred

with gzip.open(company+'_DecisionTree_trend_Score.pgz','r') as e:
    acc = pickle.load(e)

def acc2():
    return acc