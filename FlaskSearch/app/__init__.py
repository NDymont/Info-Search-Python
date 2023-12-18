from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:20205@localhost:5433/University'
app.secret_key = 'app.secret_key'

db = SQLAlchemy(app)
manager = LoginManager(app)
manager.login_view = 'login'
manager.login_message = 'Please log in to access this page'



from app.models import User


@manager.user_loader
def load_user(user_id):
    # Здесь вам нужно добавить логику загрузки пользователя по user_id
    return User.query.get(int(user_id))
    # pass
