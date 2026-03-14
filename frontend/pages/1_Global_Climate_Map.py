import streamlit as st
import plotly.express as px
from backend.data_loader import load_climate_data

st.title("🌍 Global Climate Map")

climate_df = load_climate_data()

sample_df = climate_df.sample(2000)

fig = px.scatter_mapbox(
    sample_df,
    lat="lat",
    lon="lon",
    color="air",
    size="air",
    zoom=1,
    color_continuous_scale="Turbo"
)

fig.update_layout(mapbox_style="open-street-map")

st.plotly_chart(fig, use_container_width=True)
