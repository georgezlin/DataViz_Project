import streamlit as st
import altair as alt
from utils.io import load_data
from charts.charts import base_theme, chart_duration_by_genre, chart_rnb_vs_all

st.set_page_config(page_title="Genre Deep Dive", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

df = load_data()

st.title("Genre Deep Dive")
st.header("Does the relationship between song length and popularity look different across genres?")
st.write(
    "Since duration has the strongest correlation with popularity, we investigate whether this holds across all genres."
)

st.altair_chart(chart_duration_by_genre(df), use_container_width=True)
st.caption(
    "Figure 2: Duration vs. popularity by genre, with regression trend lines for each genre."
)

st.write(
    "Most of the songs in this dataset fall between 3-4 minutes, suggesting a common length for popular tracks across all genres. "
    "There's a positive correlation between duration and popularity for most genres (Dance/Electronic, hip hop, pop, and rock). "
    "This suggests that longer songs in these genres tend to be slightly more popular, on average. "
    "The scatterplot shows a wide variation of popularity at similar durations, indicating that song length alone does not strongly determine popularity. "
    "However, one genre sticks out as an exception: R&B has a negative relationship between duration and popularity. "
    "Within R&B, shorter songs actually perform stronger than longer ones. "
    "This contrast suggests that different genres have different characteristics that make songs popular. "
    "With this unusual pattern in R&B, it's worth taking a closer look at R&B specifically to understand what features do drive popularity in this genre."
)

st.divider()
st.header("What predicts popularity in R&B compared to other genres?")

st.altair_chart(chart_rnb_vs_all(df), use_container_width=True)
st.caption(
    "Figure 3: Correlation of audio features with popularity for R&B tracks vs. all tracks."
)

st.write(
    "For R&B, there's a stronger positive correlation between popularity and loudness, tempo, speechiness, and acousticness. "
    "For songs of other genres, there is a negative correlation between popularity and features like danceability, liveness, energy, and instrumentalness. "
    "For R&B, these features actually positively correlate with popularity, with especially notable differences for energy and instrumentalness. "
    "Valence is much more negatively correlated with popularity for R&B songs compared to other genres. "
    "As previously discussed, duration correlates negatively with popularity for R&B songs, but not for songs of other genres. "
    "Audio features that predict popularity for R&B songs seem to differ significantly from trends of popularity with all songs."
)

st.divider()
st.write("Next, explore how different audio features correlate with popularity over time for different genres using the interactive dashboard.")
