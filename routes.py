from ext import app
from flask import Flask, render_template, redirect
from forms import RegisterForm, MovieForm
from os import path

profiles = []
"""
ლექსიკონიდან ინფორმაციის წამოღება:
info = profiles[0] -> info არის ლექსიკონი
print(info.get("name"), info["name"]) -> get method ან პირდაპირ ['key']-ის დახმარებით
"""

movies = [
    {"id": 1, "title": "Django Unchained", "director": "Quentin Tarantula", "rating": 4.3, "img": "movie1.jpg"},
    {"id": 2, "title": "Whiplash", "director": "Damon Giselle", "rating": 4.8, "img": "movie2.jpg"},
    {"id": 3, "title": "Interstellar", "director": "Christie Nolana", "rating": 4.6, "img": "movie3.jpg"}
]


@app.route("/")
def home():
    return render_template("index.html", movies=movies) # HTML-ისთვის ცვლადის გადაცემა


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = {
            "username": form.username.data,
            "mobile": form.mobile.data,
            "date": form.birthdate.data,
        }
        img = form.image.data # None
        if img: # None-ის გარდა ნებისმიერი რაღაც იქნება True
            directory = path.join(app.root_path, "static", "images", img.filename)
            new_user["img"] = img.filename
            img.save(directory)
        profiles.append(new_user)
        return redirect("/")
    return render_template("register.html", form=form)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    form = MovieForm()
    return render_template("add_movie.html", form=form)




@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/profile/<int:profile_id>") # profile_id დინამიური ცვლადია, რომელიც int ტიპია (int:) ამ შემთხვევაში. default-ად სტრინგია
def profile(profile_id):
    profile = profiles[profile_id]
    return render_template("profile.html", profile=profile)


@app.route("/movie/<int:movie_id>")
def view_movie_details(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return render_template("movie_details.html", movie=movie)
    return "Movie Not Found"




@app.route("/genre/<category>") # < variable > დინამიური ცვლადის შესაქმნელად
def show_genre(category):
    return render_template("genre.html", c=category)

