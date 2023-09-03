from flask import Flask, render_template, request, redirect, url_for
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST','GET'])
def get_input():
    if request.method == 'POST':
        info = request.form['search']
        return redirect(url_for('run_pred',values=info))

@app.route('/run_pred/<values>')
def run_pred(values):
    import numpy as np 
    
    values = values.split(',')
    values = np.array(values).astype('float')
    values = values.reshape(1,-1)
    
    with open('RandomForest_model', 'rb') as file:
        pickle_model = pickle.load(file)
        
    model = pickle_model
    pred = model.predict(values)
    
    if pred == 0:
        return 'Our model predicts that the flight is delayed'
    return 'Our model predicts that the flight is on time!'
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)