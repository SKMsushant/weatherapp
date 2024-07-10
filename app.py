from flask import Flask,render_template,request
import requests

app=Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index1.html")


@app.route("/weatherapp",methods=['GET','POST'])
def get_weatherdata():
    url="http://api.weatherapi.com/v1/current.json?key=9bf8826b1b274387a9d215720240907"
    param={'q':request.form.get("city"),
           'days':int(request.form.get("days")),
           }
    response=requests.get(url,params=param)
    
    data=response.json()
    city=data['name']
    return f"data:{data},city:{city}"


if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080)
