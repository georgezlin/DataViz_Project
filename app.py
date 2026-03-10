import streamlit as st

st.set_page_config(page_title="How Do Different Metrics Influence Popularity Over Time?", layout="wide")
st.title("How Do Different Metrics Define Popularity Over Time?")
st.markdown(
    "**Central question:** *In music, how do different metrics influence popularity over time?*"
)

st.write(
    "Popular music changes throughout time periods, and our group is curious what metrics define these changes. "
    "Do certain audio features correlate with music popularity? Do certain metrics define popularity in some genres but not others? "
    "Do these trends vary over time, and if so, how? We want to investigate what metrics make music popular and how it varies across genres and time."
)

st.markdown(
    "**Data Set Description:** *Our dataset explores 2000 of the top hits on Spotify from 1998-2020, including metrics that describe each track and its qualities.*  "
)

st.write(
    "The variables in the data are name of the artist, name of the song, duration of the track (in ms), if the track is explicit, "
    "release year, popularity, song danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, "
    "valence, tempo, genre. The variables we focus on are:"
)

st.markdown(
    "- **Popularity:** on a scale of 1-100, normalized for changes in overall Spotify streaming over time, with 1 being least popular and 100 being most popular\n"
    "- **Release year:** year the track is released\n"
    "- **Duration_ms:** duration of the track in milliseconds\n"
    "- **Genre:** genre of the track\n"
    "- **Loudness:** the overall loudness of a track in decibels (dB), averaged across the entire track. Values typically range between -60 and 0 dB, with -60 being silent and 0 being the maximum threshold of the human ear\n"
    "- **Danceability:** describes how suitable a track is for dancing based on tempo, rhythm stability, beat strength, and overall regularity, with a value of 0.0 being least danceable and 1.0 most danceable\n"
    "- **Energy:** represents perceptual intensity and activity, with 0.0 being least energetic and 1.0 being most energetic\n"
    "- **Speechiness:** detects the presence of spoken words in a track, with 0.0 being less spoken word and 1.0 being the most. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, like rap music. Values below 0.33 most likely represent music and other non-speech-like tracks\n"
    "- **Acousticness:** a measure of confidence on whether a track is acoustic, with 0.0 being least confident and 1.0 being most confident\n"
    "- **Instrumentalness:** a measure predicting if the track has no vocals, with 0.0 being most vocals and 1.0 being least vocals\n"
    "- **Liveness:** detects the presence of an audience in the recording, and higher liveness values represent an increased probability that the track was performed live\n"
    "- **Valence:** measure describing the musical positiveness conveyed by a track, with 0.0 being least positive and 1.0 being most positive\n"
    "- **Tempo:** speed/pace of track in beats per minute"
)

st.write("Dataset: https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019")

st.write("This dataset will allow us to investigate multiple different metrics, how they correlate to popularity, and how this relationship changes over time.")
st.write("Use the sidebar to navigate:")

st.markdown(
    "- **Audio Features & Popularity** — What audio features correlate with popularity?\n"
    "- **Genre Deep Dive** — How does duration vs. popularity differ by genre, and what makes R&B unique?\n"
    "- **Explore** — An interactive dashboard to explore features, genres, and time periods.\n"
    "- **Takeaways** — Conclusions derived from our analysis + Methods/Limitations."
)
