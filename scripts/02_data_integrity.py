import hashlib
import os
import json
def main():
    def compute_sha256(filepath):
        with open(filepath, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    if __name__ == "__main__":
        files = [
            "data/raw/annual_aqi_by_county_2018.csv",
            "data/raw/asthma_by_county.csv"
        ]

        os.makedirs("data", exist_ok=True)
        manifest = {}

        for file in files:
            checksum = compute_sha256(file)
            manifest[file] = checksum
            print(f"{file}: {checksum}")

        with open("data/checksums.json", "w") as f:
            json.dump(manifest, f, indent=4)
            print("checksums saved to data/checksums.json")

if __name__ == "__main__":
    main()
