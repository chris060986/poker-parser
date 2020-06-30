from pathlib import Path
from setuptools import setup, find_packages


install_requires = [
    "poker",
]


classifiers = [
    "Intended Audience :: Developers",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]


setup(
    name="pokerstars_parser",
    version="0.0.1",
    description="Pokerstars HandHistory Parser",
    long_description=Path("README.rst").read_text(),
    classifiers=classifiers,
    keywords="poker",
    author="Christoph Birk",
    author_email="christoph.birk@gmail.com",
    url="https://github.com/chris060986/pokerstars_parser",
    license="MIT",
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={"console_scripts": console_scripts},
)
