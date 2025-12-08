**Final Project: Air Quality and its Effects on Asthma**
--
Contributors:
  Sam Birdsley
  Michael Strobl
--

This repository explores the links between asthma and poor air quality over time. Our data workflow allows us to acquire, process, save, and document all data necessary to reproduce the results.

**Reproducibility**

To achieve the results we have obtained, all you have to do is go to the 'Actions' tab of our repository, and then run the master workflow. This can be done manually and will trigger our workflow automation python script. This will run all of our python scripts in the correct manner. From here, you must download the artificat from the workflow where you can view the results, as well as all the version of our data. We chose to do this as it was considered best practice for a GitHub workflow. If there are any questions on how to achieve these results, please reach out.

If you choose to run the results in your own envionrment based on the scripts we have provided, you will need the following libraries: Subprocess, os, sys, pandas, requests, numpy, seaborn, zipfile, io, StringIO, hashlib, json, re, sqlite3, and matplotlib.

Additionally, our raw, processed, and joined data can also be viewed here along with the final results: https://uofi.app.box.com/folder/354716358671. All course staff should have access, but if this is an issue please reach out to samuel36@illinois.edu or mstrobl3@illinois.edu.

**Summary**

The goal of our project was to investigate the statistical correlation between poor air quality and asthma rates in the same counties. Within our automated workflow, we have multiple Python scripts that retrieve the data, ensure its integrity, profile it, clean it, integrate it, store it, and analyze it. We retrieved open-source data from two different United States government agencies. We determined that the best course of action was to offset the asthma data by 2 years so that we can measure the direct effects of the air quality data as well. The data was retrieved directly via a request command, and the links to the data are included in the code and in this documentation. It is important to note that both datasets contained different counties, so we were unable to use either dataset in its entirety. Certain states were included in one dataset but not the other, resulting in a relatively low number of matches compared to either full dataset. We decided to look into this topic because we both know people with asthma and were interested in the statistical correlation between the two factors. We want to understand the mechanisms that lead to health disparities and how specific groups are affected by them.

Furthermore, when it was time to do the analysis, something we realized was that most counties have excellent air quality. Poor air quality is often found in large cities and occurs only a few days out of the year. A good example of this is Chicago, which had a few days of poor air quality due to wildfires last summer, but is usually positive overall. This made the analysis difficult because many of these cities attract affluent people who move there later in life, after they have passed the developmental stage when most people get asthma. Furthermore, in rural counties that have high levels of asthma, there are other factors affecting these people. As we will mention later, a good next step could be adding a third data source that has income level as well. This way, we can explore another factor that may help explain our asthma levels.

The final output of this project is an artifact that can be downloaded from the automated workflow that the user can trigger. Once the workflow has run all the scripts, the results and different stages of data can be viewed. We considered pushing the results back to the repository, but this was deemed a bad practice when the workflow involves the user retrieving raw data.

**Data Acquisition Documentation**

1. Air Quality Data - EPA Air Quality System (2018)
We obtained annual county-level air quality data from the EPA’s Air Quality System (AQS). This dataset contains detailed measurements from monitoring sites in specific counties (note: not all U.S. counties are included). The year of the data that we chose was 2018. This is due to the fact that the asthma data was from 2020, and we wanted to ensure a gap in the data to measure cause and effect. We chose a two year gap is this was cited by researchers as an appropriate time window.

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



2. Asthma Data - CDC PLACES (2020)
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

