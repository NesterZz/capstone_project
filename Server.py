from cmath import nan
from unittest import result
import numpy as np
import pandas
import MCD_KNN_modelStart
import MCD_KNN_trend_modelStart
import MCD_RandomForest_modelStart
import MCD_LogisticRegression_trend_modelStart
import MCD_DecisionTree_modelStart
import MCD_DecisionTree_trend_modelStart
import MCD_LinearSVR_modelStart
import MCD_NB_trend_modelStart
import MCD_LinearSVC_modelStart
import MCD_SVC_trend_modelStart
import MCD_LinearRegression_modelStart
import MCD_LinearRegression_more_modelStart
import MCD_KNN_more_modelStart
import AAPL_KNN_modelStart
import AAPL_KNN_trend_modelStart
import AAPL_RandomForest_modelStart
import AAPL_LinearRegression_modelStart
import AAPL_LogisticRegression_trend_modelStart
import AAPL_DecisionTree_modelStart
import AAPL_DecisionTree_trend_modelStart
import AAPL_LinearSVR_modelStart
import AAPL_NB_trend_modelStart
import AAPL_LinearSVC_modelStart
import AAPL_SVC_trend_modelStart
import AAPL_LinearRegression_more_modelStart
import AAPL_KNN_more_modelStart
import LSTM
import LSTM2
import GetTwitter
import GetTwitter_more

from flask import Flask, request,jsonify,redirect
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hi'

@app.route('/predict_KNN_MCD',methods=['POST'])
def post():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_KNN_modelStart.predict(input)
    r2 = MCD_KNN_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Rf_MCD',methods=['POST'])
def post2():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_RandomForest_modelStart.predict(input)
    r2 = MCD_RandomForest_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Dt_MCD',methods=['POST'])
def post3():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_DecisionTree_modelStart.predict(input)
    r2 = MCD_DecisionTree_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)})  
  

@app.route('/predict_Svr_MCD',methods=['POST'])
def post4():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVR_modelStart.predict(input)
    r2 = MCD_LinearSVR_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)})   

@app.route('/predict_Svc_MCD',methods=['POST'])
def post5():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVC_modelStart.predict(input)
    r2 = MCD_LinearSVC_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Lg_MCD',methods=['POST'])
def posts5():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearRegression_modelStart.predict(input)
    r2 = MCD_LinearSVC_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 
 

@app.route('/predict_KNN_AAPL',methods=['POST'])
def post6():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_KNN_modelStart.predict(input)
    r2 = AAPL_KNN_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Lg_AAPL',methods=['POST'])
def posts6():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LinearRegression_modelStart.predict(input)
    r2 = AAPL_LinearRegression_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Rf_AAPL',methods=['POST'])
def post7():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_RandomForest_modelStart.predict(input)
    r2 = AAPL_RandomForest_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Dt_AAPL',methods=['POST'])
def post8():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_DecisionTree_modelStart.predict(input)
    r2 = AAPL_DecisionTree_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)})    

@app.route('/predict_Svr_AAPL',methods=['POST'])
def post9():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LinearSVR_modelStart.predict(input)
    r2 = AAPL_LinearSVR_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)})   

@app.route('/predict_Svc_AAPL',methods=['POST'])
def post10():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LinearSVC_modelStart.predict(input)
    r2 = AAPL_LinearSVC_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)})   


@app.route('/scarpe',methods=['POST'])
def post11():
    insertVal = request.get_json()
    x1=insertVal['company']
    input=np.array([x1])
    result = GetTwitter.trytry(input)
    result2 = GetTwitter.trytry2(input)

    return jsonify({'return':str(result),'return2':str(result2)})  

@app.route('/scarpe_more',methods=['POST'])
def post112():
    insertVal = request.get_json()
    x1=insertVal['company']
    input=np.array([x1])
    result = GetTwitter_more.trytry(input)
    result2 = GetTwitter_more.trytry2(input)
    result3 = GetTwitter_more.trytry3(input)
    result4 = GetTwitter_more.trytry4(input)

    return jsonify({'return':str(result),'return2':str(result2),'return3':str(result3),'return4':str(result4)})  


@app.route('/predict_KNN_MCD_trend',methods=['POST'])
def post0():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_KNN_trend_modelStart.predict(input)
    acc = MCD_KNN_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})   

