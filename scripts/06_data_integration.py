import os
import pandas as pd
import sqlite3

def main():

    conn = sqlite3.connect("data/db/health_air_quality.db")

    # Load data
    df_aq = pd.read_sql("SELECT * FROM air_quality", conn)
    df_asthma = pd.read_sql("SELECT * FROM asthma", conn)

    # Standardize names for merging
    df_aq['county_name'] = df_aq['County'].str.lower().str.strip()
    df_aq['state_name'] = df_aq['State'].str.lower().str.strip()

    df_asthma['county_name'] = df_asthma['countyname'].str.lower().str.strip()
    df_asthma['state_name'] = df_asthma['statedesc'].str.lower().str.strip()

    # Rename asthma columns according to metadata
    df_asthma = df_asthma.rename(columns={
        "totalpopulation": "population_2018",
        "casthma_crudeprev": "asthma_crude_prevalence",
        "casthma_crude95ci": "asthma_crude_prevalence_ci",
        "casthma_adjprev": "asthma_age_adjusted_prevalence",
        "casthma_adj95ci": "asthma_age_adjusted_prevalence_ci"
    })

    # Merge datasets
    merged = pd.merge(
        df_asthma,
        df_aq,
        on=['state_name', 'county_name'],
        how='inner',
        suffixes=('_asthma', '_aq')
    )

    # Select columns for output
    merged = merged[
        [
            "state_name",
            "county_name",
            "population_2018",
            "asthma_crude_prevalence",
            "asthma_crude_prevalence_ci",
            "asthma_age_adjusted_prevalence",
            "asthma_age_adjusted_prevalence_ci",
            "Days with AQI",
            "Good Days",
            "Moderate Days",
            "Unhealthy for Sensitive Groups Days",
            "Unhealthy Days",
            "Very Unhealthy Days",
            "Hazardous Days",
            "Max AQI",
            "90th Percentile AQI",
            "Median AQI",
        ]
    ]

    # Save processed file
    os.makedirs("data/processed", exist_ok=True)
    merged.to_csv("data/processed/asthma_air_quality_merged.csv", index=False)

    print(f"Integrated dataset created with {len(merged)} records")

    conn.close()


if __name__ == "__main__":
    main()
