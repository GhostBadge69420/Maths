from pathlib import Path

import requests

from plotly.graph_objects import Bar
from plotly import offline

BASE_DIR = Path(__file__).resolve().parent


def fetch_python_repos():
    """Fetch the most-starred Python repositories from GitHub."""
    url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers, timeout=10)
    print(f"Status code: {response.status_code}")
    response.raise_for_status()
    return response.json()["items"]


def prepare_repo_chart_data(repo_dicts):
    """Prepare repository names, star counts, and hover labels."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict["name"]
        repo_url = repo_dict["html_url"]
        repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
        stars.append(repo_dict["stargazers_count"])

        owner = repo_dict["owner"]["login"]
        description = repo_dict["description"] or "No description provided."
        labels.append(f"{owner}<br/>{description}")
    return repo_links, stars, labels


def make_chart(repo_links, stars, labels, output_file):
    """Save a bar chart of popular Python repositories."""
    data = [{
        "type": "bar",
        "x": repo_links,
        "y": stars,
        "hovertext": labels,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width": 1.5, "color": "rgb(25, 25, 25)"},
        },
        "opacity": 0.6,
    }]

    layout = {
        "title": "Most-Starred Python Projects on GitHub",
        "xaxis": {"title": "Repository"},
        "yaxis": {"title": "Stars"},
    }
    offline.plot(
        {"data": data, "layout": layout},
        filename=str(output_file),
        auto_open=False,
    )


def main():
    """Fetch GitHub data and save the visualization."""
    repo_dicts = fetch_python_repos()
    repo_links, stars, labels = prepare_repo_chart_data(repo_dicts)
    output_file = BASE_DIR / "Python_repos.html"
    make_chart(repo_links, stars, labels, output_file)
    print(f"Saved Python repository chart to {output_file}")


if __name__ == "__main__":
    main()
