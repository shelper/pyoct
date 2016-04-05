===============================
pypeline
===============================

.. image:: https://img.shields.io/travis/shelper/pypeline.svg
        :target: https://travis-ci.org/shelper/pypeline

python based packages for pipeline based framework for data processing

* Free software: ISC license
* Documentation: https://pyoct.readthedocs.org.

Features
--------
how to use pypeline package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

assume you have input data as ``data_in``, and you want to run the data
through a pipeline that is composed of a list of functions, you can run:

.. code:: python

    p = Pipeline([list of functions])
    p.process(data_in)
    p.close() to close the pipeline

notice that the data\_in could be a iterable, so that the pipeline will
run the iterable till the iterable stopiteration. In addition,
internally the pipeline can use async method to enable concurrent
processing.

how to load a python function that can be inserted into the pipeline
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. you need to define a function, e.g., test\_func in file
   test\_func.py.
2. you need to define the input and ouput data type and format in
   test\_func.ini
3. you need to import the function and use funcwrap and argswrap to
   pipenize test\_func
4. use the Pipeline class to build and run the pipeline processing

how to pre-set the functions to be imported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

use the config.py to configure the package to setup your enviroments
this can includes: 1. use specific implementation in pypeline.impl, for
example if you want to use the frame work for a specific applicaiton,
e.g., OCT - you can specify a filter to load functions from a set of
files - you can specify a list to load functions from a set of files 2.
use specific function in pypeline.ext

how to load a function defined in other programming language?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

same as load functions written in .py, currently the pypeline supports
matlab and c/c++. please pay attention to following things: for matlab
function 1. matlab function and file name should be the same. 2. you
need to install matlab.engine provided by mathworks, and you need to
have matlab installed on your computer 3. internally, matlab function is
wrapped in pypelin.funcwrap module using matlab.engine

for c/c++ function 1. dll file is loaded 3. internally, function in dll
file is wrapped in pypelin.funcwrap module using ctypes


TODO
~~~~
* load multiple functions defined in a single .py file

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
