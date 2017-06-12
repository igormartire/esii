"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = [
    'black-bishop.png',
    'black-king.png',
    'black-knight.png',
    'black-pawn.png',
    'black-queen.png',
    'black-rook.png',
    'white-bishop.png',
    'white-king.png',
    'white-knight.png',
    'white-pawn.png',
    'white-queen.png',
    'white-rook.png',
]
OPTIONS = {
    'packages': ['pygame']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
