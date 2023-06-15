Each chapter's python file is a book's question with my answer (often with multiple implementations). Tests for the answers are written in the same file (implemented with [pytest](https://docs.pytest.org/en/7.3.x/)).

Other solutions in python:
* [careercup (book's official)](https://github.com/careercup/CtCI-6th-Edition-Python)
* [w-hat](https://github.com/w-hat/ctci-solutions)


## Verify/test the answers

First, you need to have python [poetry](https://python-poetry.org).

```shell
# Install
poetry install


# Test
# - Test all questions&answers
pytest ch*/*
# - Test a single question (for instance)
pytest ch01*/q02*
```