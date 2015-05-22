# -*- coding: utf-8 -*-
"""`sphinx_minoo_theme` on `Github`_.

.. _github: https://github.com/saeiddrv/SphinxMinooTheme

"""
from setuptools import setup
from sphinx_minoo_theme import __version__


setup(
    name = "sphinx_minoo_theme",
    version = __version__.info(),
    url = "https://github.com/saeiddrv/SphinxMinooTheme.",
    license = "MIT",
    author = "Saeid Darvishi",
    author_email = "saeid.dq@gmail.com",
    description = "A simple Sphinx theme with RTL language support.",
    long_description = open("README.rst").read(),
    zip_safe = False,
    packages = ["sphinx_minoo_theme"],
    package_data = {"sphinx_minoo_theme": [
        "theme.conf",
        "*.html",
        "includes/*.html",
        "static/*.css",
        "static/*.js",
        "static/*.jpg",
        "static/fonts/*.*"
    ]},
    include_package_data = True,
    install_requires = open("requirements.txt").read().splitlines(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "Intended Audience :: System Administrators",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