**Data Profiling** 
When we started the project, data profiling was one of the most important steps because it told us exactly what we were working with before we jumped into cleaning or analysis. At first we thought both datasets would line up pretty naturally since they were both county level information, but profiling showed that this was not really the case. The EPA air quality dataset does not include every county in the United States. It only includes counties that actually have monitoring equipment, which is way fewer than the total amount of counties. Once we saw this, we knew ahead of time that our final merged dataset would only include around three hundred counties. Instead of trying to fix this or fill in fake values, we made the decision that it was better to accept this number and work honestly with the data we really had. Profiling helped us understand that this smaller sample size was expected and totally normal for EPA data. The profiling report we created showed the number of rows, columns, missing values and duplicate rows in each dataset. This helped us see where the trouble spots were. For example, the air quality dataset had county names written in different formats. Some included words like County or Parish and others did not. Some had extra spaces at the end or beginning. The state names also had mixed capitalization. These problems would have made merging impossible if we ignored them. Profiling made these issues obvious so we could fix them later in cleaning. We also saw the numeric columns for Good Days, Moderate Days and the unhealthy categories and made sure they were realistic. A surprising thing we noticed was that the total Days with AQI did not always match the sum of all the categories. This meant the dataset had some inconsistencies that we needed to handle. Without profiling we probably would not have noticed this until way later. Profiling the asthma dataset also showed a lot of details that changed our cleaning decisions. The asthma data had confidence intervals stored as text which meant they could not be used in any numeric work until we parsed them. The dataset also had a weird field for geolocation where the latitude and longitude were hidden inside a string. We had to decide what to do with them and profiling helped us see that we could extract these numbers with regular expressions. The FIPS codes also came in different formats, sometimes with missing zeros. If we did not catch this early then none of the counties would match later during the join. Another important thing we noticed from profiling was how the actual values were shaped. The distributions for air quality values showed that most counties had mostly good air and only a few had large numbers of unhealthy or very unhealthy days. This matched real world patterns because most places in the United States do not have extremely bad pollution except during special events like wildfires. We knew this would probably lower the strength of correlations later on, since correlation needs variation in both variables to show a strong relationship. Profiling helped us understand that the dataset itself naturally leaned toward clean air and average asthma numbers for most counties. So we set our expectations realistically. Profiling did not just show problems. It helped us make smart decisions about what was worth fixing and what we should just accept. For example, instead of trying to force more counties into the final merged dataset, we accepted that only about 327 counties had both types of data. This decision kept the project honest and avoided false signals. Profiling also helped us think ahead about how the analysis might turn out. We saw that both variables do not vary extremely across most counties which explains why later correlations came out weak. The profiling step basically gave us the map for the entire workflow. It showed what issues existed, what to expect later on, and what choices we needed to make to keep our work believable and reproducible. By the end, profiling was not just a checkup step. It was a key part of shaping the project and making sure the rest of the workflow was built on solid understanding instead of guessing.

**Data Cleaning** 
For cleaning we took all the issues from profiling and fixed them one by one. We cleaned county and state names by stripping spaces and making them match across both datasets. We also removed things like County and Parish from the names so merging would be more accurate. This was important since the join depends on matching text exactly and even a small space can break everything. We converted numeric fields to real numbers and forced impossible values like negative asthma prevalence or values over one hundred to become missing instead. This made the dataset more believable and prevented weird spikes in analysis. For the EPA dataset we fixed the mismatches between category days and total Days with AQI by adjusting Moderate Days which was the safest category to change. Wild Max AQI values over five hundred were clipped since that number is the absolute upper limit. In the asthma dataset we had to parse confidence intervals from strings into numeric low and high values. We also extracted latitude and longitude from the geolocation field so it could be used later if needed. The CDC data had the county FIPS stored different ways so we changed them to always be five digits. Most of the cleaning decisions came from real problems we found so nothing was random. We chose conservative edits to keep the analysis legitimate rather than making crazy assumptions that would change the results.

**Database Connection**
Once both datasets were cleaned we saved them into a SQLite database. This made the workflow easier to repeat because anyone can rebuild the same database just by running the scripts again. SQLite was a good choice since it does not need any kind of server and it works pretty much anywhere. We stored the air quality table and the asthma table exactly the way they looked after cleaning, so we always have a stable version of both datasets saved in one place. This also kept everything more organized and made it simpler to load the data for merging and analysis later on.

**Data Integration**

Merged asthma and air qaulity data at the county level. Prepared merged dataset for analysis.

**Analysis**

Generate descriptive statistics, visualizations, and correlations.

**Work Cited**

GitHub Documentation. (2024). About workflow artifacts. GitHub Docs. https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts
American Lung Association. (2025, May 9). 

Understanding the strong link between air pollution and asthma. American Lung Association. https://www.lung.org/blog/asthma-and-air-pollution
