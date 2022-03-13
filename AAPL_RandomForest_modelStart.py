import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_RandomForest_model.pgz','r') as f:
    Rf_Model = pickle.load(f)

def predict(input):
    pred=Rf_Model.predict(input)[0]
    print(pred)
    return pred