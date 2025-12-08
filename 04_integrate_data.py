{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Integrated dataset created with 327 records\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import sqlite3\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    conn = sqlite3.connect(\"data/db/health_air_quality.db\")\n",
    "\n",
    "    df_aq = pd.read_sql(\"SELECT * FROM air_quality\", conn)\n",
    "    df_asthma = pd.read_sql(\"SELECT * FROM asthma\", conn)\n",
    "\n",
    "    # Standardize names for merging\n",
    "    df_aq['county_name'] = df_aq['County'].str.lower().str.strip()\n",
    "    df_aq['state_name'] = df_aq['State'].str.lower().str.strip()\n",
    "\n",
    "    df_asthma['county_name'] = df_asthma['countyname'].str.lower().str.strip()\n",
    "    df_asthma['state_name'] = df_asthma['statedesc'].str.lower().str.strip()\n",
    "\n",
    "    merged = pd.merge(\n",
    "        df_asthma,\n",
    "        df_aq,\n",
    "        on=['state_name', 'county_name'],\n",
    "        how='inner',\n",
    "        suffixes=('_asthma', '_aq')\n",
    "    )\n",
    "\n",
    "    os.makedirs(\"data/processed\", exist_ok=True)\n",
    "    merged.to_csv(\"data/processed/asthma_air_quality_merged.csv\", index=False)\n",
    "\n",
    "    print(f\"Integrated dataset created with {len(merged)} records\")\n",
    "    conn.close()"
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
