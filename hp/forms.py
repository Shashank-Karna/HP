import email
import imp
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from nbformat import ValidationError
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    BooleanField,
    TextAreaField,
    IntegerField,
)
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from hp.models import User, Test
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("That username is taken. Please chooser another one.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("That email is taken. Please chooser another one.")


class TestForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired()])
    gender = IntegerField("Gender", validators=[DataRequired()])
    cp = IntegerField("CP", validators=[DataRequired()])
    trest_bps = IntegerField("Trest BPS", validators=[DataRequired()])
    chol = IntegerField("Cholestrol", validators=[DataRequired()])
    fbs = IntegerField("FBS", validators=[DataRequired()])
    rest_ecg = IntegerField("Rest ECG", validators=[DataRequired()])
    thalach = IntegerField("Thalach", validators=[DataRequired()])
    exang = IntegerField("EXANG", validators=[DataRequired()])
    old_peak = IntegerField("Old Peak", validators=[DataRequired()])
    slope = IntegerField("Slope", validators=[DataRequired()])
    ca = IntegerField("CA", validators=[DataRequired()])
    thal = IntegerField("Thal", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
