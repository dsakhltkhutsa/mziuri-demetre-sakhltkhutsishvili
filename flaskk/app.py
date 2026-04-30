from flask import Flask, render_template

app = Flask(__name__)

profiles = [
    {"name": "jasurbeki", "surname": "iaxshiboevi", "img": "earth.jpg", "role": "admin"},
    {"name": "iago", "surname": "xvichia", "img": "cat.jpg", "role": "user"}
]
movies = [
    {"id": 1, "title": "12 Angry Man", "rating": 4.3, "img": "movie1.jpeg"},
    {"id": 2, "title": "12 Angry Man2", "rating": 4.1,"img": "movie2.jpeg"},
    {"id": 3, "title": "12 Angry Man3", "rating": 3.8, "img": "movie3.jpeg"}
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

@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie_details.html", movie=movie)
    return "Movie not found"


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