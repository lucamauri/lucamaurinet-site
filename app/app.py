# =============================================================================
# lucamaurinet-site — Flask application entry point
#
# This is the main application file. It creates the Flask app instance,
# defines URL routes, and connects them to template rendering.
#
# Gunicorn looks for the object named "app" in this file when starting:
#   gunicorn --bind 0.0.0.0:5000 app:app
#   (first "app" = this filename, second "app" = the object below)
# =============================================================================

from flask import Flask, render_template

# -----------------------------------------------------------------------------
# Create the Flask application instance.
# __name__ tells Flask where to look for templates and static files,
# relative to this file's location.
# -----------------------------------------------------------------------------
app = Flask(__name__)


# -----------------------------------------------------------------------------
# Route: home page
#
# The @app.route decorator maps a URL path to a Python function.
# When a visitor requests https://lucamauri.net/, Flask calls this function
# and returns whatever it produces as the HTTP response.
# -----------------------------------------------------------------------------
@app.route("/")
def home():
    # render_template() loads a Jinja2 HTML template from the templates/
    # directory and returns it as a response. We pass "title" as a variable
    # that the template can use (see templates/index.html).
    return render_template("index.html", title="Luca Mauri")


# -----------------------------------------------------------------------------
# Route: about page (placeholder for future content)
# -----------------------------------------------------------------------------
@app.route("/about")
def about():
    return render_template("about.html", title="About — Luca Mauri")


# -----------------------------------------------------------------------------
# Development server entry point.
# This block only runs when you execute "python app.py" directly —
# it is NEVER used by Gunicorn in production.
# Useful for quick local testing outside Docker.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)