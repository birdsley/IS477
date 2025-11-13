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
      "data successfully stored in SQLite database: data/db/health_air_quality.db\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import sqlite3\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    os.makedirs(\"data/db\", exist_ok=True)\n",
    "    conn = sqlite3.connect(\"data/db/health_air_quality.db\")\n",
    "\n",
    "    df_aq = pd.read_csv(\"data/raw/annual_aqi_by_county_2018.csv\")\n",
    "    df_asthma = pd.read_csv(\"data/raw/asthma_by_county.csv\")\n",
    "\n",
    "    df_aq.to_sql(\"air_quality\", conn, if_exists=\"replace\", index=False)\n",
    "    df_asthma.to_sql(\"asthma\", conn, if_exists=\"replace\", index=False)\n",
    "\n",
    "    conn.close()\n",
    "    print(\"data successfully stored in SQLite database: data/db/health_air_quality.db\")"
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
