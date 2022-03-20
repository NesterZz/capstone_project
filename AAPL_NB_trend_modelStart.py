import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_NB_model_trend.pgz','r') as f:
    NB_Model = pickle.load(f)

def predict(input):
    pred=NB_Model.predict(input)[0]
    print(pred)
    return pred