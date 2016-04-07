# design of pypeline package

the package includes 3 subpackages
1. core
2. ext
3. impl

and a configuration file `config.py`

`core` is where the pypeline's core functions locate.
it contains all the definition of functions and classes
that enables the building of pipelines for async data
processing

`ext` is the extension folder where functions can be saved.
these functions can be loaded during package initialization
through the configuration in `config.py`

`impl` is where a set of functions can be combined for a
specific application/implementation. e.g., if this
package is used for Optical Coherence Tomography(OCT),
then the `oct` in `impl` contains all the functions dedicated
to OCT application and data processing

## core
subpackage `core` contains 3 modules:
1. `pipeline`, which defines the Pipeline class for building
data processing pipeline
2. `funcwrap`, which contains functions to load function from
a python module (.py file) and wrap up the function so
that it is ready to build the pipeline
3. `decors`, which collects some useful function wrappers
that modifies function behaviors using decorator based method

the steps of package initialization:
1. __init__.py of pypeline is loaded, which loads config.py
2. config.py checks which extensions in`ext` should be loaded,
then load these extensions using functions in `funcwrap`
3. config.py checks which implementation in `impl` should
be loaded,

## TODO
write the use case for this package, remember to learn from tydlig
calculator.
