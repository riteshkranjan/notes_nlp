from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
from notes_processing  import notes_nlp as nn

#from predict_fail_processing import premade_estimator as pe

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/process_nlp/<data>")
def parse_get(data):
    #print data
    response = {'debugInfo': 'some debug info', 'predictions': [{'name': nn.apply_nlp(data), 'percentage': round(nn.get_accuracy()*100,2), 'priority': 0}]}
    return jsonify(response)

@app.route('/process_nlp', methods = ['POST'])
def parse_post():   
    # print("start")
    # print(request.headers['Content-Type'])
    # print(request.data.decode("utf-8"))
    # print("end")
    s = request.data.decode("utf-8")
    start = "Ring ahead information ends==="
    end = "Please see additional information"
    sIndx = s.index(start) + len(start) if start in s else 0 
    eIndx = s.index(end) if end in s else len(s)
    newS = s[sIndx:eIndx]
    #print newS    
    response = {'debugInfo': newS.strip(), 'predictions': [{'name': nn.apply_nlp(newS.strip()), 'percentage': round(nn.get_accuracy()*100,2), 'priority': 0}]} 
    return jsonify(response)

"""
@app.route("/predict/<data>")
def predict(data):
    print(data)
    output, probability, predict_x =  pe.predict_fail(data)
    response = {'debugInfo': predict_x, 'predictions': [{'name': output, 'percentage': round(probability*100,2), 'priority': 0}]}
    return jsonify(response)
"""

