from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, IntegerField, DateField, RadioField, SelectField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField("sheyivanet momxmareblis saxeli")
    password = PasswordField("sheiyvanet paroli")
    confirm_password = PasswordField("daadasturet paroli")
    age = IntegerField("sheiyvanet asaki")
    birthdate = DateField()
    gender = RadioField(choices=["man", "woman", "cat"])
    country = SelectField(choices=["georgia", "america"])

    register = SubmitField("dagregistrirdi")


