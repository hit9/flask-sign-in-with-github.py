from setuptools import setup

setup(
    name="flask_github_login.py",
    version="0.1",
    author="hit9",
    author_email="nz2324@126.com",
    description=(
        "Sign in with github via github V3 API in Flask"
    ),
    license="BSD",
    url="https://github.com/hit9/flask-sign-in-with-github.py",
    install_requires=["flask", "requests"],
    py_modules=["flask_github_login"]
)
