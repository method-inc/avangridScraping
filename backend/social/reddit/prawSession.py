import praw
import os


class prawSession:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.environ.get("REDDIT_CLIENT_ID"),
            client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
            user_agent=os.environ.get("REDDIT_USER_AGENT"),
            username=os.environ.get("REDDIT_USERNAME"),
            password=os.environ.get("REDDIT_PASSWORD"),
        )
