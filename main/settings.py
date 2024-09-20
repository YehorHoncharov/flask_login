import flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin


main_project = flask.Flask(
    import_name= "main",
    template_folder= "templates"
)
main_project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
main_project.secret_key = "verysecretkey"
bcrypt = Bcrypt(main_project)

login_manager = LoginManager()
login_manager.init_app(main_project)

db = SQLAlchemy()
db.init_app(main_project)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    # def __init__(self, login, password):
    #     self.login = login
    #     self.password = password

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# with main_project.app_context():
#     db.create_all()