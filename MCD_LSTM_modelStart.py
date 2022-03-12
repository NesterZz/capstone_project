import pickle
import gzip

with gzip.open(r'.\MCD.\MCD_LSTM_model.pgz','r') as f:
    Lstm_Model = pickle.load(f)

def predict(input):
    pred=Lstm_Model.predict(input)[0]
    print(pred)
    return pred