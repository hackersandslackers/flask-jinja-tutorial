"""Route declaration."""
from flask import current_app as app
from flask import render_template


@app.route('/')
def home():
    """Landing page."""
    links = [{'name': 'Link 1', 'url': 'https://example.com/1'},
             {'name': 'Link 2', 'url': 'https://example.com/2'},
             {'name': 'Link 2', 'url': 'https://example.com/3'}]
    return render_template('home.html',
                           links=links,
                           title="Jinja Demo Site",
                           description="Smarter page templates \
                                with Flask & Jinja.")
