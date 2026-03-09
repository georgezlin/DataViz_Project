import altair as alt
import pandas as pd


def base_theme():
    return {
        "config": {
            "view": {"stroke": None},
            "axis": {"labelFontSize": 12, "titleFontSize": 14},
            "legend": {"labelFontSize": 12, "titleFontSize": 14},
        }
    }


def chart_feature_correlation(df: pd.DataFrame) -> alt.Chart:
    features = ['danceability', 'energy', 'loudness', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

    corr_rows = []
    for f in features:
        r = df['popularity'].corr(df[f])
        corr_rows.append({'feature': f, 'correlation': round(r, 3)})

    corr_df = pd.DataFrame(corr_rows)

    return alt.Chart(corr_df).mark_bar().encode(
        x=alt.X('correlation:Q', scale=alt.Scale(domain=[-0.3, 0.3]),
                 title='Correlation with Popularity'),
        y=alt.Y('feature:N', sort=alt.EncodingSortField(field='correlation', order='descending'),
                 title=None),
        color=alt.Color('correlation:Q',
                        scale=alt.Scale(scheme='redblue', domain=[-0.3, 0.3]),
                        legend=None),
        tooltip=['feature', 'correlation']
    ).properties(
        title='Which Audio Features Correlate with Popularity?',
        width=500,
        height=350
    )


def chart_duration_by_genre(df: pd.DataFrame) -> alt.LayerChart:
    df_genre = df.dropna(subset=['primary_genre'])

    points = alt.Chart(df_genre).mark_circle(size=30, opacity=0.35).encode(
        x=alt.X('duration_min:Q', title='Duration (minutes)', scale=alt.Scale(domain=[1.5, 7])),
        y=alt.Y('popularity:Q', title='Popularity'),
        color=alt.Color('primary_genre:N', title='Genre'),
        tooltip=['artist:N', 'song:N', 'year:Q', 'popularity:Q',
                 alt.Tooltip('duration_min:Q', format='.1f', title='Duration (min)'),
                 'primary_genre:N']
    )

    trend = alt.Chart(df_genre).mark_line(size=3).encode(
        x=alt.X('duration_min:Q'),
        y=alt.Y('popularity:Q'),
        color=alt.Color('primary_genre:N', title='Genre')
    ).transform_regression(
        'duration_min', 'popularity', groupby=['primary_genre']
    )

    return (points + trend).properties(
        title='Duration vs. Popularity by Genre',
        width=600,
        height=450
    )


def chart_rnb_vs_all(df: pd.DataFrame) -> alt.Chart:
    df_rnb = df[df['genre'].str.contains('R&B', na=False)]

    features = ['danceability', 'energy', 'loudness', 'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']

    corr_rows = []
    for f in features:
        corr_rows.append({
            'feature': f,
            'R&B': round(df_rnb['popularity'].corr(df_rnb[f]), 3),
            'All Songs': round(df['popularity'].corr(df[f]), 3)
        })

    corr_compare = pd.DataFrame(corr_rows).melt(
        id_vars='feature', var_name='group', value_name='correlation'
    )

    return alt.Chart(corr_compare).mark_bar().encode(
        x=alt.X('correlation:Q', title='Correlation with Popularity',
                 scale=alt.Scale(domain=[-0.1, 0.1])),
        y=alt.Y('feature:N',
                 sort=alt.EncodingSortField(field='correlation', order='descending'),
                 title=None),
        color=alt.Color('group:N', title='Group',
                        scale=alt.Scale(domain=['R&B', 'All Songs'],
                                        range=['#e45756', 'steelblue'])),
        xOffset='group:N',
        tooltip=['feature:N', 'group:N', alt.Tooltip('correlation:Q', format='+.3f')]
    ).properties(
        title='What Predicts Popularity in R&B vs. All Songs?',
        width=500,
        height=400
    )


def chart_interactive_explorer(df: pd.DataFrame) -> alt.VConcatChart:
    genre_options = ['All'] + sorted(df['primary_genre'].dropna().unique().tolist())
    genre_dropdown = alt.binding_select(options=genre_options, name='Genre: ')
    genre_param = alt.param(name='genre_select', value='All', bind=genre_dropdown)

    feature_list = ['loudness', 'danceability', 'energy', 'speechiness',
                    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
    feature_dropdown = alt.binding_select(options=feature_list, name='Feature: ')
    feature_param = alt.param(name='feature_select', value='loudness', bind=feature_dropdown)

    brush = alt.selection_interval(encodings=['x'])

    base = alt.Chart(df).transform_calculate(
        match_genre="datum.primary_genre === null ? 'Other' : datum.primary_genre"
    ).transform_filter(
        "(genre_select === 'All') || (datum.match_genre === genre_select)"
    ).transform_fold(
        feature_list,
        as_=['feature_name', 'feature_value']
    ).transform_filter(
        "datum.feature_name === feature_select"
    )

    yearly_trend = base.mark_line(point=True, color='steelblue').encode(
        x=alt.X('year:O', title='Year'),
        y=alt.Y('mean(feature_value):Q', title='Average Value',
                 scale=alt.Scale(zero=False)),
        tooltip=[alt.Tooltip('year:O'),
                 alt.Tooltip('mean(feature_value):Q', format='.2f')]
    ).properties(
        width=650,
        height=120,
        title='Average Feature by Year (brush to filter scatter below)'
    ).add_params(brush, genre_param, feature_param)

    scatter = base.mark_circle(size=35).encode(
        x=alt.X('feature_value:Q', title='Feature Value'),
        y=alt.Y('popularity:Q', title='Popularity'),
        color=alt.condition(
            brush,
            alt.Color('year:O', scale=alt.Scale(scheme='viridis'), legend=None),
            alt.value('lightgray')
        ),
        opacity=alt.condition(brush, alt.value(0.7), alt.value(0.05)),
        tooltip=['artist:N', 'song:N', 'year:O', 'popularity:Q',
                 alt.Tooltip('feature_value:Q', format='.2f'),
                 'match_genre:N']
    ).properties(
        width=650,
        height=400,
        title='Feature vs. Popularity'
    )

    trend = base.mark_line(color='red', size=3).transform_filter(
        brush
    ).transform_regression(
        'feature_value', 'popularity'
    ).encode(
        x='feature_value:Q',
        y='popularity:Q'
    )

    return alt.vconcat(yearly_trend, scatter + trend).properties(spacing=5)
