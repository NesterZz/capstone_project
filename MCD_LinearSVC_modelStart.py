import pickle
import gzip

with gzip.open(r'C:\Users\may\Desktop\FYP_VS\MCD\MCD_Linear_SVC_model.pgz','r') as f:
    Svc_Model = pickle.load(f)

def predict(input):
    pred=Svc_Model.predict(input)[0]
    print(pred)
    return pred