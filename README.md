sloths
======

[![PyPI](https://img.shields.io/pypi/v/sloths.svg)](https://pypi.org/project/sloths/)
[![Python 3.x](https://img.shields.io/pypi/pyversions/sloths.svg?logo=python&logoColor=white)](https://pypi.org/project/sloths/)
[![Tests](https://github.com/lirsacc/sloths-py/workflows/Checks/badge.svg)](https://github.com/lirsacc/sloths-py/actions?query=workflow%3AChecks)
[![Documentation Status](https://readthedocs.org/projects/sloths-py/badge/?version=latest)](https://sloths-py.readthedocs.io/en/latest/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lirsacc/sloths-py/blob/main/LICENSE)

Lazy iterator pipelines for Python.

`sloths` is a library providing a chainable interface to easily compose lazy iterator pipelines in Python. The interface is largely inspired by Rust's Iterator trait (although it's not a carbon copy).

The 2 primary goals of the library are:

- Provide an easy to use, chainable and typed API for composing generator pipelines.
- Make it easy to control peak memory usage and throughput on large source datasets or long running input streams.

```python
>>> from sloths import Stream
>>> Stream(range(100_000)).enumerate().filter(lambda x: x[1] % 3 == 0).skip(3).take(5).collect()
[(9, 9), (12, 12), (15, 15), (18, 18), (21, 21)]

```

For more examples check out the [full usage documentation](https://sloths-py.readthedocs.io/en/latest/usage.html) or the [cookbook](https://sloths-py.readthedocs.io/en/latest/cookbook.html).

Installation
------------

The project is released [on PyPI](https://pypi.org/project/sloths/).

```shell
pip install sloths
```
