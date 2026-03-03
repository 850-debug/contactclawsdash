import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://amq-inc.com/en/members/"

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_amq():
    r = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(r.text, "html.parser")

    companies = []

    cards = soup.select("article")  # adaptable selector

    for c in cards:
        name = c.get_text(strip=True)

        companies.append({
            "name": name,
            "industry": "Mining",
            "province": "Quebec",
            "source": "AMQ"
        })

    return pd.DataFrame(companies)