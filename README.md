# Pytest-demo: a repo for exploring basic pytest features

## Prerequisites
1. [git](https://git-scm.com/downloads)
2. [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

Just  [Clone the repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)!

#### Example with SSH:
```bash
git clone git@github.com:jwjacobson/pytest-demo.git && cd pytest-demo
```

## Using the repo

The repo consists of four branches: `main` (the default branch), `basics`, `calculator`, and `fastapi`. Switch between them using `git switch`:

```bash
git switch basics
git switch calculator
etc.
```

`Basics` contains two simple tests that run on their own without testing any application code: it demonstrates the concepts of tests and assertions.

`Calculator` contains the beginning of a hypothetical calculator app to demonstrate testing application code.

`Fastapi` contains a minimal FastAPI app for submitting contact data plus tests to demonstrate testing a web app.

To run pytest:

```
uv run pytest
```
