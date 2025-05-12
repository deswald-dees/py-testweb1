import os
from __main__ import app

@app.route("/")
def index():
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/hello")
def hello_world():
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"
