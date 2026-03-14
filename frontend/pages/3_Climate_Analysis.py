import streamlit as st
import plotly.express as px
from backend.data_loader import load_climate_data

st.title("📊 Climate Analysis")

climate_df = load_climate_data()

lat_df = climate_df.groupby("lat")["air"].mean().reset_index()

fig = px.line(
    lat_df,
    x="lat",
    y="air",
    title="Average Temperature by Latitude"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("## Dataset Explorer")

st.dataframe(climate_df.sample(500))
