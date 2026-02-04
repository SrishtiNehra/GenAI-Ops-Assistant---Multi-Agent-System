import requests


def get_trending_repos():
    """
    Fetch top trending GitHub repositories by stars
    """

    url = "https://api.github.com/search/repositories?q=stars:>50000&sort=stars&order=desc"

    response = requests.get(url)

    data = response.json()

    repos = []

    for item in data["items"][:3]:
        repos.append({
            "name": item["name"],
            "stars": item["stargazers_count"],
            "url": item["html_url"]
        })

    return repos
