import pandas as pd

def scrape_seao():
    # conservative placeholder ingestion
    # later replace with structured query endpoints

    tenders = [
        {
            "name": "Hydro infrastructure upgrade",
            "industry": "Energy",
            "province": "Quebec",
            "source": "SEAO"
        }
    ]

    return pd.DataFrame(tenders)