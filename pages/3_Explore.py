import streamlit as st
import altair as alt
from utils.io import load_data
from charts.charts import base_theme, chart_interactive_explorer

st.set_page_config(page_title="Explore", layout="wide")

alt.themes.register("project", base_theme)
alt.themes.enable("project")

df = load_data()

st.title("Explore: Audio Features, Genres, and Time")
st.write(
    "With this interactive, user-driven visualization, users can explore how different audio features affect popularity "
    "for different genres, over time. The top line chart shows the average use of the feature by year and the bottom scatterplot "
    "shows the relationship between feature value and popularity (filtered by genre, feature, and time period)."
)

st.markdown(
    "**How to interact:**\n"
    "- Use the **Genre** dropdown to filter to a specific genre or view all.\n"
    "- Use the **Feature** dropdown to select which audio feature to explore.\n"
    "- **Brush** a time period on the top line chart to filter the scatter below.\n"
    "- A red regression line appears for the brushed selection."
)

st.altair_chart(chart_interactive_explorer(df), use_container_width=True)
st.caption(
    "Figure 4: Interactive explorer showing average feature trends by year (top) and feature vs. popularity scatter (bottom)."
)

st.markdown("**Guided Prompts:**")
st.markdown(
    "- Filter to one audio feature ('loudness', 'danceability', etc.) -- how does this feature relate to popularity?\n"
    "- Filter to different genres ('pop', 'rock') -- how do certain audio features affect certain genres? What are the differences and similarities between the relationships?\n"
    "- Brush a specific time period -- how do trends change for different time periods?"
)

st.divider()
st.subheader("Feature-by-Feature Insights")

st.markdown("**Loudness:** When looking at loudness across genres, the relationship with popularity appears relatively weak overall. "
    "However, hip hop and rock show slightly positive trends, suggesting that louder tracks in these genres tend to perform better. "
    "Genres such as pop, R&B, and dance/electronic appear to have little or no relationship between loudness and popularity.")

st.markdown("**Danceability:** The relationship between danceability and popularity varies across genres. "
    "Hip hop is the only genre that appears to have a positive relationship, while pop has no relationship, "
    "and the rest (dance/electronic, R&B, and rock) have negative correlations with popularity.")

st.markdown("**Energy:** Across most genres, energy shows a slight positive correlation, suggesting that more energetic songs "
    "tend to have slightly higher popularity scores. Dance/electronic and pop are the only genres with no or negative correlations.")

st.markdown("**Speechiness:** Speechiness appears to have little to no correlation with most genres, "
    "with the only positive correlation in R&B. This suggests that speechiness does not have a strong influence on popularity.")

st.markdown("**Acousticness:** Acousticness appears to have little to no correlation with most genres, "
    "with the only negative correlation in rock. This suggests that acousticness does not strongly correlate with popularity.")

st.markdown("**Instrumentalness:** Instrumentalness appears to have little to no correlation with most genres, "
    "with the only negative correlation appearing in rock. This suggests that instrumentalness does not strongly influence popularity.")

st.markdown("**Liveliness:** Across all genres, liveliness appears to have little to no correlation, "
    "suggesting it does not strongly correlate with popularity.")

st.markdown("**Valence:** Valence appears to have little to no relationship with most genres besides a negative correlation in R&B. "
    "This is interesting because in R&B, this means that songs that sound less positive (lower valence) tend to have slightly higher popularity.")

st.markdown("**Tempo:** Tempo has little to no correlation with popularity across all genres.")
