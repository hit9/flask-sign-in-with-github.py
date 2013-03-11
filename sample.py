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

@app.route("/login")
def login():
    user_data = github.fetch_user()
    if not user_data:
        return github.authorize()
    return user_data["email"]

@app.route("/authorize/callback")
def authorize_callback():
    github.fetch_token()
    user_data = github.fetch_user()  # return json
    return user_data["login"] # unicode

if __name__ == '__main__':
    app.run(debug=True)
