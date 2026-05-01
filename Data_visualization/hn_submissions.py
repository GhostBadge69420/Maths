from operator import itemgetter

import requests


def fetch_json(url):
    """Fetch JSON data from a URL."""
    response = requests.get(url, timeout=10)
    print("Status code:", response.status_code)
    response.raise_for_status()
    return response.json()


def fetch_top_submissions(limit=30):
    """Fetch and sort the top Hacker News submissions by comments."""
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    submission_ids = fetch_json(url)

    submission_dicts = []
    for submission_id in submission_ids[:limit]:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        response_dict = fetch_json(url)
        submission_dicts.append({
            "title": response_dict.get("title", "No title"),
            "link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict.get("descendants", 0),
        })

    return sorted(submission_dicts, key=itemgetter("comments"), reverse=True)


def main():
    """Print popular Hacker News submissions."""
    for submission_dict in fetch_top_submissions():
        print("\nTitle:", submission_dict["title"])
        print("Discussion link:", submission_dict["link"])
        print("Comments:", submission_dict["comments"])


if __name__ == "__main__":
    main()
