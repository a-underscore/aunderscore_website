from server import app

def run():
    return app

if __name__ == "__main__":
    app.run(debug=__debug__)
