# what is this folder for?
this folder contains all the pipes that extend the functionality of the package.
a pipe is similar to a plugin and should be saved in this folder

# how pipes are loaded
the pipes are loaded by name and configged by a config file, e.g.,
a pipe named: compensate_dispersion.py, and a config file can be presented in the same folder, named
compensate_dispersion.cfg.
when config the system, the pipe needs to be registered before use:
```python
pyoct.OCTSystem.register(('compensate_dispersion')),
```
this line imports the pipe and load its configration. then the plugin is ready to be used

# what if the pipe is multiple file?
then it should be saved in a folder in pipes

# example of pipe and its configuration
pipe is a function that reads in and spit out certain data.
so it should have a major function
```python
def do_something(input):
    return output
```
then in the configuration file it should define the format of input and output:
```
[input]
    bitdepth =
    dtype =
    dimension = ('spectrum': 1024, 'b-scan': 512, 'c-scan': 1) #named tuple or dict would be nice.

[output]
    bitdepth =
    dtype =
    dimension = ('spectrum': 1024, 'b-scan': 512, 'c-scan': 1) #named tuple or dict would be nice.
```
a input/output type check is done before running the pipe, so to make sure the data flow is correct,
other wise, raise: PipeInputError, or PipeOutputError.

