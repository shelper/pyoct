# what is this folder for?
this folder contains all the pipes that extend the functionality of the package.
a pipe is similar to a plugin and should be saved in this folder

# how pipes are loaded
assume you have input data as `data`, and you want to run the data through a pipeline
that is composed of pipe A, B, and C. you can run:
```python
pipeline(A, data)
pipeline.add_pipe(B)
pipeline.add_pipe(C, is_end=True)
pipeline.run()
```
what pipeline.run() does is:
```python
for pipe in pipeline:
    try:
        pipe.check_input(data)
        pipe.process(data)
    except PipeInputError:
        # do error handling
    return data
```

if you want to run pipeline in a continuous loop, you can do
```python
pipeline.loop_run()
```
this line does
```python
while True:  # or use iterater until stop
    for pipe in pipeline:
        try:
            pipe.check_input(data)
            pipe.process(data)
        except PipeInputError:
            # do error handling
        return data
```
internally the pipeline can use async method to avoid waiting time
in addition, input/output type check is done before running the pipe, so to make sure the data flow is correct,
other wise, raise: PipeInputError, or PipeOutputError.

# how to config the pipes
the pipes are loaded by name and configured by a config file, e.g.,
a pipe named: compensate_dispersion.py, and a config file can be presented in the same folder, named
compensate_dispersion.cfg.

# what if the pipe contains multiple files?
then it should be saved in a subfolder in pipeline

