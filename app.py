# app.py

from flask import Flask, request,jsonify,render_template
import pickle
import numpy as np

#load the trained model
model_path='model.pkl'
with open(model_path,'rb')as file:
    model=pickle.load(file)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #extract data from form
    int_features=[float(x)for x in request.form.values()]
    final_features=[np.array(int_features)] 

    #make prediction
    prediction = model.predict(final_features)
    output= 'placed'if prediction[0]==1 else 'Not Placed'

    return render_template('index.html', prediction_text='Prediction:{}'.format(output))

if __name__=="__main__" :
    app.run(debug=True)       