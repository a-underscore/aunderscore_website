import os
import json

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

server = conf["server"]
wsgi_app = "run:run()"
bind = f'{server["address"]}:{server["port"]}'
workers = os.cpu_count() * 2 + 1
reload = True