@app.route('/predict_DT_MCD_trend',methods=['POST'])
def post12():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_DecisionTree_trend_modelStart.predict(input)
    acc = MCD_DecisionTree_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})  

@app.route('/predict_LG_MCD_trend',methods=['POST'])
def post13():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LogisticRegression_trend_modelStart.predict(input)
    acc = MCD_LogisticRegression_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})    

@app.route('/predict_Svc_MCD_trend',methods=['POST'])
def post14():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_SVC_trend_modelStart.predict(input)
    acc = MCD_SVC_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})   

@app.route('/predict_NB_MCD_trend',methods=['POST'])
def post15():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_NB_trend_modelStart.predict(input)
    acc = MCD_NB_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})   

@app.route('/predict_KNN_AAPL_trend',methods=['POST'])
def post16():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_KNN_trend_modelStart.predict(input)
    acc = AAPL_KNN_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)}) 

@app.route('/predict_DT_AAPL_trend',methods=['POST'])
def post17():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_DecisionTree_trend_modelStart.predict(input)
    acc = AAPL_DecisionTree_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)}) 

@app.route('/predict_LG_AAPL_trend',methods=['POST'])
def post18():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LogisticRegression_trend_modelStart.predict(input)
    acc = AAPL_LogisticRegression_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})     

@app.route('/predict_Svc_AAPL_trend',methods=['POST'])
def post19():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_SVC_trend_modelStart.predict(input)
    acc = AAPL_SVC_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})    

@app.route('/predict_NB_AAPL_trend',methods=['POST'])
def post20():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_NB_trend_modelStart.predict(input)
    acc = AAPL_NB_trend_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)})     

@app.route('/predict_LSTM_MCD',methods=['POST'])
def post21():
    insertVal = request.get_json()
    x1=float(insertVal['good'])
    x2=float(insertVal['bad'])

    x_predict=np.array([[x1,x2]])
    x_predict = x_predict.reshape(x_predict.shape[0], 1, x_predict.shape[1])
    result = LSTM.predict(x_predict)

    r2_MCD = LSTM.r2score2()

    return jsonify({'return':str(result[0][0]),'r2':str(r2_MCD)}) 

@app.route('/predict_LSTM_AAPL',methods=['POST'])
def post22():
    insertVal = request.get_json()
    x1=float(insertVal['good'])
    x2=float(insertVal['bad'])

    x_predict=np.array([[x1,x2]])
    x_predict = x_predict.reshape(x_predict.shape[0], 1, x_predict.shape[1])
    result = LSTM2.predict(x_predict)
    r2_AAPL = LSTM2.r2score2()

    return jsonify({'return':str(result[0][0]),'r2':str(r2_AAPL)}) 

@app.route('/predict_Lg_MCD_more',methods=['POST'])
def post23():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    x3=insertVal['close']
    x4=insertVal['vol']
    input=np.array([[x1,x2,x3,x4]])
    result = MCD_LinearRegression_more_modelStart.predict(input)
    r2 = MCD_LinearRegression_more_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_Lg_AAPL_more',methods=['POST'])
def post24():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    x3=insertVal['close']
    x4=insertVal['vol']
    input=np.array([[x1,x2,x3,x4]])
    result = AAPL_LinearRegression_more_modelStart.predict(input)
    r2 = AAPL_LinearRegression_more_modelStart.r2score()

    return jsonify({'return':str(result),'r2':str(r2)}) 

@app.route('/predict_KNN_MCD_more',methods=['POST'])
def post25():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    x3=insertVal['close']
    x4=insertVal['vol']
    input=np.array([[x1,x2,x3,x4]])
    result = MCD_KNN_more_modelStart.predict(input)
    acc = MCD_KNN_more_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)}) 

@app.route('/predict_KNN_AAPL_more',methods=['POST'])
def post26():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    x3=insertVal['close']
    x4=insertVal['vol']
    input=np.array([[x1,x2,x3,x4]])
    result = AAPL_KNN_more_modelStart.predict(input)
    acc = AAPL_KNN_more_modelStart.acc2()

    return jsonify({'return':str(result),'acc':str(acc)}) 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1000, debug=True)