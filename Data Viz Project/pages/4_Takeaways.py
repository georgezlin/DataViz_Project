import streamlit as st

st.set_page_config(page_title="Takeaways", layout="wide")

st.title("Takeaways")

st.header("Conclusion")
st.write(
    "Popularity isn't defined by a single metric. Rather, different metrics predict success for different genres over time. "
    "Therefore, the relationship between audio features and popularity is context-dependent. Both genre and time period shape which metrics matter. "
    "Different genres prioritize different musical qualities, and some features only matter with specific genres. For example, danceability has a "
    "positive relationship with popularity for hip-hop, but a negative relationship with dance/electronic, rock, and R&B. Most audio features show "
    "weak correlations with popularity overall, suggesting that audio characteristics alone cannot explain popularity. Other factors likely influence "
    "success, such as artist reputation, marketing, cultural trends, and more."
)
st.write(
    "Additionally, some metrics predict success differently across time periods. For example, there's a negative relationship between energy and "
    "popularity for all genres from 1998-2007 and a positive one from 2007-2020. This suggests that listener preferences evolve over time. Things "
    "like technological shifts, such as the streaming era and new production techniques, may influence what kinds of songs succeed. Different metrics "
    "define music popularity in varying ways (whether positively, negatively, or not at all) across genres and across time."
)
st.write(
    "Popularity is a reflection of social and cultural dynamics, not just sound. Audio features capture musical structure, but popularity is heavily "
    "dependent on external factors. This dataset captures many successful songs, and the overlap and differences that make them successful. Popular "
    "music success is layered and constantly evolving, and understanding popularity requires musical characteristics, such as audio features, and "
    "broader cultural context."
)

st.header("Data Source")
st.write("Dataset: https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019")

st.header("Key Variables")
st.write("Primary variables: 'popularity', 'release year', 'duration_ms', 'genre', 'loudness'")
st.write("Other variables included: 'danceability', 'energy', 'valence', 'tempo', 'acousticness', 'instrumentalness', 'liveliness', 'speechiness'")

st.header("Limitations")
st.markdown(
    "- **Top 2000 tracks:** these findings only apply to the most popular tracks and can't be generalized to the popularity of all tracks\n"
    "- **1998-2020:** these findings cannot be generalized to all time periods\n"
    "- Since our analysis is based on observational data, we cannot draw conclusions of causal relationships between audio features and popularity\n"
    "- Analysis is limited to coarse 'genre' categories, which may hide intra-category variation"
)

st.header("Future Work")
st.write(
    "With more time and resources, we would've evaluated even more data across a longer time period to get a better understanding "
    "of audio features and popularity throughout history (and before the creation of Spotify). With more historical and recent data, "
    "we would attempt to predict popularity trends based on audio features in the future."
)
