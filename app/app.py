import pickle
import pandas as pd
from flask import Flask, jsonify

# Carregar o modelo treinado
with open('/compartilhado/modelo.pkl', 'rb') as arquivo:
    model = pickle.load(arquivo)

with open('/compartilhado/scaler.sav', 'rb') as arquivo2:
    scaler = pickle.load(arquivo2)    

app = Flask(__name__)
@app.route('/predict/<dic>')
def homepage(dic):
    
    dicAux = dic
       
    list_ = list(map(float, dic.split()))   

    x_scaler = scaler.transform([list_])  
    
    prediction = model.predict(x_scaler)
  
    resp = prediction[0][1]
    
    return jsonify(str(resp))

if __name__ == '__main__':
    app.run()
