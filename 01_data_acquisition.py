{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "downloading from: https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2018.zip\n",
      "Extracted: annual_aqi_by_county_2018.csv\n",
      "saved to data/raw/annual_aqi_by_county_2018.csv\n",
      "downloading from: https://data.cdc.gov/resource/mssc-ksj7.csv\n",
      "downloaded: mssc-ksj7.csv\n",
      "saved to data/raw/asthma_by_county.csv\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import requests\n",
    "import zipfile\n",
    "import io\n",
    "import pandas as pd\n",
    "from io import StringIO\n",
    "\n",
    "def download_and_save(url, local_filename):\n",
    "    os.makedirs(os.path.dirname(local_filename), exist_ok=True)\n",
    "    print(f\"downloading from: {url}\")\n",
    "    response = requests.get(url)\n",
    "    response.raise_for_status()\n",
    "\n",
    "    if url.endswith(\".zip\"):\n",
    "        with zipfile.ZipFile(io.BytesIO(response.content)) as z:\n",
    "            csv_filename = z.namelist()[0]\n",
    "            print(f\"Extracted: {csv_filename}\")\n",
    "            df = pd.read_csv(z.open(csv_filename))\n",
    "    else:\n",
    "        print(f\"downloaded: {url.split('/')[-1]}\")\n",
    "        df = pd.read_csv(StringIO(response.text))\n",
    "\n",
    "    df.to_csv(local_filename, index=False)\n",
    "    print(f\"saved to {local_filename}\")\n",
    "    return local_filename\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    aq_url = \"https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2018.zip\"\n",
    "    asthma_url = \"https://data.cdc.gov/resource/mssc-ksj7.csv\"\n",
    "\n",
    "    download_and_save(aq_url, \"data/raw/annual_aqi_by_county_2018.csv\")\n",
    "    download_and_save(asthma_url, \"data/raw/asthma_by_county.csv\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
