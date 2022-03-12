import pickle
import gzip

with gzip.open(r'.\MCD.\MCD_RandomForest_model.pgz','r') as f:
    Rf_Model = pickle.load(f)

def predict(input):
    pred=Rf_Model.predict(input)[0]
    print(pred)
    return pred