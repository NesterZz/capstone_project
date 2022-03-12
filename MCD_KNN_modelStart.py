import pickle
import gzip

with gzip.open(r'C:\Users\may\Desktop\FYP_VS\MCD\MCD_KNN_model.pgz','r') as f:
    KNN_Model = pickle.load(f)

def predict(input):
    pred=KNN_Model.predict(input)[0]
    print(pred)
    return pred