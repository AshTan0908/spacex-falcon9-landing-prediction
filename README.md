# SpaceX Falcon 9 First Stage Landing Prediction

Predicting whether the Falcon 9 first stage will land successfully, using public SpaceX launch data. If landing outcome can be predicted, launch cost can be estimated — SpaceX reuses the first stage, which is the main reason it can offer launches at a fraction of the cost of competitors.

## Overview

This project walks through a full data science pipeline: collecting and cleaning launch data, exploring it for patterns, visualizing relationships between flight number, payload mass, orbit, and landing outcome, mapping launch site geography, and finally training classification models (logistic regression, SVM, decision tree, KNN) to predict landing success.

## Repository Structure

| Notebook | Description |
|---|---|
| `01_data_collection_api.ipynb` | Pulls launch records via the SpaceX REST API and IBM's static snapshot dataset; cleans and exports `dataset_part_1.csv` |
| `02_webscraping.ipynb` | Scrapes historical Falcon 9/Heavy launch records from a pinned Wikipedia snapshot using BeautifulSoup |
| `03_data_wrangling.ipynb` | Exploratory data analysis; engineers the binary landing-outcome `Class` label |
| `04_eda_sql.ipynb` | SQL queries (SQLite) answering specific questions about launch sites, payload mass, and mission outcomes |
| `05_eda_dataviz.ipynb` | Visual EDA with `matplotlib`/`seaborn`; feature engineering and one-hot encoding for modeling |
| `06_launch_site_location.ipynb` | Interactive Folium map of launch sites, proximity to coastlines/highways, and outcome markers |
| `07_dashboard_app.py` | Interactive Plotly Dash dashboard for exploring launch outcomes by site and payload range |
| `08_predictive_analysis.ipynb` | Trains and tunes logistic regression, SVM, decision tree, and KNN classifiers; compares test accuracy |

## Data Sources

- SpaceX launch data via the community-maintained SpaceX REST API and a static JSON/CSV snapshot (IBM-hosted, for reproducibility)
- Historical launch records scraped from a pinned revision of [List of Falcon 9 and Falcon Heavy launches](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches) (Wikipedia)

**Note:** The original SpaceX REST API (`api.spacexdata.com`) was archived in June 2026 and its endpoints no longer resolve. `01_data_collection_api.ipynb` documents this (including the resulting SSL/connection errors) and falls back to IBM's canonical pre-collected dataset so the rest of the pipeline runs on consistent, real data.

## Tools & Libraries

Python, Pandas, NumPy, Matplotlib, Seaborn, SQLite (`ipython-sql`), Folium, Plotly Dash, scikit-learn

## Key Findings

*Will fill once all insights are collated post-presentation.*

## How to Run

Each notebook is self-contained and pulls data from the URLs referenced above. Install dependencies with:

```cmd prompt 
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 folium dash scikit-learn ipython-sql
```

Then open the notebooks in Jupyter in numerical order.

## Acknowledgments

Built as the capstone project for IBM's Applied Data Science Capstone course on Coursera.

## Author

Aashutosh Tandon
