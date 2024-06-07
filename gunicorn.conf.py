import os
import json

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

wsgi_app = "run:run()"
bind = f'{conf.get("server_address")}:{conf.get("server_port")}'
workers = 4
reload = True

