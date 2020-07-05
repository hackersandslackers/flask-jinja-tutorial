"""Route declaration."""
from dataclasses import dataclass

from flask import current_app as app
from flask import render_template


@dataclass
class Link:
    url: str
    name: str


@app.route('/')
def home():
    """Landing page."""
    nav = [
        Link(name='Home', url='https://example.com/1'),
        Link(name='About', url='https://example.com/2'),
        Link(name='Pics', url='https://example.com/2')
    ]
    return render_template('home.html',
                           nav=nav,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
