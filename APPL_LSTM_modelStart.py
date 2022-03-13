import pickle
import gzip

#company="MCD/MCD"
company="AAPL/AAPL"
#company="KO/KO"

with gzip.open(company+'_LSTM_model.pgz','r') as f:
    Lstm_Model = pickle.load(f)

def predict(input):
    pred=Lstm_Model.predict(input)[0]
    print(pred)
    return pred