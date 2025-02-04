from backend.Scraper import Scraper
from backend.social.reddit import prawSession
import json


class redditScraper(Scraper):
    name = "reddit"
    limit = 5
    queries = 0

    def __init__(self) -> None:
        self.session = prawSession.prawSession()

    def _overLimit(self) -> bool:
        if self.queries >= self.limit:
            print(
                "Query limit reached, please manually override if needed using the manualLimitOverride method"
            )
        return self.queries >= self.limit

    def manualLimitOverride(self, limit: int) -> None:
        self.limit = limit

    def searchSubredditMostRecent(
        self, subreddit: str, search: str, resultLimit: int
    ) -> list:
        """method to run a text search on a given subreddit
        Returns a list of the most recent posts that match the search query
        Args:
            subreddit (str): the subreddit to search
            search (str): the search query
        """

        if self._overLimit():
            return []
        results = []
        for submission in self.session.reddit.subreddit(subreddit).search(
            search, limit=resultLimit, sort="new", time_filter="all"
        ):
            object = {
                "title": submission.title,
                "url": submission.url,
                "text": submission.selftext,
                "author": submission.author,
                "created": submission.created_utc,
                "score": submission.score,
                "upvote_ratio": submission.upvote_ratio,
            }
            results.append(object)
        self.queries += 1
        self._cache(results)
        return results

    def _cache(self, result: list) -> None:
        """method to cache the results of a search to local storage
        Args:
            result (list): the list of search results to cache
        """
        # append the results to the cache file
        if len(result) > 0:
            with open("cache/cache.txt", "a") as file:
                for item in result:
                    file.write(str(item))
                    file.write("\n")
