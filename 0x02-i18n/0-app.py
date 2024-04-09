#!/usr/bin/env python3
"""
Program to render a html page using Flask.

This program creates a simple Flask web application that renders an HTML template.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_route():
    """
    Route function for the home page.

    Returns:
        str: Rendered HTML template.
    """
    title = 'Welcome to Holberton'
    header = 'Hello world'
    return render_template('0-index.html', title=title, header=header)

if __name__ == '__main__':
    app.run(debug=True)
