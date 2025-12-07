import os
import requests
import zipfile
import io
import pandas as pd
from io import StringIO

def download_and_save(url, local_filename):
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)
    print(f"Downloading from: {url}")
    response = requests.get(url)
    response.raise_for_status()

    if url.endswith(".zip"):
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            csv_filename = z.namelist()[0]
            print(f"Extracted: {csv_filename}")
            df = pd.read_csv(z.open(csv_filename))
    else:
        print(f"Downloaded: {url.split('/')[-1]}")
        df = pd.read_csv(StringIO(response.text))

    df.to_csv(local_filename, index=False)
    print(f"Saved to {local_filename}")
    return local_filename

def main():
    aq_url = "https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2018.zip"
    asthma_url = "https://data.cdc.gov/resource/mssc-ksj7.csv"

    download_and_save(aq_url, "data/raw/annual_aqi_by_county_2018.csv")
    download_and_save(asthma_url, "data/raw/asthma_by_county.csv")

if __name__ == "__main__":
    main()
