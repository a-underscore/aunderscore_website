import json
import os
from server import app

with open(os.path.join(os.getcwd(), "config.json")) as file:
    conf = json.load(file)

def run():
    return app

if __name__ == "__main__":
    app.run(debug=__debug__, host=conf["server_address"], port=conf["server_port"])
