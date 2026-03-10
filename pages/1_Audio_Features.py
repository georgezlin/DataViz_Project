import streamlit as st
import altair as alt
from utils.io import load_data
from charts.charts import base_theme, chart_feature_correlation

st.set_page_config(page_title="Audio Features & Popularity", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

df = load_data()

st.title("Audio Features & Popularity")
st.header("How do different metrics define popularity over time?")
st.write(
    "Let's break down our big question and start small: ")
st.write("Which audio features of a song correlate most strongly with popularity?")

st.altair_chart(chart_feature_correlation(df), use_container_width=True)
st.caption(
    "Figure 1: Correlation of each audio feature with popularity across all 2,000 tracks."
)

st.write(
    "Duration seems to have the largest positive correlation, suggesting that longer songs tend to be more popular, on average. "
    "Loudness and acousticness also show small positive relationships with popularity, while instrumentalness has the largest negative correlation, "
    "suggesting that songs with more instrumental content tend to be less popular on average. Most of these correlations are relatively weak overall, "
    "suggesting that no single feature determines a song's popularity, but a combination of these characteristics is what makes a song popular."
)

st.divider()
st.write("Next, since duration has the strongest correlation with popularity, explore how this relationship differs across genres.")
