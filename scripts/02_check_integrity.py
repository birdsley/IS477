{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔒 data/raw/annual_aqi_by_county_2018.csv: 861333cbdac9e08cda80f59ac32520b1b9b3dc4b334fab0e9f4c27198b274437\n",
      "🔒 data/raw/asthma_by_county.csv: dd6231e8c9bfc3e330f591c8b9ba25d4cd5fd6eedc2060196682cf730ce61a23\n",
      "checksums saved to data/checksums.json\n"
     ]
    }
   ],
   "source": [
    "import hashlib\n",
    "import os\n",
    "import json\n",
    "\n",
    "def compute_sha256(filepath):\n",
    "    with open(filepath, \"rb\") as f:\n",
    "        return hashlib.sha256(f.read()).hexdigest()\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    files = [\n",
    "        \"data/raw/annual_aqi_by_county_2018.csv\",\n",
    "        \"data/raw/asthma_by_county.csv\"\n",
    "    ]\n",
    "\n",
    "    os.makedirs(\"data\", exist_ok=True)\n",
    "    manifest = {}\n",
    "\n",
    "    for file in files:\n",
    "        checksum = compute_sha256(file)\n",
    "        manifest[file] = checksum\n",
    "        print(f\"{file}: {checksum}\")\n",
    "\n",
    "    with open(\"data/checksums.json\", \"w\") as f:\n",
    "        json.dump(manifest, f, indent=4)\n",
    "        print(\"checksums saved to data/checksums.json\")\n"
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
