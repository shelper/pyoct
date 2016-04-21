# quick start
 To use pypeline to build data processing pipeline, the user needs:
1. python source code files that defines the functions for data processing.
function name should be same as file name
2. function configuration files, where extra arguments are loaded
3. data to be processed

once the user has all these ready, they can run script as below
to build the pipeline
```python
from pypeline import funcwrap, pipeline

# load and register the function for building pipeline
for py_file in files:
    funcwrap.func_fromfile('path to the function.py file',reg_name=None)

# the use can list all the registered functions
funcwrap.list_funcs()

# the user can build the pypeline:
p = Pipeline([list of functions])

# the user can run the pypeline
p.process(data_in)

# once finished, the pipeline auto closes it self
# user can also explicitly close pypeline by:
p.close()

```


