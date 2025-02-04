import tweepy
import os


class twitterSession:
    def __init__(self):
        oauth2_user_handler = tweepy.OAuth2UserHandler(
            client_id=os.getenv("TWITTER_CLIENT_ID"),
            redirect_uri="http://localhost:8000",
            scope=["tweet.read", "users.read"],
            client_secret=os.environ.get("TWITTER_CLIENT_SECRET"),
        )

        oauth1_user_handler = tweepy.OAuth1UserHandler(
            "API / Consumer Key here",
            "API / Consumer Secret here",
            callback="Callback / Redirect URI / URL here",
        )
