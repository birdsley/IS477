#data quality profiling
import os
import pandas as pd

def main():
    raw_path = "data/raw"
    report_path = "data/profile_reports"

    os.makedirs(report_path, exist_ok=True)

    def profile_dataset(df, name):
        """Generate profiling statistics for a dataset."""
        report = []

        report.append(f" DATA PROFILE: {name}")
    #shape
        report.append(f"Rows: {df.shape[0]}")
        report.append(f"Columns: {df.shape[1]}\n")

    #data type
        report.append("Column Types:")
        report.append(df.dtypes.to_string())
        report.append("\n")

    #completeness
        report.append("Missing Values per Column:")
        report.append(df.isna().sum().to_string())
        report.append("\n")

    #duplicates
        dup_count = df.duplicated().sum()
        report.append(f"Duplicate Rows: {dup_count}\n")

    #uniqueness
        report.append("Unique Counts per Column:")
        report.append(df.nunique().to_string())
        report.append("\n")

    #state and counties
        possible_county_cols = [c for c in df.columns if "county" in c.lower()]
        possible_state_cols = [c for c in df.columns if "state" in c.lower()]

        report.append(f"County-like columns: {possible_county_cols}")
        report.append(f"State-like columns: {possible_state_cols}\n")

    #check casing/whitespace issues in key fields
        for col in possible_county_cols + possible_state_cols:
            if col in df.columns:
                cleaned = df[col].astype(str).str.lower().str.strip()
                mismatch = (cleaned != df[col].astype(str)).sum()
                report.append(f"Formatting fixes needed in {col}: {mismatch} rows")

        report.append("\n")

    #numeric value description
        numeric_cols = df.select_dtypes(include="number").columns
        if len(numeric_cols) > 0:
            report.append("Numeric Column Summary:")
            report.append(df[numeric_cols].describe().to_string())
            report.append("\n")

        return "\n".join(report)


    if __name__ == "__main__":
        aq_path = os.path.join(raw_path, "annual_aqi_by_county_2018.csv")
        asthma_path = os.path.join(raw_path, "asthma_by_county.csv")
        df_aq = pd.read_csv(aq_path)
        df_asthma = pd.read_csv(asthma_path)
        aq_report = profile_dataset(df_aq, "Air Quality (EPA)")
        asthma_report = profile_dataset(df_asthma, "Asthma (CDC)")

        with open(os.path.join(report_path, "air_quality_profile.txt"), "w") as f:
            f.write(aq_report)

        with open(os.path.join(report_path, "asthma_profile.txt"), "w") as f:
            f.write(asthma_report)

        print("Profiling complete. Reports saved to data/profile_reports/")

if __name__ == "__main__":
    main()
