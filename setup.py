"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask Jinja Tutorial',
    version='0.1.0',
    description='Build smarter page templates with Flask and Jinja.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/flask-jinja-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Flask Jinja Jinja2 Templating Templates',
    packages=find_packages(),
    install_requires=['Flask'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
        'env': ['python-dotenv']
    },
    entry_points={
        'console_scripts': [
            'run=wsgi:app',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/flask-jinja-tutorial/issues',
        'Source': 'https://github.com/hackersandslackers/flask-jinja-tutorial/',
    },
)
