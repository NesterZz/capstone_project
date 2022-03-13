import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_Linear_SVR_model.pgz','r') as f:
    Svr_Model = pickle.load(f)

def predict(input):
    pred=Svr_Model.predict(input)[0]
    print(pred)
    return pred