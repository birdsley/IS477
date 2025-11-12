This repository explores the links between asthma and poor air quality over time. Our data workflow allows us to acquire, process, save, and document all data necessary to reproduce the results.


**Data Acquisition Documentation**

1. Air Quality Data
We obtained annual county-level air quality data from the EPA’s Air Quality System (AQS). This dataset contains detailed measurements from monitoring sites in specific counties (note: not all U.S. counties are included).

Schema:

| Field Position | Field Name                   | Description                                                                       |
| -------------- | ---------------------------- | --------------------------------------------------------------------------------- |
| 1              | State Code                   | FIPS code of the state where the monitor resides                                  |
| 2              | County Code                  | FIPS code of the county where the monitor resides                                 |
| 3              | Site Num                     | Unique number within the county identifying the monitoring site                   |
| 4              | Parameter Code               | AQS code for the parameter measured by the monitor                                |
| 5              | POC                          | Parameter Occurrence Code distinguishing instruments measuring the same parameter |
| 6              | Latitude                     | Latitude of the monitoring site in decimal degrees                                |
| 7              | Longitude                    | Longitude of the monitoring site in decimal degrees                               |
| 8              | Datum                        | Datum associated with Latitude and Longitude measures                             |
| 9              | Parameter Name               | Name/description of the measured parameter (pollutant or non-pollutant)           |
| 10             | Sample Duration              | Length of time air passes through the monitor before analysis                     |
| 11             | Pollutant Standard           | Description of the ambient air quality standard rules                             |
| 12             | Metric Used                  | Base metric used in aggregate statistics (e.g., Daily Maximum)                    |
| 13             | Method Name                  | Description of processes, equipment, and protocols used                           |
| 14             | Year                         | Year the annual summary represents                                                |
| 15             | Units of Measure             | Standard unit of the measured parameter                                           |
| 16             | Event Type                   | Indicates whether exceptional events (e.g., wildfires) are included or excluded   |
| 17             | Observation Count            | Number of observations taken during the year                                      |
| 18             | Observation Percent          | Percent of scheduled observations taken                                           |
| 19             | Completeness Indicator       | Whether regulatory completeness criteria were met (Y/N)                           |
| 20             | Valid Day Count              | Number of days with valid monitoring criteria                                     |
| 21             | Required Day Count           | Scheduled number of sampling days                                                 |
| 22             | Exceptional Data Count       | Data points affected by exceptional air quality events                            |
| 23             | Null Data Count              | Scheduled samples when no data was collected                                      |
| 24             | Primary Exceedance Count     | Number of samples exceeding primary air quality standard                          |
| 25             | Secondary Exceedance Count   | Number of samples exceeding secondary air quality standard                        |
| 26             | Certification Indicator      | Certification status of the annual summary data                                   |
| 27             | Num Obs Below MDL            | Number of samples below method detection limit (MDL)                              |
| 28–48          | Various statistical measures | Annual mean, max values, percentiles, standard deviations                         |
| 49             | Local Site Name              | Name of the site given by state/local/tribal agency                               |
| 50             | Address                      | Approximate street address of monitoring site                                     |
| 51             | State Name                   | Name of the state                                                                 |
| 52             | County Name                  | Name of the county                                                                |
| 53             | City Name                    | Legal city boundaries of the monitoring site                                      |
| 54             | CBSA Name                    | Core Based Statistical Area (metropolitan area)                                   |
| 55             | Date of Last Change          | Date of the last numeric update in AQS                                            |



2. Asthma Data
Asthma data was acquired from the CDC (Center for Disease Control). For our analysis, we focused on columns starting with CASTHMA_, which indicate the frequency of asthma in U.S. counties. We queried data for 2020, based on research suggesting that the negative effects of poor air quality on asthma prevalence may take 12–24 months to come into effect.

Schema:

| Column Name       | Description                                                                      | Standardized Name | Type   |
| ----------------- | -------------------------------------------------------------------------------- | ----------------- | ------ |
| StateAbbr         | State abbreviation                                                               | stateabbr         | Text   |
| StateDesc         | State name                                                                       | statedesc         | Text   |
| CountyName        | County name                                                                      | countyname        | Text   |
| CountyFIPS        | County FIPS code                                                                 | countyfips        | Text   |
| TotalPopulation   | 2018 population estimate                                                         | totalpopulation   | Number |
| CASTHMA_CrudePrev | Model-based estimate of crude prevalence of current asthma among adults aged ≥18 | casthma_crudeprev | Number |
| CASTHMA_Crude95CI | Estimated confidence interval for crude prevalence                               | casthma_crude95ci | Text   |
| CASTHMA_AdjPrev   | Model-based estimate of age-adjusted prevalence of asthma                        | casthma_adjprev   | Number |
| CASTHMA_Adj95CI   | Estimated confidence interval for age-adjusted prevalence                        | casthma_adj95ci   | Text   |





The data can be accessed and assessed using the following URL’s
Asthma data: https://data.cdc.gov/500-Cities-Places/PLACES-County-Data-GIS-Friendly-Format-2020-releas/mssc-ksj7/about_data
Air Quality Data: https://aqs.epa.gov/aqsweb/airdata/download_files.html


**Data Integrity Verification**

This script inspects the integrity of the data we download by generating SHA-256 checksums for the raw data retrieved in the acquisition phase. This allows for other uses to check integrity and ensure that the original files have not been altered.

The compute function finds the raw data according to a specified file path. After this is done, the function returns a SHA256 hexadecimal string and saves this as a JSON. The JSON’s are saved in a ‘checksums’ folder located within the data branch. As long as the correct file paths are specified to find the raw data, this script will run and save to the correct location.
