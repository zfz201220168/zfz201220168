from wsgiref.validate import validator
import wtforms

from wtforms.validators import length, EqualTo


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=8, max=20)])
    password2 = wtforms.StringField(validators=[EqualTo("password")])


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=6, max=20)])
    password = wtforms.StringField(validators=[length(min=8, max=20)])
