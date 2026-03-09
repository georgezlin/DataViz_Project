import streamlit as st
import pandas as pd


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/spotify_top_hits.csv")
    df['duration_min'] = df['duration_ms'] / 60000

    top_genres = ['pop', 'hip hop', 'rock', 'R&B', 'Dance/Electronic']

    def get_primary_genre(genre_str):
        for g in top_genres:
            if g in str(genre_str):
                return g
        return None

    df['primary_genre'] = df['genre'].apply(get_primary_genre)
    return df
