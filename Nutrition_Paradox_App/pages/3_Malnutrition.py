import streamlit as st
import pandas as pd
import plotly.express as px
from db.connection import get_engine
import queries.malnutrition_queries as q
from utils.plotly_config import apply_plotly_theme

apply_plotly_theme()
engine = get_engine()

st.header("🍽️ Malnutrition Analysis")

options = {
    # ---------- DEMOGRAPHICS ----------
    "Average Malnutrition by Age Group": (
        q.AVG_BY_AGE,
        lambda df: px.bar(
            df, x="Age_Group", y="avg_malnutrition",
            title="Average Malnutrition by Age Group"
        )
    ),

    "Average Malnutrition by Gender": (
        q.AVG_BY_GENDER,
        lambda df: px.bar(
            df, x="Gender", y="avg_malnutrition",
            title="Average Malnutrition by Gender"
        )
    ),

    # ---------- RANKINGS ----------
    "Top 5 Countries by Malnutrition": (
        q.TOP_COUNTRIES,
        lambda df: px.bar(
            df, x="Country", y="avg_malnutrition",
            title="Top 5 Countries by Malnutrition"
        )
    ),

    "Regions with Lowest Malnutrition": (
        """
        SELECT Region, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition_data
        GROUP BY Region
        ORDER BY avg_malnutrition ASC
        LIMIT 5;
        """,
        lambda df: px.bar(
            df, x="Region", y="avg_malnutrition",
            title="Regions with Lowest Average Malnutrition"
        )
    ),

    # ---------- TRENDS ----------
    "Malnutrition Trend in Africa": (
        q.AFRICA_TREND,
        lambda df: px.line(
            df, x="Year", y="avg_malnutrition",
            markers=True,
            title="Malnutrition Trend in Africa"
        )
    ),

    "Yearly Malnutrition Change (India, Nigeria, Brazil)": (
        """
        SELECT Year, Country, AVG(Mean_Estimate) AS avg_malnutrition
        FROM malnutrition_data
        WHERE Country IN ('India','Nigeria','Brazil')
        GROUP BY Year, Country
        ORDER BY Year;
        """,
        lambda df: px.line(
            df, x="Year", y="avg_malnutrition",
            color="Country",
            markers=True,
            title="Yearly Malnutrition Change (Selected Countries)"
        )
    ),

    # ---------- DATA QUALITY ----------
    "Malnutrition Level vs CI Width": (
        q.LEVEL_CI,
        lambda df: px.box(
            df, x="Malnutrition_Level", y="avg_ci",
            title="CI Width by Malnutrition Level"
        )
    ),

    "High CI Width Flags (>5)": (
        q.HIGH_CI,
        lambda df: px.bar(
            df, x="Country", y="CI_Width",
            title="High CI Width Flags (Low Reliability)"
        )
    ),

    # ---------- CHANGE ANALYSIS ----------
    "Countries with Increasing Malnutrition": (
        q.INCREASING,
        lambda df: px.bar(
            df, x="Country", y="change",
            title="Countries with Increasing Malnutrition"
        )
    ),

    "Min vs Max Malnutrition per Year": (
        q.MIN_MAX_YEAR,
        lambda df: px.line(
            df, x="Year",
            y=["min_malnutrition", "max_malnutrition"],
            markers=True,
            title="Min vs Max Malnutrition Levels per Year"
        )
    ),
}

question = st.selectbox(
    "🔍 Search and select a malnutrition analysis question",
    list(options.keys())
)

sql, chart_fn = options[question]
df = pd.read_sql(sql, engine)

fig = chart_fn(df)
fig.update_layout(height=450)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📋 Query Output")
st.dataframe(df, use_container_width=True, height=320)
