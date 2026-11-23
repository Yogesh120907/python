"""
Experiment 20: Extract news headlines and hyperlinks from a web page using Beautiful Soup.
"""
import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/"

FALLBACK_HTML = """
<html><body>
  <span class="titleline"><a href="https://www.python.org/downloads/">Python 3.13 Released with Major Performance Gains</a></span>
  <span class="titleline"><a href="https://numpy.org/news/">NumPy 2.0 Improves Vectorized Array Operations</a></span>
  <span class="titleline"><a href="https://pandas.pydata.org/">Pandas Introduces Faster PyArrow Backend by Default</a></span>
</body></html>
"""


def scrape_headlines(url):
    try:
        response = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        html = response.text
        source = url
    except requests.RequestException:
        html = FALLBACK_HTML
        source = "Offline Sample HTML"

    soup = BeautifulSoup(html, "html.parser")
    articles = soup.select("span.titleline > a")

    print(f"Source: {source}\n" + "-" * 65)
    for idx, tag in enumerate(articles[:15], start=1):
        headline = tag.get_text(strip=True)
        link = tag.get("href", "")
        print(f"{idx:02d}. {headline}\n    Link: {link}")


if __name__ == "__main__":
    scrape_headlines(URL)
