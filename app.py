from flask import Flask, render_template
from forms import RegisterForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234567"

profiles = [
    {"name": "jasurbeki", "surname": "iaxshiboevi", "img": "earth.jpg"},
    {"name": "iago", "surname": "xvichia", "img": "cat.jpg"}
]
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


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)


@app.route("/genre/<category>") # < variable > დინამიური ცვლადის შესაქმნელად
def show_genre(category):
    return render_template("genre.html", c=category)


app.run(debug=True) # debug=True -> ცვლილებების შემთხვევაში აღარ გვიწევს სერვერის თავიდან გაშვება, ავტომატურად აფდეითდება საიტი