from flask import Flask

app = Flask(__name__)

import os
app.secret_key = os.urandom(25)

from Github import Github

github = Github(
    client_id="27080baf703669cb7571",
    client_secret="9892dc12683a962e8bcf48caf9bfe64f75e6f706",
    callback="http://localhost:5000/authorize/callback"
)

def do_login(user_data):
	# do login stuff..: set session .etc
	return user_data["login"]

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

### for test,not required!
@app.route("/")
def mk_bad_token():
	from flask import session
	session["Github_access_token"] = "BADTOKEN"
	return ""


if __name__ == '__main__':
    app.run(debug=True)
