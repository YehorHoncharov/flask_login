from .settings import main_project
import home
import user

home.home.add_url_rule(rule= '/', view_func= home.render_home, methods = ["GET", "POST"])
main_project.register_blueprint(blueprint= home.home)

user.user.add_url_rule(rule= '/login/', view_func= user.login, methods = ["GET", "POST"])


user.user.add_url_rule(rule= '/reg/', view_func= user.reg, methods = ["GET", "POST"])
user.user.add_url_rule(rule= '/logout/', view_func= user.logout, methods = ["GET", "POST"])
main_project.register_blueprint(blueprint= user.user)