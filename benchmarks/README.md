# Logging Benchmarks

Benchmarks to test various logging situations.

## Silent logging

These tests will set the verbosity level to `0` and log a message which will not be output to console.

* [log-silent-cpython.py](log-silent-cpython.py): Use cpython
* [log-silent-pypy.py](log-silent-pypy.py): Use pypy
* [log-silent-cpython-optimized.py](log-silent-cpython-optimized.py): Use cpython with `-O` flag
* [log-silent-pypy-optimized.py](log-silent-pypy-optimized.py): Use pypy with `-O` flag
