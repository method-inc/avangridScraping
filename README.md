# Scraping repo for avangrid proof of concept

## Setup

### using uv

Run the following command to install the repo's dependencies:

```bash
uv pip install -e .
```

[Installing uv](https://docs.astral.sh/uv/getting-started/installation/)

### using pip

Run the following command to install the repo's dependencies:

```bash
pip install -e .
```

## Authentication

### Reddit

set required .env variables

```bash
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
REDDIT_USERNAME=
REDDIT_PASSWORD=
```

How to get Reddit credentials: [Python Reddit API Wrapper (praw)](https://josephlai241.github.io/URS/credentials.html)

## Run

```bash
python hello.py
```
