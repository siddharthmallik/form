from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, Submitfield
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	user_id = Submitfield("UserID", validators=[DataRequired()])
	email = Submitfield("password", validators=[DataRequired()])
	password = StringField("password", validators=[DataRequired()])
	submit = Submitfield("Login")

class RegisterForm(FlaskForm):
	user_id = Submitfield("UserID", validators=[DataRequired()])
	email = Submitfield("password", validators=[DataRequired()])
	password = StringField("password", validators=[DataRequired()])
	password_confirm = StringField("confirm password", validators=[DataRequired()])
	Full_name = StringField("Full name", validators=[DataRequired()])
	submit = Submitfield("Login")

