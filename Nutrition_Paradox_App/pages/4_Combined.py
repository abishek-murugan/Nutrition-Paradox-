import streamlit as st
import pandas as pd
import plotly.express as px
from db.connection import get_engine
import queries.combined_queries as q
from utils.plotly_config import apply_plotly_theme

apply_plotly_theme()
engine = get_engine()

st.header("🔗 Combined Obesity & Malnutrition Analysis")

options = {
    # ---------- RELATIONSHIP ----------
    "Obesity vs Malnutrition (5 Countries)": (
        q.COUNTRY_COMPARE,
        lambda df: px.scatter(
            df,
            x="obesity",
            y="malnutrition",
            color="Country",
            trendline="ols",
            title="Obesity vs Malnutrition Relationship"
        )
    ),

    # ---------- GENDER ----------
    "Gender-based Disparity (Obesity vs Malnutrition)": (
        q.GENDER_COMPARE,
        lambda df: px.bar(
            df,
            x="Gender",
            y="obesity",
            title="Gender-based Obesity vs Malnutrition"
        )
    ),

    # ---------- REGION ----------
    "Region-wise Comparison (Africa vs Americas)": (
        q.REGION_COMPARE,
        lambda df: px.bar(
            df,
            x="Region",
            y="obesity",
            title="Regional Comparison: Obesity (Africa vs Americas)"
        )
    ),

    # ---------- DIRECTIONAL CHANGE ----------
    "Countries with Obesity ↑ and Malnutrition ↓": (
        q.OB_UP_MAL_DOWN,
        lambda df: px.bar(
            df,
            x="Country",
            y="obesity_change",
            title="Countries with Obesity Increase & Malnutrition Decrease"
        )
    ),

    # ---------- AGE ----------
    "Age-wise Obesity vs Malnutrition Trend": (
        q.AGE_TREND,
        lambda df: px.line(
            df,
            x="Year",
            y=["obesity", "malnutrition"],
            markers=True,
            title="Age-wise Obesity vs Malnutrition Trend"
        )
    ),
}

question = st.selectbox(
    "🔍 Search and select a combined analysis question",
    list(options.keys())
)

sql, chart_fn = options[question]
df = pd.read_sql(sql, engine)

fig = chart_fn(df)
fig.update_layout(height=450)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📋 Query Output")
st.dataframe(df, use_container_width=True, height=320)
