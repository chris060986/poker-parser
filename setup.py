from setuptools import setup, find_packages

install_requires = [
    "poker",
    "flask",
    "jsonpickle",
    "couchdb",
    "configloader[all]"
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
    version="0.0.2",
    description="Pokerstars HandHistory Parser",
    classifiers=classifiers,
    keywords="poker",
    author="Christoph Birk",
    author_email="christoph.birk@gmail.com",
    url="https://github.com/chris060986/pokerstars_parser",
    license="MIT",
    packages=find_packages(),
    package_data={'': ['templates/*']},
    install_requires=install_requires
)
