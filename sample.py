from flask import Flask

app = Flask(__name__)

from Github import Github

github = Github(
    client_id="27080baf703669cb7571",
    client_secret="9892dc12683a962e8bcf48caf9bfe64f75e6f706",
    callback="http://localhost:5000/login/callback"
)

@app.route("/login")
def login():
    return github.authorize()

@app.route("/login/callback")
def login_callback():
    user_data = github.fetch_user()  # return json
    return user_data["login"] # unicode

if __name__ == '__main__':
    app.run(debug=True)
