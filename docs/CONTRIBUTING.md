<!-- ⚠️ This README has been generated from the file(s) ".config/docs/blueprint-contributing.md" ⚠️-->

<a href="#contributing" style="width:100%"><img style="width:100%" src="https://gitlab.com/megabyte-labs/assets/-/raw/master/png/aqua-divider.png" /></a>

# }Contributing

First of all, thanks for visiting this page 😊 ❤️ ! We are totally ecstatic that you may be considering contributing to this project. You should read this guide if you are considering creating a pull request.

<a href="#table-of-contents" style="width:100%"><img style="width:100%" src="https://gitlab.com/megabyte-labs/assets/-/raw/master/png/aqua-divider.png" /></a>

## Table of Contents

- [}Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)
  - [Overview](#overview)
  - [Pull Requests](#pull-requests)
    - [How to Commit Code](#how-to-commit-code)
    - [Pre-Commit Hook](#pre-commit-hook)

<a href="#code-of-conduct" style="width:100%"><img style="width:100%" src="https://gitlab.com/megabyte-labs/assets/-/raw/master/png/aqua-divider.png" /></a>

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](https://gitlab.com/megabyte-labs/python/SLUG/-/blob/master/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [contact_email](mailto:contact_email).

<a href="#overview" style="width:100%"><img style="width:100%" src="https://gitlab.com/megabyte-labs/assets/-/raw/master/png/aqua-divider.png" /></a>

## Overview

<a href="#pull-requests" style="width:100%"><img style="width:100%" src="https://gitlab.com/megabyte-labs/assets/-/raw/master/png/aqua-divider.png" /></a>

## Pull Requests

All pull requests should be associated with issues. You can find the [issues board on GitLab](https://gitlab.com/megabyte-labs/python/SLUG/-/issues). The pull requests should be made to [the GitLab repository](https://gitlab.com/megabyte-labs/python/SLUG) instead of the [GitHub repository](ProfessorManhattan/python-SLUG). This is because we use GitLab as our primary repository and mirror the changes to GitHub for the community.

### How to Commit Code

Instead of using `git commit`, we prefer that you use `npm run commit`. You will understand why when you try it but basically it streamlines the commit process and helps us generate better CHANGELOG.md files.

### Pre-Commit Hook

Even if you decide not to use `npm run commit`, you will see that `git commit` behaves differently because there is a pre-commit hook that installs automatically after you run `npm i`. This pre-commit hook is there to test your code before committing and help you become a better coder. If you need to bypass the pre-commit hook, then you may add the `--no-verify` tag at the end of your `git commit` command (e.g. `git commit -m "Commit" --no-verify`).
