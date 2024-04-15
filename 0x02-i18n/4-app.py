#!/usr/bin/env python3
"""A Basic Flask app."""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

    @staticmethod
    def get_locale() -> str:
        """Sets the language of the webpage to the selected parameters."""
        locale_param = request.args.get('locale')

        if locale_param and locale_param in LANGUAGES:
            return locale_param

        return None


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/?locale=fr')
def get_index() -> str:
    """The home/index page."""
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
