from unittest import result
import numpy as np
import MCD_KNN_modelStart
import MCD_RandomForest_modelStart
import MCD_DecisionTree_modelStart
import MCD_LinearSVR_modelStart
import MCD_LinearSVC_modelStart


from flask import Flask, request,jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'hi'

@app.route('/predict_KNN',methods=['POST'])
def post():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_KNN_modelStart.predict(input)


    return jsonify({'return':str(result)})

@app.route('/predict_Rf',methods=['POST'])
def post2():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_RandomForest_modelStart.predict(input)


    return jsonify({'return':str(result)})

@app.route('/predict_Dt',methods=['POST'])
def post3():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_DecisionTree_modelStart.predict(input)


    return jsonify({'return':str(result)})    

@app.route('/predict_Svr',methods=['POST'])
def post4():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVR_modelStart.predict(input)


    return jsonify({'return':str(result)})   

@app.route('/predict_Svc',methods=['POST'])
def post5():
    insertVal = request.get_json()
    x1=insertVal['good']
    x2=insertVal['bad']
    input=np.array([[x1,x2]])
    result = MCD_LinearSVC_modelStart.predict(input)


    return jsonify({'return':str(result)})   



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000, debug=True)