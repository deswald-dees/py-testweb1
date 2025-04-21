import os

from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Hello {name}!"

@app.route("/gallery-dl-get-url")
def gallery_dl_get_url():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return f"Gallery DL GET_URL, {name}!"

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
