import pickle
import gzip

with gzip.open(r'.\MCD.\MCD_Linear_SVR_model.pgz','r') as f:
    Svr_Model = pickle.load(f)

def predict(input):
    pred=Svr_Model.predict(input)[0]
    print(pred)
    return pred