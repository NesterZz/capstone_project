from unittest import result
import numpy as np
import MCD_KNN_modelStart
import MCD_RandomForest_modelStart
import MCD_DecisionTree_modelStart
import MCD_LinearSVR_modelStart
import MCD_LinearSVC_modelStart
import AAPL_KNN_modelStart
import AAPL_RandomForest_modelStart
import AAPL_DecisionTree_modelStart
import AAPL_LinearSVR_modelStart
import AAPL_LinearSVC_modelStart

from flask import Flask, request,jsonify
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


    return jsonify({'return':str(result)})

@app.route('/predict_Rf_MCD',methods=['POST'])
def post2():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_RandomForest_modelStart.predict(input)


    return jsonify({'return':str(result)})

@app.route('/predict_Dt_MCD',methods=['POST'])
def post3():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_DecisionTree_modelStart.predict(input)


    return jsonify({'return':str(result)})    

@app.route('/predict_Svr_MCD',methods=['POST'])
def post4():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVR_modelStart.predict(input)


    return jsonify({'return':str(result)})   

@app.route('/predict_Svc_MCD',methods=['POST'])
def post5():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVC_modelStart.predict(input)


    return jsonify({'return':str(result)})   

@app.route('/predict_KNN_AAPL',methods=['POST'])
def post6():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_KNN_modelStart.predict(input)


    return jsonify({'return':str(result)})

@app.route('/predict_Rf_AAPL',methods=['POST'])
def post7():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_RandomForest_modelStart.predict(input)


    return jsonify({'return':str(result)})

@app.route('/predict_Dt_AAPL',methods=['POST'])
def post8():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_DecisionTree_modelStart.predict(input)


    return jsonify({'return':str(result)})    

@app.route('/predict_Svr_AAPL',methods=['POST'])
def post9():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LinearSVR_modelStart.predict(input)


    return jsonify({'return':str(result)})   

@app.route('/predict_Svc_AAPL',methods=['POST'])
def post10():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = AAPL_LinearSVC_modelStart.predict(input)


    return jsonify({'return':str(result)})   

@app.route('/scarpe',methods=['POST'])
def post11():
    print('hi')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)