import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_KNN_model.pgz','r') as f:
    KNN_Model = pickle.load(f)

def predict(input):
    pred=KNN_Model.predict(input)[0]
    print(pred)
    return pred