from flask import Flask,request
import torch 
import googlemaps
from const import API_KEY,CURRENT_FEATURES
from locationAnalize import extractData

gmaps = googlemaps.Client(API_KEY)
l = torch.load('tempmodel.h5')

app = Flask(__name__)

@app.route('/')
def home():
    return "Location intelligence API"
    
@app.route('/rate/',methods=['GET','POST'])
def rate():
    data = request.get_json()
    latitude = data["latitude"]
    longtiude = data["longtiude"]
    result = extractData(CURRENT_FEATURES,latitude,longtiude)
    result_float = []
    for item in list(result.values()):
        result_float.append(float(item))
    test_values = torch.tensor([result_float])
    rate = torch.argmax(
    torch.softmax(l(test_values),1), axis = 1)
    result["rating"] = rate.item()
    return result
if __name__ == '__main__':
    app.run(debug=True)