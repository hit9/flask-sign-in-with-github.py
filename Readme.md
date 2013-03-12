flask sign in with Github
=========================

Install
-------

    pip install git+git://github.com/hit9/flask-sign-in-with-github.py.git

How to use
----------

1.) Init github instance.

```python
from flask_github_login import Github

github = Github(
    client_id="xxxxxxxxxxxx",
    client_secret = "xxxxxxxxxxxx",
    callback="yourdomain.com/authorize/callback"
)

```

2.) define 2 route: /login and /authorize/callback

```python
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
    return do_login(user_data) # do login stuff
```

How to redirect to user's request url after login.
--------------------------------------------------


```python

from flask import request,url_for,redirect

@app.route("/login")
def login():
    # get next_url
    next_url = request.args.get("next", url_for("index"))
    github.callback += "?next=" + next_url
    user_data = github.fetch_user()
    if not user_data:
        return github.authorize()
    return do_login(user_data,next_url)

@app.route("/authorize/callback")
def authorize_callback():
    next_url = request.args.get("next",url_for("index"))
    github.fetch_token()
    user_data = github.fetch_user()  # return json
    return do_login(user_data,next_url) # do login stuff

def do_login(user_data,next):
    # set session .etc
    return redirect(next)
```
