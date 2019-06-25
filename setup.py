from distutils.core import setup

from shapes import VERSION

arguments = dict(
        name = "Shapes",
        version = VERSION,
        description = "2D Game Utilities",

        author = "Kale Kundert",
        author_email = "kale@thekunderts.net",

        py_modules = ("vector", "shapes", "collisions") )

setup(**arguments)
