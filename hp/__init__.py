from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "db31ba4a81da503f91cac8859eef24ecfc440f217a6667d3f91b99c26c573229"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from hp import routes
