import requests
import pandas as pd
from bs4 import BeautifulSoup
from config import INDUSTRIES

HEADERS = {"User-Agent": "Mozilla/5.0"}

def scrape_mock_directory():
    """
    Replace URLs later with CCC + Quebec directories.
    Structure already production-ready.
    """

    companies = []

    sample_sources = [
        {
            "name": "Norda Stelo",
            "industry": "Engineering",
            "province": "Quebec",
            "city": "Quebec City",
            "language": "French",
            "services": "Engineering & Procurement"
        },
        {
            "name": "Chrono Aviation",
            "industry": "Aviation Charter",
            "province": "Quebec",
            "city": "Montreal",
            "language": "French",
            "services": "Remote charter flights"
        }
    ]

    for c in sample_sources:
        companies.append(c)

    return pd.DataFrame(companies)

def run_scraper():
    df = scrape_mock_directory()
    df.to_csv("data/companies.csv", index=False)
    print("Dataset updated.")

if __name__ == "__main__":
    run_scraper()