import pickle
import gzip

with gzip.open(r'.\MCD.\MCD_Linear_SVC_model.pgz','r') as f:
    Svc_Model = pickle.load(f)

def predict(input):
    pred=Svc_Model.predict(input)[0]
    print(pred)
    return pred