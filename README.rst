Minoo
======

.. image:: https://badge.fury.io/py/sphinx_minoo_theme.svg
    :target: http://badge.fury.io/py/sphinx_minoo_theme
    
|

.. contents::


`Minoo <https://github.com/saeiddrv/SphinxMinooTheme>`_ is a simple `Sphinx <http://sphinx-doc.org/>`_ theme with supports right-to-left languages such as `Persian <http://en.wikipedia.org/wiki/Persian_language>`_.


Features
---------
* Material Colors
* RTL language
* Responsive
* Google Analytics id
* Social Links and Avatar
* Free


Installation
-------------

Via package
~~~~~~~~~~~~

1. Installing from PyPI::
    
    $ pip install sphinx_minoo_theme

2. Edit the Sphinx configuration file ``conf.py`` ::
    
    # At the top.
    import sphinx_minoo_theme
    
    # ...
    
    html_theme = "sphinx_minoo_theme"
    
    html_theme_path = [sphinx_minoo_theme.get_html_theme_path()]


Via git or download
~~~~~~~~~~~~~~~~~~~~

1. Copy ``sphinx_minoo_theme/sphinx_minoo_theme`` from repository into your documentation at ``_templates`` folder.

2. Edit the Sphinx configuration file ``conf.py`` ::
    
    # ...
    
    html_theme = "sphinx_minoo_theme"
    
    html_theme_path = ["_templates"]


Customisation
--------------

1. Put your avatar image file into ``static`` folder with ``avatar.jpg`` name.

.. rubric:: Edit the theme configuration file ``theme.conf``

2. Change direction::
    
    direction = ltr

  for "right-to-left" languages set on ``rtl``

3. Add your Google Analytics id::
    
    analytics_id = UA-XXXXX-X

4. Add your website address and social links::
    
    website =
    facebook =
    googleplus =
    linkedin =
    twitter =
    github = https://github.com/saeiddrv/SphinxMinooTheme
    bitbucket =

  Whichever you don't want, left empty!

.. rubric:: Edit the ``glossary.html`` file

5. In this way, you can change the theme words!

License
--------

`The MIT License (MIT) <https://github.com/saeiddrv/SphinxMinooTheme/blob/master/LICENSE>`_

Gratitude
----------

`sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`_ helped me build this theme.



     
