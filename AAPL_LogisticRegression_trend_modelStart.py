import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_LogisticRegression_model_trend.pgz','r') as f:
    LG_Model = pickle.load(f)

def predict(input):
    pred=LG_Model.predict(input)[0]
    print(pred)
    return pred