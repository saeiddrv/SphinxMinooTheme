
reStructuredText
=================

Resources: `reStructuredText Directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_ and `reStructuredText <http://rest-sphinx-memo.readthedocs.org/en/latest/ReST.html>`_

Sidebar
--------

.. sidebar:: Sidebar Title
    :subtitle: Optional Sidebar Subtitle
    
    Subsequent indented lines comprise
    the body of the sidebar, and are
    interpreted as body elements.
    
.. code::
    
    .. sidebar:: Sidebar Title
        :subtitle: Optional Sidebar Subtitle
        
        Subsequent indented lines comprise
        the body of the sidebar, and are
        interpreted as body elements.

Sidebars are like miniature, parallel documents that occur inside other documents, providing related or reference material. A sidebar is typically offset by a border and "floats" to the side of the page; the document's main text may flow around it. Sidebars can also be likened to super-footnotes; their content is outside of the flow of the document's main text.


Inline markup
--------------

.. sidebar:: Special cases
    
    ================== =============
    ``Asterisk \*``    Asterisk \*
    ``back-quote \```  back-quote \`
    ``**mark**\ up.``  **mark**\ up.
    ================== =============

========================== ======================
``*emphasize*``            *emphasize*
``**emphasize strongly**`` **emphasize strongly**
````code````               ``code``
```don't know```           `don't know`
========================== ======================

|


Lists
------

.. sidebar:: Code
    
    .. code::
        
        - First item with some lengthy text wrapping hopefully across several lines.
        - Second item

    .. code::
        
        .. hlist::
            :columns: 3
            
            * one
            * two
            * three
            * four
            * five

    .. code::
        
        2. We start with point number 2
        #. Automatically numbered item.
        
        a) Point a
        b) Point b
        #) Automatic point c.

    .. code::
        
        what
            Definition of "what". We add a few
            words to show the line wrapping.
        how
            Definition of "how".
        why : cause
            We define "why" we do it.
            
            In many paragraphs

    .. code::
        
        :Name: Isaac Newton
        :Long: Here we insert more
            text to show the effect of
            many lines.
        :Remark:
            Start on the next line.

    .. code::
        
        -v           An option
        -o file      Same with value
        --delta      A long option
        --delta=len  Same with value


Bullet list
~~~~~~~~~~~~~

- First item with some lengthy text wrapping hopefully across several lines.
- Second item

Horizontal list
~~~~~~~~~~~~~~~~

.. hlist::
    :columns: 3
    
    * one
    * two
    * three
    * four
    * five

Enumerated list
~~~~~~~~~~~~~~~~

2. We start with point number 2
#. Automatically numbered item.

a) Point a
b) Point b
#) Automatic point c.

Definition list
~~~~~~~~~~~~~~~~
what
  Definition of "what". We add a few
  words to show the line wrapping.
how
  Definition of "how".
why : cause
  We define "why" we do it.

  In many paragraphs

Field list
~~~~~~~~~~~
:Name: Isaac Newton
:Long: Here we insert more
    text to show the effect of
    many lines.
:Remark:
    Start on the next line.

Options list
~~~~~~~~~~~~~
-v           An option
-o file      Same with value
--delta      A long option
--delta=len  Same with value


Blocks
-------

.. sidebar:: Code
    
    .. code::
        
        | Line block
        | New line and we are still on
          the same line
        |   Yet a new line

    .. code::
        
        indenting them more than the surrounding paragraphs.
            
            Neither from itself nor from another,
            Nor from both,
            Nor without a cause,
            Does anything whatever, anywhere arise.
            
            --Nagarjuna - *Mulamadhyamakakarika*

    .. code::
        
        .. epigraph::
            
            No matter where you go, there you are.
            
            -- Buckaroo Banzai

    .. code::
        
        .. pull-quote::
            
            Just as a solid rock is not shaken by the storm, even so
            the wise are not affected by praise or blame.

    .. code::
        
        .. highlights::
                
            With these *highlights* we have completed the Rest blocks.


Line blocks
~~~~~~~~~~~~

| Line block
| New line and we are still on
  the same line
|   Yet a new line

Block quote
~~~~~~~~~~~~

indenting them more than the surrounding paragraphs.

   Neither from itself nor from another,
   Nor from both,
   Nor without a cause,
   Does anything whatever, anywhere arise.

   --Nagarjuna - *Mulamadhyamakakarika*

Epigraph
~~~~~~~~~~
An epigraph is an apposite (suitable, apt, or pertinent) short inscription, often a quotation or poem, at the beginning of a document or section.

.. epigraph::
    
    No matter where you go, there you are.
    
    -- Buckaroo Banzai

Pull-quote
~~~~~~~~~~~
A pull-quote is a small selection of text "pulled out and quoted", typically in a larger typeface. Pull-quotes are used to attract attention, especially in long articles.

.. pull-quote::
    
    Just as a solid rock is not shaken by the storm, even so
    the wise are not affected by praise or blame.


Highlight
~~~~~~~~~~
Highlights summarize the main points of a document or section, often consisting of a list.

.. highlights::
    
    With these *highlights* we have completed the Rest blocks.

Tables
-------

.. sidebar:: Code
    
    .. code::
        
        ==  ==
        aA  bB
        cC  dD
        ==  ==
        
        =====  ======
        Vokal  Umlaut
        =====  ======
        aA     äÄ
        oO     öÖ
        =====  ======
        
        =====  =====  ======
        Inputs        Output
        ------------  ------
          A      B    A or B
        =====  =====  ======
        False         False
        ------------  ------
        True   False  True
        False  True   True
        True          True
        ============  ======
        
        ===========  ================
        1. Hallo     | blah blah blah
                       blah blah blah
                       blah
                             | blah blah
        2. Here      We can wrap the
                     text in source
        32. There    **aha**
        ===========  ================

    .. code::
        
        +--------+--------+-----------+
        | Header | Header with 2 cols |
        +========+========+===========+
        | A      | Lists: | **C**     |
        +--------+  - aha +-----------+
        | B::    |  - yes | | a block |
        |        |        |   of text |
        |  *hey* |  #. hi | | a break |
        +--------+--------+-----------+

    .. code::
        
        .. csv-table:: Balance Sheet
            :header: Description,In,Out,Balance
            :widths: 20, 10, 10, 10
            :stub-columns: 1
            
            Travel,,230.00,-230.00
            Fees,,400.00,-630.00
            Grant,700.00,,70.00
            Train Fare,,70.00,**0.00**
    
    

Simple tables
~~~~~~~~~~~~~~

==  ==
aA  bB
cC  dD
==  ==

=====  ======
Vokal  Umlaut
=====  ======
aA     äÄ
oO     öÖ
=====  ======

=====  =====  ======
Inputs        Output
------------  ------
  A      B    A or B
=====  =====  ======
False         False
------------  ------
True   False  True
False  True   True
True          True
============  ======

===========  ================
1. Hallo     | blah blah blah
               blah blah blah
               blah
             | blah blah
2. Here      We can wrap the
             text in source
32. There    **aha**
===========  ================

Grid tables
~~~~~~~~~~~~

+--------+--------+-----------+
| Header | Header with 2 cols |
+========+========+===========+
| A      | Lists: | **C**     |
+--------+  - aha +-----------+
| B::    |  - yes | | a block |
|        |        |   of text |
|  *hey* |  #. hi | | a break |
+--------+--------+-----------+

CSV Tables
~~~~~~~~~~~
.. csv-table:: Balance Sheet
    :header: Description,In,Out,Balance
    :widths: 20, 10, 10, 10
    :stub-columns: 1
    
    Travel,,230.00,-230.00
    Fees,,400.00,-630.00
    Grant,700.00,,70.00
    Train Fare,,70.00,**0.00**


Explicit Markup
-----------------

.. sidebar:: Code
    
    .. code::
        
        A good rST tutorial [#f1]_ is located at the bottom[#f2]_
        of the page.
        
        .. rubric:: Footnotes
        
        .. [#f1] Here: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
        .. [#f2] Text of the second footnote.


    .. code::
        
        The rST specification [RefMarkup]_ is available on the web.
        
        .. [RefMarkup] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

Footnotes
~~~~~~~~~~

For footnotes, use ``[#name]_`` to mark the footnote location, and add the footnote body at the bottom of the document after a "Footnotes" rubric heading, like so:

A good rST tutorial [#f1]_ is located at the bottom [#f2]_
of the page.

.. rubric:: Footnotes

.. [#f1] Here: http://docutils.sourceforge.net/docs/user/rst/quickstart.html
.. [#f2] Text of the second footnote.


Citations
~~~~~~~~~~~
All citations can be referenced from all files. Citation usage is similar to footnote usage, but with a label that is not numeric or begins with #.

The rST specification [RefMarkup]_ is available on the web.

.. [RefMarkup] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html


Code Examples
--------------

.. sidebar:: Code
    
    .. code::
        
        .. code-block:: language
            
            Some language code.

    see: `Here <http://sphinx-doc.org/markup/code.html>`_


.. code-block:: python
    
    >>> 
    >>> class Complex:
    ...     def __init__(self, realpart, imagpart):
    ...         self.r = realpart
    ...         self.i = imagpart
    ...
    >>> x = Complex(3.0, -4.5)
    >>> x.r, x.i
    (3.0, -4.5)
    >>> 

.. rubric:: With line numbers:

.. code-block:: python
    :linenos:
    
    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)
        
        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)
    
        __update = update   # private copy of original update() method
    
    class MappingSubclass(Mapping):
    
        def update(self, keys, values):
            # provides new signature for update()
            # but does not break __init__()
            for item in zip(keys, values):
                self.items_list.append(item)


Admonitions
------------
.. sidebar:: Code
    
    .. code::
        
        .. danger::
            Beware killer rabbits!

.. hlist::
    :columns: 3
    
    * attention
    * note
    * tip
    * important
    * hint
    * warning
    * error
    * danger
    * caution
    * admonition

For example:

.. attention::
    Your text  

.. note::
    Your text  

.. tip::
    Your text  

.. important::
    Your text  

.. hint::
    Your text  

.. warning::
    Your text  

.. error::
    Your text  

.. danger::
    Your text  

.. caution::
   Your text  

.. admonition:: Your title
    
    Your text 


