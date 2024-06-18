import os
import json
from flask import Flask
from github import Github
from github import Auth
from dotenv import load_dotenv

load_dotenv()

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

auth = Auth.Token(os.environ.get("NEXT_PUBLIC_GITHUB_TOKEN"))
github = Github(auth=auth)
app = Flask(conf["server"]["name"])

import server.routes
