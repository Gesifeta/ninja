from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    year = datetime.date.today().year
    return render_template("index.html",year=year)
@app.route('/guess/<name>')
def about(name):
    response = requests.get(f"http://api.genderize.io/?name={name}")
    response.raise_for_status()
    data = response.json()
    year = datetime.date.today().year
    return render_template("index.html",year=year,gender=data["gender"], name=data["name"],probability=data["probability"])
if __name__ == '__main__':
    app.run(debug=True)
