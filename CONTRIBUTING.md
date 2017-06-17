Development Environment Setup
=============================

Requirement: python 3.6.1
- Run python3 --version
- If version different than 3.6.1, install the 3.6.1 version

- Git clone this repository
- Inside the repository folder, run `python3 -m venv .`
- Run `source ./bin/activate`
- Run `pip install -r requirements.txt`

Git Workflow
============

[Git Flow](https://danielkummer.github.io/git-flow-cheatsheet/)

Commits
=======

Each commit should be minimal and independent.
A series of commits should tell a story.

Name your commits following the format:

:emoji: ISSUE-CODE Commit message

The commit message should be in the imperative present tense, capitalized and have fewer than 50 characters.

Examples:

- :rocket: #30 Create Color constants
- :green_heart: #30 Add test cases for valid parameters
- :green_heart: #30 Add test cases for invalid parameters
- :rocket: #30 Implement coloring function
- :bug: #30 Handle null parameter

Emoji List:

- :green_heart: When adding tests
- :rocket: When implementing features
- :bug: When fixing bugs
- :art: When fixing code style/structure
- :memo: Documentation

Style Guide
===========

[PEP 8](https://www.python.org/dev/peps/pep-0008/)
