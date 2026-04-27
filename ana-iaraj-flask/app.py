from flask import Flask, render_template

app = Flask(__name__)

profiles = [
    {"name": "jasurbeki", "surname": "iaxshiboevi", "img": "earth.jpg", "role": "admin"},
    {"name": "iago", "surname": "xvichia", "img": "cat.jpg", "role": "user"}
]
movies = [
    {"title": "12 Angry Man", "description": "magari filmia", "img": "movie1.jpeg"},
    {"title": "12 Angry Man2", "description": "zan magari filmia","img": "movie2.jpeg"},
    {"title": "12 Angry Man3", "description": "zan zan magari filmia", "img": "movie3.jpeg"}

]

@app.route("/")
def home():

    return render_template("index.html", role="admin", movies=movies)



@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template("profile.html", profile=profile)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/genre/<category>")
def show_genre(category):
    return render_template("genre.html", c=category)



app.run(debug=True)