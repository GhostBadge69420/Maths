import json
from pathlib import Path

import requests


DATA_DIR = Path(__file__).resolve().parent / "data"


def fetch_item(item_id):
    """Fetch a single Hacker News item."""
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    response = requests.get(url, timeout=10)
    print(f"Status code: {response.status_code}")
    response.raise_for_status()
    return response.json()


def main():
    """Fetch one Hacker News article and save readable JSON."""
    response_dict = fetch_item(19155826)
    readable_file = DATA_DIR / "readable_hn_data.json"
    with open(readable_file, "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4)
    print(f"Saved article data to {readable_file}")


if __name__ == "__main__":
    main()
