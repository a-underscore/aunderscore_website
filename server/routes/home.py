from server import app, github
from flask import render_template


@app.route("/")
def home():
    data = [
        (repo.stargazers_count, f"{repo.name} (archived)" if repo.archived else repo.name, repo.clone_url)
        for repo in reversed(
            sorted(
                reversed(list(github.get_user().get_repos())),
                key=lambda r: r.stargazers_count,
            )
        )
    ]

    return render_template("home.html", data=data)
