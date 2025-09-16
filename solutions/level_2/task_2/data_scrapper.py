import requests
from bs4 import BeautifulSoup
import csv

def scrape_headlines(url="https://news.ycombinator.com/"):
    """
    Scrapes headlines from a given URL and saves them to headlines.csv.

    :param url: URL to scrape headlines from (default: https://news.ycombinator.com/)
    """
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    titles = [a.get_text() for a in soup.select(".titleline a")]

    with open("headlines.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Headline"])
        for t in titles:
            writer.writerow([t])
    print("Headlines saved to headlines.csv")

    return titles

if __name__ == "__main__":
    scrape_headlines()
