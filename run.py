import json
import os
from server import app, conf

def run():
    return app

if __name__ == "__main__":
    app.run(debug=__debug__, host=conf["server"]["address"], port=conf["server"]["port"])
