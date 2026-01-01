import streamlit as st
import pandas as pd
import plotly.express as px
from db.connection import get_engine
from utils.plotly_config import apply_plotly_theme

# Apply global Plotly theme
apply_plotly_theme()

engine = get_engine()

st.set_page_config(
    page_title="Nutrition Paradox Dashboard",
    layout="wide"
)

# -----------------------------
# TITLE & DESCRIPTION
# -----------------------------
st.title("⚖️ Nutrition Paradox Dashboard")
st.markdown("""
A SQL-powered analytics dashboard that explores **global obesity and malnutrition trends**
across countries, age groups, genders, and regions using WHO datasets.
""")

st.divider()

# -----------------------------
# KPI METRICS
# -----------------------------
kpi_df = pd.read_sql("""
SELECT 
    AVG(o.Mean_Estimate) AS avg_obesity,
    AVG(m.Mean_Estimate) AS avg_malnutrition,
    COUNT(DISTINCT o.Country) AS countries
FROM obesity_data o
JOIN malnutrition_data m 
    ON o.Country = m.Country;
""", engine)

c1, c2, c3 = st.columns(3)

c1.metric("🌍 Countries Covered", int(kpi_df["countries"][0]))
c2.metric("🧋 Avg Obesity (%)", round(kpi_df["avg_obesity"][0], 2))
c3.metric("🍽️ Avg Malnutrition (%)", round(kpi_df["avg_malnutrition"][0], 2))

st.divider()

# -----------------------------
# LINE PLOT: OBESITY vs MALNUTRITION OVER YEARS
# -----------------------------
st.subheader("📈 Global Obesity vs Malnutrition Trend Over Years")

trend_df = pd.read_sql("""
SELECT 
    o.Year,
    AVG(o.Mean_Estimate) AS obesity,
    AVG(m.Mean_Estimate) AS malnutrition
FROM obesity_data o
JOIN malnutrition_data m
    ON o.Year = m.Year
GROUP BY o.Year
ORDER BY o.Year;
""", engine)

fig = px.line(
    trend_df,
    x="Year",
    y=["obesity", "malnutrition"],
    markers=True,
    title="Global Trend: Obesity vs Malnutrition"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Percentage (%)",
    legend_title="Metric",
    height=450
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "💡 Insight: While global obesity shows a steady increase over time, "
    "malnutrition declines more slowly, highlighting the global nutrition paradox."
)
