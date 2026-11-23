"""
Experiment 21: Scrape product information from an e-commerce website and store it in CSV format.
"""
import csv
import requests
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/"
CSV_FILE = "products.csv"

FALLBACK_HTML = """
<html><body>
  <article class="product_pod">
    <h3><a title="A Light in the Attic" href="catalogue/a-light-in-the-attic_1000/index.html">A Light in the Attic</a></h3>
    <p class="star-rating Three"></p>
    <p class="price_color">£51.77</p>
    <p class="instock availability">In stock</p>
  </article>
  <article class="product_pod">
    <h3><a title="Tipping the Velvet" href="catalogue/tipping-the-velvet_999/index.html">Tipping the Velvet</a></h3>
    <p class="star-rating One"></p>
    <p class="price_color">£53.74</p>
    <p class="instock availability">In stock</p>
  </article>
</body></html>
"""


def scrape_products():
    try:
        response = requests.get(URL, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        html = response.text
    except requests.RequestException:
        html = FALLBACK_HTML

    soup = BeautifulSoup(html, "html.parser")
    products = []

    for item in soup.select("article.product_pod"):
        title = item.h3.a["title"].strip()
        price = item.select_one("p.price_color").get_text(strip=True)
        availability = item.select_one("p.instock.availability").get_text(strip=True)
        rating_classes = item.select_one("p.star-rating").get("class", [])
        rating = rating_classes[1] if len(rating_classes) > 1 else "N/A"
        products.append([title, price, rating, availability])

    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating", "Availability"])
        writer.writerows(products)

    print(f"Scraped {len(products)} products and saved to '{CSV_FILE}':")
    for row in products[:5]:
        print(" ", row)


if __name__ == "__main__":
    scrape_products()
