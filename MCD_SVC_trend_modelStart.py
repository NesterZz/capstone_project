import pickle
import gzip

company="MCD/MCD"
#company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_SVC_model_trend.pgz','r') as f:
    Svc_Model = pickle.load(f)

def predict(input):
    pred=Svc_Model.predict(input)[0]
    print(pred)
    return pred