import subprocess
import os
import sys

def run(script_path):
    print(f"\nRunning {script_path}")
    result = subprocess.run([sys.executable, script_path])
    
    if result.returncode != 0:
        print(f"Script failed: {script_path}")
        sys.exit(1)
    print(f"Completed: {script_path}")


if __name__ == "__main__":

    # list scripts in the order they should run
    scripts = [
        "scripts/01_data_acquisition.py",
        "scripts/02_data_integrity.py",
        "scripts/03_data_profiling.py",
        "scripts/04_data_cleaning.py",
        "scripts/05_db_connection.py",
        "scripts/06_data_integration.py",
        "scripts/07_analysis.py"
    ]

    for script in scripts:
        run(script)

    print("\nPipeline complete! All scripts executed successfully. You can now view results in the analysis folder. For more information and contextaulization, view the README and any other documentation.")
