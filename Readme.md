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

2.)

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
