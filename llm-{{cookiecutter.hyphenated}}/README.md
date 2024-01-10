# llm-{{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/llm-{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/llm-{{ cookiecutter.hyphenated }}/){% if cookiecutter.github_username %}
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/llm-{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/llm-{{ cookiecutter.hyphenated }}/releases)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/llm-{{ cookiecutter.hyphenated }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/llm-{{ cookiecutter.hyphenated }}/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/llm-{{ cookiecutter.hyphenated }}/blob/main/LICENSE){% endif %}

{{ cookiecutter.description or "" }}

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

    llm install llm-{{ cookiecutter.hyphenated }}

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-{{ cookiecutter.hyphenated }}
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
