import pickle
import gzip

company="MCD/MCD"
#company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_Linear_SVC_model.pgz','r') as f:
    Svc_Model = pickle.load(f)

with gzip.open(company+'_Linear_SVC_score.pgz','r') as e:
    r2 = pickle.load(e)

def predict(input):
    pred=Svc_Model.predict(input)[0]
    print(pred)
    return pred

def r2score():
    return r2