from flask import Flask, render_template
import requests, datetime, json, os


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
    return render_template("index.html",year=year,gender=data["gender"], name=data["name"].upper(),probability=data["probability"])
@app.route("/blogs")
def blogs():
    with open("blog.json") as f:
        my_blogs = json.load(f)
        return render_template("blog.html",my_blogs=my_blogs)
@app.route("/blog/<int:id>")
def get_post(id):
    with open("blog.json") as f:
        my_blogs = json.load(f)
        my_blog = my_blogs[id]
        return render_template("blog.html",my_blog=my_blog,id=id)

if __name__ == '__main__':
    app.run(debug=True)
