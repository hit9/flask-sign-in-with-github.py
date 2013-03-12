from flask import session, flash, redirect, url_for, Flask

app = Flask(__name__)

import os
app.secret_key = os.urandom(25)

from flask_github_login import Github

github = Github(
    client_id="27080baf703669cb7571",
    client_secret="9892dc12683a962e8bcf48caf9bfe64f75e6f706",
    callback="http://localhost:5000/authorize/callback"
)

@app.route("/")
def index():
    return "index page.."

def do_login(user_data):
    # do login stuff..: set session .etc
    session["github_id"] = user_data["id"]
    session["username"] = user_data["login"]
    flash("Successfully logined!")
    return redirect(url_for("index"))

@app.route("/login")
def login():
    user_data = github.fetch_user()
    if not user_data:
        return github.authorize()
    return do_login(user_data)

@app.route("/authorize/callback")
def authorize_callback():
    github.fetch_token()
    user_data = github.fetch_user()  # return json
    return do_login(user_data)


if __name__ == '__main__':
    app.run(debug=True)
