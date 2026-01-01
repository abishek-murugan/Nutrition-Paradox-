import streamlit as st
import pandas as pd
import plotly.express as px
from db.connection import get_engine
import queries.obesity_queries as q
from utils.plotly_config import apply_plotly_theme

apply_plotly_theme()
engine = get_engine()

st.header("🧋 Obesity Analysis")

options = {
    # ---------- RANKINGS ----------
    "Top 5 Regions by Obesity (2022)": (
        q.TOP_REGIONS_2022,
        lambda df: px.bar(df, x="Region", y="avg_obesity")
    ),

    "Top 5 Countries by Obesity": (
        q.TOP_COUNTRIES,
        lambda df: px.bar(df, x="Country", y="avg_obesity")
    ),

    # ---------- TRENDS ----------
    "Obesity Trend in India": (
        q.INDIA_TREND,
        lambda df: px.line(df, x="Year", y="obesity_rate", markers=True)
    ),

    "Global Obesity Trend": (
        q.GLOBAL_TREND,
        lambda df: px.line(df, x="Year", y="global_avg", markers=True)
    ),

    # ---------- DEMOGRAPHICS ----------
    "Average Obesity by Gender": (
        q.AVG_BY_GENDER,
        lambda df: px.bar(df, x="Gender", y="avg_obesity")
    ),

    "Average Obesity by Age Group": (
        q.AVG_BY_AGE,
        lambda df: px.box(df, x="Age_Group", y="avg_obesity")
    ),

    # ---------- DISTRIBUTION ----------
    "Obesity Level Distribution": (
        """
        SELECT Obesity_Level, COUNT(DISTINCT Country) AS count
        FROM obesity_data
        GROUP BY Obesity_Level;
        """,
        lambda df: px.pie(df, names="Obesity_Level", values="count", hole=0.4)
    ),

    # ---------- DATA QUALITY ----------
    "Least Reliable Countries (High CI Width)": (
        q.LEAST_RELIABLE,
        lambda df: px.bar(df, x="Country", y="avg_ci")
    ),

    "Most Consistent Countries (Low CI Width)": (
        q.MOST_RELIABLE,
        lambda df: px.bar(df, x="Country", y="avg_ci")
    ),

    # ---------- GENDER GAP ----------
    "Female vs Male Obesity Gap": (
        q.FEMALE_GT_MALE,
        lambda df: px.bar(df, x="Country", y="gender_gap")
    ),
}

question = st.selectbox(
    "🔍 Search and select an obesity analysis question",
    options=list(options.keys())
)

sql, chart_fn = options[question]
df = pd.read_sql(sql, engine)

fig = chart_fn(df)
fig.update_layout(height=450)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📋 Query Output")
st.dataframe(df, use_container_width=True, height=320)
