from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz

app = Flask(__name__)
babel = Babel(app)

# User table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Function to get user based on login_as parameter
def get_user(login_as):
    return users.get(int(login_as))

# Before request function to set the user as global variable on flask.g.user
@app.before_request
def before_request():
    login_as = request.args.get('login_as')
    g.user = get_user(login_as) if login_as else None

# Translation strings
translations = {
    "en": {
        "logged_in_as": "You are logged in as %(username)s.",
        "not_logged_in": "You are not logged in."
    },
    "fr": {
        "logged_in_as": "Vous êtes connecté en tant que %(username)s.",
        "not_logged_in": "Vous n'êtes pas connecté."
    }
}

# Route for home page
@app.route('/')
def home():
    if g.user:
        username = g.user['name']
        message = _(translations[g.user['locale']]['logged_in_as']) % {'username': username}
    else:
        message = _(translations['en']['not_logged_in'])  # Default message
    return render_template('5-index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
