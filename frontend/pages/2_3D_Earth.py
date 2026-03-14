import streamlit as st
import plotly.express as px
from backend.data_loader import load_climate_data

st.title("🌎 3D Climate Globe")

climate_df = load_climate_data()

globe_df = climate_df.sample(2500)

fig_globe = px.scatter_geo(
    globe_df,
    lat="lat",
    lon="lon",
    color="air",
    projection="orthographic",
    color_continuous_scale="Turbo"
)

fig_globe.update_geos(
    showcountries=True,
    showcoastlines=True,
    showland=True
)

st.plotly_chart(fig_globe, use_container_width=True)
