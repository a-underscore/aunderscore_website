from server import app

@app.route("/")
def home():
    return "<p>Hello, World!</p>"
