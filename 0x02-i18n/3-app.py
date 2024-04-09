#!/usr/bin/env python3
""" """

from flask import Flask, render_template
from flask_babel import Babel, gettext, ngettext


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

app = Flask(__name__)
babel - Babel(app)
#Tells the program where to get the config from
app.config.from_object(Config)



if __name__ == "__main__":
	app.run(debug=True)