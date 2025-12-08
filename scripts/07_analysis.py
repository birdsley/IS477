import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def main():

    plt.style.use("seaborn-v0_8")
    sns.set_palette("deep")

    output_path = "results/analysis"
    os.makedirs(output_path, exist_ok=True)

    def save_fig(name):
        plt.tight_layout()
        plt.savefig(f"{output_path}/{name}.png", dpi=300)
        plt.close()

    if __name__ == "__main__":
        df = pd.read_csv("data/processed/asthma_air_quality_merged.csv")

        numeric_df = df.select_dtypes(include=[np.number]).copy()
        numeric_cols = numeric_df.columns.tolist()

        print(f"Using {len(numeric_cols)} numeric columns for analysis.")
        print(numeric_cols[:20])

        summary = numeric_df.describe().T
        summary.to_csv(f"{output_path}/summary_statistics.csv")

        asthma_metrics = [
            "Asthma_Crude_Prevalence",
            "Asthma_Crude_Prevalence_CI",
            "Asthma_Age_Adjusted_Prevalence",
            "Asthma_Age_Adjusted_Prevalence_Ci"
        ]
        asthma_metrics = [c for c in asthma_metrics if c in numeric_cols]

        for col in asthma_metrics:
            plt.figure(figsize=(6,4))
            sns.histplot(numeric_df[col], kde=True)
            plt.title(f"Distribution of {col}")
            save_fig(f"dist_{col}")

        aq_metrics = ["Days with AQI", "Good Days", "Unhealthy Days", "Max AQI"]
        aq_metrics = [c for c in aq_metrics if c in numeric_cols]

        for col in aq_metrics:
            plt.figure(figsize=(6,4))
            sns.histplot(numeric_df[col], kde=True)
            plt.title(f"Distribution of {col}")
            save_fig(f"dist_{col}")

        corr = numeric_df.corr()

        plt.figure(figsize=(12,10))
        sns.heatmap(corr, cmap="coolwarm", annot=False, center=0)
        plt.title("Correlation Heatmap – Asthma & Air Quality (Numeric Only)")
        save_fig("correlation_heatmap")

        asthma_numeric = [c for c in asthma_metrics if c in numeric_cols]
        aq_numeric = [c for c in aq_metrics if c in numeric_cols]

        pair_corr = numeric_df[asthma_numeric + aq_numeric].corr()
        plt.figure(figsize=(8,6))
        sns.heatmap(pair_corr, annot=True, cmap="vlag")
        plt.title("Asthma vs Air Quality – Focused Correlation Matrix")
        save_fig("asthma_aq_pair_corr")

        for asth_col in asthma_numeric:
            for aq_col in aq_numeric:
                plt.figure(figsize=(6,4))
                sns.regplot(
                    x=numeric_df[aq_col],
                    y=numeric_df[asth_col],
                    scatter_kws={"alpha": 0.35}
                )
                plt.title(f"{asth_col} vs {aq_col}")
                save_fig(f"scatter_{asth_col}_vs_{aq_col}")

        required_cols = {"county_name", "Max AQI", "asthma_crude_prevalence"}

        if required_cols.issubset(df.columns):

            worst10 = df.sort_values("Max AQI", ascending=False).head(10)

            plt.figure(figsize=(10, 6))
            sns.barplot(
                data=worst10,
                x="county_name",
                y="asthma_crude_prevalence"
            )

            plt.xticks(rotation=45, ha="right")
            plt.ylabel("Asthma Crude Prevalence (%)")
            plt.title("Asthma Prevalence in the 10 Worst Air-Quality Counties")

            mean_asthma = df["asthma_crude_prevalence"].mean()
            plt.axhline(mean_asthma, color="red", linestyle="--", label=f"Mean Asthma ({mean_asthma:.2f}%)")
            plt.legend()

            save_fig("worst10_airquality_asthma")

            correlation = df["asthma_crude_prevalence"].corr(df["Max AQI"])

            # Save correlation as a text file
            with open(f"{output_path}/asthma_air_quality_correlation.txt", "w") as f:
                f.write(f"Correlation between asthma prevalence and Max AQI: {correlation:.4f}\n")

            print(f"Correlation between asthma prevalence and Max AQI: {correlation:.4f}")

        else:
            print("Could not compute worst-air-quality chart or correlation. Columns missing:")
            missing = required_cols - set(df.columns)
            print(missing)
        
        print("Analysis complete. Figures saved to results/analysis/")

if __name__ == "__main__":
    main()
