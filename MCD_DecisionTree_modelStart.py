import pickle
import gzip

with gzip.open(r'.\MCD.\MCD_DecisionTree_model.pgz','r') as f:
    Dt_Model = pickle.load(f)

def predict(input):
    pred=Dt_Model.predict(input)[0]
    print(pred)
    return pred