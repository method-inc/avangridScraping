from dotenv import load_dotenv
from backend.social.reddit import redditScraper
from backend.soaxScrapingApi.twitterScraper import SoaxTwitterPhotos
from backend.soaxScrapingApi.twitterRequests.photoSearch import (
    PhotoSearch,
    PhotoSearchParams,
)


def main():
    # Load env variables from .env file
    load_dotenv()

    print("Select a platform to search:")
    print("1. Twitter")
    print("2. Reddit")

    platform = input("Enter the number of the platform you would like to search: ")
    if platform == "1":
        previous_text_search = '"Local News"'
        previous_result_limit = 20

        scraper = SoaxTwitterPhotos(PhotoSearch(PhotoSearchParams()))

        while True:
            search = (
                input(f"Enter the search query [{previous_text_search}]: ")
                or previous_text_search
            )
            resultLimit = (
                input(
                    f"Enter the number of results to return [{previous_result_limit}]: "
                )
                or previous_result_limit
            )

            previous_text_search = search
            previous_result_limit = resultLimit

            params = PhotoSearchParams(
                count=resultLimit,
                query=search,
                result_type="recent",
                lang="en",
                since_id="0",
                max_id="9999999999999999999",
                radius="20mi",
                geocode="43.161030,-77.610924,20mi",  # "37.7749,-122.4194,1mi"
            )

            scraper.replaceParams(params)
            scraper.run(scraper.twitterHashtagSearchRequest)

    elif platform == "2":
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

        previous_subreddit = ""
        previous_search = ""
        previous_result_limit = 10

        while True:
            subreddit = (
                input(f"Enter the subreddit to search [{previous_subreddit}]: ")
                or previous_subreddit
            )
            search = (
                input(f"Enter the search query [{previous_search}]: ")
                or previous_search
            )
            resultLimit = (
                input(
                    f"Enter the number of results to return [{previous_result_limit}]: "
                )
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
