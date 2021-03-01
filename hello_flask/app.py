
from flask import Flask
app = Flask(__name__)
from flask import jsonify
import requests


@app.route('/buy')
def buy():
    r = requests.get('https://api.exchangeratesapi.io/latest')
    json = r.json()
    rates_object = json['rates']
    buy_rates = {}
    for key,value in rates_object.items():
        cost = value / 100 * 2
        buy_rates[key] = round(value + cost, 5) 
    return jsonify(buy_rates)

@app.route('/sell')
def sell():
    r = requests.get('https://api.exchangeratesapi.io/latest')
    json = r.json()
    rates_object = json['rates']
    sell_rates = {}
    for key,value in rates_object.items():
        cost = value / 100 * 2
        sell_rates[key] = round(value - cost, 5) 
    return jsonify(sell_rates)
    

if __name__ == "__main__":
    app.run(debug=True)

