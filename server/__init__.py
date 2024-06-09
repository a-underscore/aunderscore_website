import os
import json
from flask import Flask
from github import Github
from github import Auth

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

auth = Auth.Token(conf["token"])
github = Github(auth=auth)
app = Flask(conf["server"]["name"])

import server.routes
