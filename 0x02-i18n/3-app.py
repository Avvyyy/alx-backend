#!/usr/bin/env python3
"""A Basic Flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    @staticmethod
    def get_locale() -> str:
        """Retrieves the locale for a web page.
        """
        return request.accept_languages.best_match(Config.LANGUAGES)


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """The home/index page.
    """
    return render_template('3-index.html')

@app.route('/user/<username>')
def display(username):
    return render_template('3-index.html', name=username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
