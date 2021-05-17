from app import *
from modules.user import User, Create_User
from modules.forms import Login_Form

@app.route("/new_user", methods = ["post"])
def create_user():
    form = Login_Form()

    User_Obj = Create_User(form.identifier.data, form.email.data, form.password.data)

    if User_Obj.validate_user():
        User_Obj.create_user()
    
    else:
        error = "Username Already In Use"
        return render_template("create_user.html", form = form, error = error)

    return redirect(url_for("validate_user"), code = 307)

@app.route("/new_user", methods = ["get"])
def new_user():
    form = Login_Form()
    return render_template("create_user.html", form = form)

@login_manager.user_loader
def load_user(id):
    return User(id)

@app.route("/", methods = ["post"])
def validate_user():
    form = Login_Form()

    if User.validate_user(form.identifier.data, form.password.data):
        user_id = User.get_user_id(form.identifier.data)
        user = User(user_id)
        login_user(user)

        return redirect(url_for("home"))

    error = "Incorrect Username or Password"

    return render_template("login.html", form = form, error = error)

@app.route("/", methods = ["get"])
def index():
    form = Login_Form()
    return render_template("login.html", form = form)

if __name__ == "__main__":
    socketio.run(app)