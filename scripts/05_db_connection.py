#creating sql database
import os
import pandas as pd
import sqlite3

def main():
    if __name__ == "__main__":
        os.makedirs("data/db", exist_ok=True)
        conn = sqlite3.connect("data/db/health_air_quality.db")

        df_aq = pd.read_csv("data/processed/air_quality_cleaned.csv")
        df_asthma = pd.read_csv("data/processed/asthma_cleaned.csv")

        df_aq.to_sql("air_quality", conn, if_exists="replace", index=False)
        df_asthma.to_sql("asthma", conn, if_exists="replace", index=False)

        conn.close()
        print("data successfully stored in SQLite database: data/db/health_air_quality.db")

if __name__ == "__main__":
    main()
