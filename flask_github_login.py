"""
Access Github to login:

  1.) define a route to authorize.(redirect to github's oauth page):

      github = Github(
          client_id="xxxxxxxxxxxx",
          client_secret = "xxxxxxxxxxxx",
          callback="yourdomain.com/authorize/callback"
      )
  2.) and then in your app:

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

"""

import requests
from flask import redirect, request, session


class Github(object):

    def __init__(self, client_id, client_secret, callback=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.callback = callback

    def authorize(self):
        authorize_url = "https://github.com/login/oauth/authorize"
        uri = authorize_url + "?client_id=" + self.client_id
        if self.callback:
            uri += "&redirect_uri=" + self.callback
        return redirect(uri)

    def fetch_code(self):
        return request.args.get("code")

    def fetch_token(self):
        code = self.fetch_code()
        data = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {'Accept': 'application/json'}
        token_url = "https://github.com/login/oauth/access_token"
        re = requests.post(token_url, data=data, headers=headers)
        # set session
        token = session["Github_access_token"] = re.json()['access_token']
        return token

    def fetch_user(self):
        token = session.get("Github_access_token", None)

        # No token session, go to authorize web flow
        if not token:
            return None
        params = {"access_token": token}
        user_api_url = "https://api.github.com/user"
        resp = requests.get(user_api_url, params=params)
        # token in session not avaliblea now, out of lifetime
        if resp.status_code != requests.codes.ok:
            return None
        return resp.json()
