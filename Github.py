"""
Access Github to login:

  1.) define a route to authorize.(redirect to github's oauth page):

      github = Github(
          client_id="xxxxxxxxxxxx",
          client_secret = "xxxxxxxxxxxx",
          callback="yourdomain.com/login/callback"
      )

      @app.route("/login")
      def login():
          return github.authorize()

  3.) fetch user information in your callback route:

      @app.route("/login/callback")
      def login_callback():
        user_data = github.fetch_user()  # return json
"""

import requests
from flask import redirect, request


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

    def fetch_token(self, code):
        data = {
            "code": code,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {'Accept': 'application/json'}
        token_url = "https://github.com/login/oauth/access_token"
        re = requests.post(token_url, data=data, headers=headers)
        return re.json()['access_token']

    def fetch_user(self):
        token = self.fetch_token(self.fetch_code())
        params = {"access_token": token}
        user_api_url = "https://api.github.com/user"
        return requests.get(user_api_url, params=params).json()
