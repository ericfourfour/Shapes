from setuptools import setup, find_packages

from shapes import VERSION

setup(
    name="Shapes",
    version=VERSION,
    description="2D Game Utilities",

    author="Kale Kundert",
    author_email="kale@thekunderts.net",

    packages=find_packages()
)
