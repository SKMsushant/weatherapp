from flask import Flask,render_template,request
import requests

app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index1.html")


@app.route("/weatherapp",methods=['GET','POST'])
def get_weatherdata():
    url="http://api.weatherapi.com/v1/current.json?key=fe233e7c62774816bde163107240801"
    param={'q':request.form.get("city"),
           'days':int(request.form.get("days")),
           }
    response=requests.get(url,params=param)
    city=data['name']
    data=response.json()
    return f"data:{data},city:{city}"


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5001)
