# Nutrition Paradox Project

This repository contains an end-to-end data analysis project on **global obesity
and malnutrition** using WHO data.

The project includes:
- Exploratory Data Analysis (EDA) using Python
- SQL-based analytical queries
- An interactive Streamlit dashboard for visualization

---

## Repository Contents

- `Pre_Analysis.ipynb`  
  Data cleaning, preprocessing, statistical analysis, and exploratory
  visualizations.

- `Nutrition_Paradox_App/`  
  Streamlit application that connects to a SQL database and visualizes obesity
  and malnutrition insights.

---

## Tools & Technologies

- Python
- SQL (MySQL / TiDB)
- Pandas
- Plotly
- Streamlit
- SQLAlchemy

---

## How to Run the Dashboard

```bash
pip install -r Nutrition_Paradox_App/requirements.txt
cd Nutrition_Paradox_App
streamlit run app.py
