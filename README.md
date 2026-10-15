# CLIMAGUARD AI
### An Adaptive Climate Risk Intelligence and Decision Support System

**Project Status:** In Development  
**Project Type:** AI / Machine Learning / Climate Intelligence  
**Geographic Focus:** Sri Lanka

## 1. Project Overview

CLIMAGUARD AI is an AI-powered climate intelligence project designed to analyze historical rainfall patterns in Sri Lanka and support the identification of potentially hazardous rainfall conditions.

The system aims to transform historical climate data into useful information that can help identify extreme rainfall patterns and support climate-risk assessment. The long-term goal is to develop a system that can assist with disaster preparedness and climate-related decision-making.

The project is currently in the data collection and preprocessing stage. The final prediction capabilities will depend on the availability and quality of suitable historical event data.

## 2. Main Objectives

- Collect historical daily rainfall data covering Sri Lanka.
- Process geographical rainfall data into structured datasets.
- Analyze rainfall patterns and identify extreme rainfall conditions.
- Engineer useful features from historical rainfall observations.
- Investigate reliable flood and other hazard-event records.
- Develop and evaluate suitable machine learning models.
- Build a dashboard to visualize rainfall patterns and model results.
- Explore risk indicators that can support climate-risk awareness.

## 3. Data Source

The project currently uses **CHIRPS daily precipitation data**, obtained from the Climate Hazards Center.

**Dataset source:** [CHIRPS Daily Rainfall Data](https://data.chc.ucsb.edu/products/CHIRPS/v3.0/daily/final/rnl/)

The dataset provides gridded daily rainfall estimates. Each grid cell represents an estimated rainfall value for a geographic location.

The initial historical collection period is:

- Start date: January 1, 2020
- End date: December 31, 2024
- Geographic area: Sri Lanka

The five-year period contains 1,827 calendar days, including leap years 2020 and 2024.

## 4. Technologies Used

- **Python** — primary programming language
- **Pandas and NumPy** — data processing and numerical operations
- **GeoPandas** — geographical boundary handling
- **Rasterio** — processing rainfall GeoTIFF files
- **Natural Earth** — Sri Lanka country boundary data
- **CHIRPS** — historical rainfall data source
- **Machine Learning** — planned for rainfall-risk analysis and prediction
- **Data Visualization and Dashboard** — planned for presenting results

## 5. How the System Works

1. **Data acquisition:** Python downloads daily rainfall GeoTIFF files from the CHIRPS data server.
2. **Geographic filtering:** Rasterio uses the Sri Lanka boundary polygon to extract relevant grid cells.
3. **Data cleaning:** Missing-data markers and invalid rainfall values are removed.
4. **CSV generation:** Each day's valid rainfall observations are saved in a separate CSV file.
5. **Dataset integration:** Validated daily CSV files are combined into a historical dataset.
6. **Feature engineering:** Historical rainfall observations will be transformed into features such as rolling rainfall totals and rainfall intensity indicators.
7. **Model development:** Suitable machine learning models will be selected, trained and evaluated.
8. **Visualization:** A dashboard will present rainfall patterns, analytical results and supported risk indicators.

## 6. Project Structure

```text
CLIMAGUARD-AI/
├── data/
│   ├── raw/
│   │   └── boundaries/
│   └── processed/
│       ├── daily_rainfall/
│       └── historical_rainfall.csv
├── src/
│   └── data/
│       ├── mask_sri_lanka.py
│       ├── process_rainfall_series.py
│       └── download_historical_rainfall.py
├── .venv/
└── README.md
```

*The structure shows the main files and folders currently used in the data pipeline. Additional folders and modules will be added as development progresses.*

## 7. Current Progress

### Completed

- Set up the Python development environment.
- Downloaded and prepared the Sri Lanka country boundary.
- Successfully opened and processed CHIRPS rainfall GeoTIFF files.
- Extracted valid rainfall pixels within Sri Lanka.
- Created a CSV containing rainfall observations for January 1–7, 2024.
- Built an automated daily rainfall downloader.
- Added daily CSV validation and a combined dataset generation process.
- Tested the downloader with January 1–3, 2024, producing 6,519 pixel-day records.

### In Progress

- Collecting historical rainfall data for 2020–2024.
- Handling network timeouts and restarting interrupted downloads.
- Validating the completeness and consistency of the historical dataset.

### Planned

- Exploratory data analysis and rainfall visualization.
- Rainfall feature engineering.
- Collection and verification of historical flood or hazard-event records.
- Machine learning model development and evaluation.
- Risk visualization dashboard.
- Documentation, testing and final project evaluation.

## 8. Important Limitations

Rainfall measurements alone cannot confirm that a flood occurred. Flood prediction requires appropriate event labels or other credible evidence, and potentially additional information such as river levels, terrain, drainage and land characteristics.

If reliable flood-event data cannot be obtained, the initial model will focus on extreme rainfall analysis and rainfall-risk indicators rather than claiming verified flood prediction.

Model performance will be evaluated using suitable metrics and data splits that avoid misleading results from spatial or temporal leakage.

## 9. Final Goal

The final goal is to develop a working climate intelligence prototype that combines historical rainfall analysis, machine learning and interactive visualization to help users understand rainfall patterns and assess potentially hazardous conditions.

CLIMAGUARD AI is currently a work in progress. Its final capabilities will be determined by data availability, model validation and the results of development and testing.

---

**Project:** CLIMAGUARD AI  
**Focus:** Climate Intelligence and Rainfall-Risk Analysis  
**Status:** Data Pipeline Development
