import os
import json
import urllib.request

def fetch_pypi_stats():
    url = "https://pypistats.org/api/packages/pybleton/recent"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            # Sum up downloads for the last month as our total download metric for the landing page
            return data.get("data", {}).get("last_month", 0)
    except Exception as e:
        print(f"Error fetching PyPI stats: {e}")
        return 0

def fetch_github_stats():
    url = "https://api.github.com/repos/whs2k/pybleton"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return {
                "stars": data.get("stargazers_count", 0),
                "forks": data.get("forks_count", 0),
                "issues": data.get("open_issues_count", 0)
            }
    except Exception as e:
        print(f"Error fetching GitHub stats: {e}")
        return {"stars": 0, "forks": 0, "issues": 0}

def main():
    downloads = fetch_pypi_stats()
    gh_stats = fetch_github_stats()
    
    stats = {
        "downloads": downloads,
        "stars": gh_stats["stars"],
        "forks": gh_stats["forks"],
        "issues": gh_stats["issues"]
    }
    
    os.makedirs("docs", exist_ok=True)
    with open("docs/stats.json", "w") as f:
        json.dump(stats, f, indent=2)
    print(f"Updated stats: {stats}")

if __name__ == "__main__":
    main()
