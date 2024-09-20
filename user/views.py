import flask
from flask_bcrypt import Bcrypt
import main
import home
from flask_login import current_user, login_user, logout_user, login_required



def login():
    if not current_user.is_authenticated:
        if flask.request.method == "POST":
            login_var = flask.request.form['login']
            password_var = flask.request.form['password']
            if login_var and password_var:
                user_obj = main.User.query.filter_by(login=login_var).first()
                if user_obj and main.bcrypt.check_password_hash(user_obj.password, password_var):
                    login_user(user_obj)
                    return flask.redirect(flask.url_for("home.render_home"))

        return flask.render_template(template_name_or_list='login.html') 
    else:
        return flask.redirect(flask.url_for("home.render_home"))


def reg():
    if not current_user.is_authenticated:
        if flask.request.method == "POST":
            login_var = flask.request.form['login']
            password_var = flask.request.form['password']
            password2_var = flask.request.form['password2']
            if login_var and password_var and password2_var:
                if len(login_var) <= 12 and len(login_var) > 0:
                    if len(password_var) >= 8 and len(password_var) <= 15:
                        if password_var == password2_var:
                            
                            user_obj = main.User.query.filter_by(login=login_var).first()
                            if user_obj is None:
                                pw_hash = main.bcrypt.generate_password_hash(password_var).decode('utf-8')
                                user_obj = main.User(
                                    login = login_var,
                                    password = pw_hash
                                )
                                main.db.session.add(user_obj)
                                main.db.session.commit()

                                login_user(user_obj)
                                return flask.redirect(flask.url_for("home.render_home"))

        return flask.render_template(template_name_or_list='reg.html') 
    else:
        return flask.redirect(flask.url_for("home.render_home"))

@login_required
def logout():
    logout_user()
    return flask.redirect(flask.url_for('home.render_home'))