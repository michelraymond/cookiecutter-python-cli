## What is this?

A default template for a new CLI project, written in Python, to be used
with the [cookiecutter](https://cookiecutter.readthedocs.io) utility. 
Deals with all the boilerplate involved in the setuptools setup, etc.


## How do I use this?

Here's my preferred path to bliss:

1. Start by installing `pipenv`.  It's awesome.
   `$ pip3 install --user pipenv`
2. Now install Cookiecutter:
   `$ pipenv install cookiecutter`.
3. Now use Cookiecutter to create your brand new project:
   `$ pipenv run cookiecutter https://github.com/michelraymond/cookiecutter-python-cli`


## How to answer these questions?

When running Cookiecutter, you'll need to provide some values.
Here's what they're for:

* `project_name` -- "My Tool"   (Used for marketing.  Keep it short and capitalize accordingly.)
* `repo_name` -- "python-mytool"  (Name of the GitHub repo.)
* `pypi_name` -- "mytool"   (Name on PyPI, i.e. what people type to `pip install`.)
* `script_name` -- "my-tool"  (Binary of the script, i.e. what people will run on the command line.)
* `package_name` -- "my_tool"  (Name of the Python module/package used internally.)


## License

Liberally licensed under BSD terms.

[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks!-%F0%9F%A6%89-1EAEDB.svg)](https://saythanks.io/to/michelraymond)
