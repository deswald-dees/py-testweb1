import os
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# import declared routes
import route_default
import route_gallery_dl_get_url
import route_gallery_dl_get_url2

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("CONTAINER_PORT", 3000)))
