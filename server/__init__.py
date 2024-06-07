import os
import json
from flask import Flask

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

app = Flask(conf["server"]["name"])

import server.routes
