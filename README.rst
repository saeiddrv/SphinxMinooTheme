Minoo
======

Minoo Theme is a `Sphinx <http://sphinx-doc.org/>`_ theme that supports right-to-left languages like `Persian <http://en.wikipedia.org/wiki/Persian_language>`_. It is available on PyPI and enables developers to create documentation websites with an elegant and functional design that works well with RTL languages.

.. image:: https://badge.fury.io/py/sphinx_minoo_theme.svg
    :target: http://badge.fury.io/py/sphinx_minoo_theme
    
|

.. contents::



Features
---------
* Material Colors
* RTL language support
* Responsive design
* Google Analytics integration
* Social links and avatar
* Free to use


Installation
-------------

Via package
~~~~~~~~~~~~

You can install Minoo Theme from PyPI::
    
    $ pip install sphinx_minoo_theme

To use the theme in your Sphinx project, edit your Sphinx configuration file ``conf.py`` as follows::
    
    # At the top.
    import sphinx_minoo_theme
    
    # ...

    extensions = ["sphinxcontrib.jquery"]
    html_theme = "sphinx_minoo_theme"
    html_theme_path = [sphinx_minoo_theme.get_html_theme_path()]


Via git or download
~~~~~~~~~~~~~~~~~~~~

Alternatively, you can download the theme from the repository and copy ``sphinx_minoo_theme/sphinx_minoo_theme`` into your documentation at ``_templates`` folder. Then, add the following lines to your ``conf.py`` file::
    
    extensions = ["sphinxcontrib.jquery"]
    html_theme = "sphinx_minoo_theme"
    html_theme_path = ["_templates"]


Customisation
--------------

To customize the Minoo Theme, follow these steps:

1. Put your avatar image file into the ``static`` folder with the name ``avatar.jpg``.

2. Edit the theme configuration file ``theme.conf``: 

* Change direction:

  ..  code-block:: none
  
    direction = ltr

  For "right-to-left" languages, set it to ``rtl``

* Add your Google Analytics ID:

  ..  code-block:: none
    
    analytics_id = UA-XXXXX-X

* Add your website address and social links:

  ..  code-block:: none
    
    website =
    facebook =
    googleplus =
    linkedin =
    twitter =
    github = https://github.com/saeiddrv/SphinxMinooTheme
    gitlab =
    bitbucket =

  Leave empty whichever you don't want.

3. Edit the ``glossary.html`` file to change the theme words.

License
--------

Minoo Theme is licensed under the MIT License. For more information, see the `LICENSE <https://github.com/saeiddrv/SphinxMinooTheme/blob/master/LICENSE>`_ file.


Gratitude
----------

I would like to thank `sphinx_rtd_theme <https://github.com/snide/sphinx_rtd_theme>`_ for helping me build this theme.



     
