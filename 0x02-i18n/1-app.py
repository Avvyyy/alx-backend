#!/usr/bin/env python3
"""Program to configure babel's langauge and timezone"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
	"""
		Class to configure the language and timezone settings of Babel

		Attributes:
		Languages - english and french
		Time: UTC
	"""
	LANGUAGES = ["en", "fr"]
	BABEL_DEFAULT_LOCALE = "en"
	BABEL_DEFAULT_TIMEZONE = "UTC"

#Tells the program where to get the config from
app.config.from_object(Config)

@app.route('/')
def home_route():
    """
    Route function for the home page.

    Returns:
        str: Rendered HTML template.
    """
    title = 'Welcome to Holberton'
    header = 'Hello world'
    return render_template('1-index.html', title=title, header=header)


if __name__ == '__main__':
	app.run(debug=True)