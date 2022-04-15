from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/i2', methods=['POST', 'GET'])
def i2():
    city = request.form['city']
    # state = request.form['state']
    # country = request.form['country']

    a = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=65dc9f64995b633d2c7df3534dabd007')
    j_o = a.json()
    temp_k = float(j_o['main']['temp'])
    w_i=j_o['weather'][0]['icon']
    temp_c = temp_k - 273
    # ap1 = requests.get(api.openweathermap.org/data/2.5/weather?q=+city+,state&appid={API key})
    # ap2 = requests.get(api.openweathermap.org/data/2.5/weather?q=city,state,country&appid={API key})

    return render_template('i2.html', city=city, temp=temp_c,weather_icon=w_i)
    #return j_o
#weather_des=w_d,

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
