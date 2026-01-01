# Nutrition Paradox – Streamlit Dashboard

This Streamlit application visualizes global **obesity and malnutrition data**
using SQL queries and interactive charts. The dashboard allows users to explore
trends, comparisons, and demographic insights in a clean and user-friendly way.

---

## Features

- SQL-connected Streamlit dashboard
- Analysis of obesity and malnutrition trends
- Searchable query selector for each analysis section
- One visualization and one table per query
- Clean dark-themed UI with interactive Plotly charts

---

## App Structure

Nutrition_Paradox_App/
├── app.py
├── requirements.txt
├── .streamlit/
│ └── config.toml
├── db/
│ └── connection.py
├── queries/
│ ├── obesity_queries.py
│ ├── malnutrition_queries.py
│ └── combined_queries.py
├── pages/
│ ├── 1_Project_Overview.py
│ ├── 2_Obesity.py
│ ├── 3_Malnutrition.py
│ ├── 4_Combined.py
│ └── 5_Insights.py
└── utils/
└── plotly_config.py
---

## How to Run the App

1. Install dependencies:
```bash
pip install -r requirements.txt

Configure database connection:

Update credentials in db/connection.py

Run the app:

streamlit run app.py

Data

Source: World Health Organization (WHO)

Time period: 2012–2022

Metrics: Mean Estimate, CI Width, Region, Country, Age Group, Gender


---

Author
Abishek Murugan
