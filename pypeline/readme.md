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

`ext` is the extension folder where builtin functions can be saved.
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
be loaded

# examples and use case for using pypeline:
## general usage
consider you write a set of functions (as an extension)
and want to build a pipeline for async data processing,
users need to first save each function as a separate
.py file, with a file name same as the function
name, then you need to:
1. tell pypeline where these .py files are saved by setting:
`pypeline.ext_path.append('path-to-your-py-files')`
2. do `pypeline.load_ext()``
3. to list all available functions, do `pypeline.list_ext()`
4. build and run your pipeline by:
    ```python
    p = Pipeline([list of functions])
    p.process(data_in)
    p.close() to close the pipeline
    ```
alternatively, users can load specific function instead of
a set of them by doing:
`pypeline.load_func('path-to-the-func-file')`.
Thereafter, the user can put the function into the pipeline
as they wish

## load for certain implementations
this is very useful for quick prototyping to enable real time
data acquisition and processing/displaying
TODO:


TODO:
write the use case for this package, remember to learn from tydlig
calculator.
