


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '2ddd2602056cd619783ab9536e863539'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes #noqa