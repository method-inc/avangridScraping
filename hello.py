from dotenv import load_dotenv
from backend.social.reddit import redditScraper


def main():
    # Load env variables from .env file
    load_dotenv()
    scraper = redditScraper.redditScraper()
    try:
        scraper.session.reddit.user.me()
    except:
        print(
            "\n".join(
                [
                    "Failed to authenticate with Reddit API. Please check your credentials.",
                    "Reddit API credentials should be set in a .env file in the root directory of the project.",
                ]
            )
        )
        return

    # CLI loop to search for posts by subreddit
    # Suggest previous search queries as default values
    previous_subreddit = ""
    previous_search = ""
    previous_result_limit = 10

    while True:
        subreddit = (
            input(f"Enter the subreddit to search [{previous_subreddit}]: ")
            or previous_subreddit
        )
        search = (
            input(f"Enter the search query [{previous_search}]: ") or previous_search
        )
        resultLimit = (
            input(f"Enter the number of results to return [{previous_result_limit}]: ")
            or previous_result_limit
        )

        resultLimit = int(resultLimit)  # Ensure resultLimit is an integer

        scraper.searchSubredditMostRecent(subreddit, search, resultLimit)

        # Update previous values
        previous_subreddit = subreddit
        previous_search = search
        previous_result_limit = resultLimit

        print("\n" * 2)
        print("Search again? [y/n]")
        if input().lower() != "y":
            break


if __name__ == "__main__":
    main()
