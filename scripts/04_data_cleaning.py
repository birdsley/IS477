import pandas as pd
import numpy as np
import re
import os

#air quality cleaning functions

def main():
    def clean_air_quality(df):
        df = df.copy()

        df["State"] = df["State"].astype(str).str.strip().str.upper()
        df["County"] = (
            df["County"]
            .astype(str)
            .str.strip()
            .str.title()
            .str.replace(" County", "", regex=False)
            .str.replace(" Parish", "", regex=False)
        )

        numeric_cols = df.select_dtypes(include=["float", "int"]).columns.tolist()
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")


        category_cols = [
            "Good Days", "Moderate Days",
            "Unhealthy for Sensitive Groups Days",
            "Unhealthy Days", "Very Unhealthy Days", "Hazardous Days"
        ]

        df["sum_category_days"] = df[category_cols].sum(axis=1)
        df["days_mismatch"] = df["Days with AQI"] - df["sum_category_days"]

        # Optional: fix mismatches by adjusting “Moderate Days”
        df.loc[df["days_mismatch"] != 0, "Moderate Days"] += df["days_mismatch"]

        df.drop(columns=["sum_category_days", "days_mismatch"], inplace=True)


        #sanity check, AQI cannot exceed 500 normally → flag or cap
        df["Max AQI"] = df["Max AQI"].clip(upper=500)

    #standardize FIPS
        if "FIPS" not in df.columns:
            df["FIPS"] = None
        

        return df


    #asthma cleaning

    def clean_cdc_asthma(df):
        df = df.copy()

        #state and county
        df["stateabbr"] = df["stateabbr"].astype(str).str.upper().str.strip()
        df["statedesc"] = df["statedesc"].astype(str).str.title().str.strip()
        df["countyname"] = (
            df["countyname"]
            .astype(str)
            .str.title()
            .str.replace(" County", "", regex=False)
            .str.strip()
        )

        # standardize FIPS
        df["countyfips"] = df["countyfips"].astype(str).str.zfill(5)

        #parsing confidence interval string 
        ci_cols = [c for c in df.columns if c.endswith("95ci")]

        def parse_ci(ci_text):
            if not isinstance(ci_text, str):
                return (np.nan, np.nan)

            nums = re.findall(r"[\d\.]+", ci_text)
            if len(nums) == 2:
                return float(nums[0]), float(nums[1])
            return (np.nan, np.nan)

        for col in ci_cols:
            df[col + "_low"] = df[col].apply(lambda x: parse_ci(x)[0])
            df[col + "_high"] = df[col].apply(lambda x: parse_ci(x)[1])

        # convert crude/adj prevalence columns
        prev_cols = [c for c in df.columns if c.endswith("crudeprev") or c.endswith("adjprev")]
        df[prev_cols] = df[prev_cols].apply(pd.to_numeric, errors="coerce")

        #remove out-of-range prevalence % values
        for col in prev_cols:
            df.loc[(df[col] < 0) | (df[col] > 100), col] = np.nan

        #split geolocation
        def extract_lat_lon(text):
            m = re.findall(r"-?\d+\.\d+", text)
            if len(m) == 2:
                return float(m[0]), float(m[1])
            return (np.nan, np.nan)

        df["lat"] = df["geolocation"].apply(lambda x: extract_lat_lon(x)[0])
        df["lon"] = df["geolocation"].apply(lambda x: extract_lat_lon(x)[1])



        return df


    #run all functions

    def clean_all(epa_df, cdc_df):
        clean_epa = clean_air_quality(epa_df)
        clean_cdc = clean_cdc_asthma(cdc_df)
        return clean_epa, clean_cdc

    epa_raw=pd.read_csv("data/raw/annual_aqi_by_county_2018.csv")
    cdc_raw=pd.read_csv("data/raw/asthma_by_county.csv")

    clean_epa, clean_cdc = clean_all(epa_raw, cdc_raw)

    clean_epa.to_csv('data/processed/air_quality_cleaned.csv')
    clean_cdc.to_csv('data/processed/asthma_cleaned.csv')

if __name__ == "__main__":
    main()
