import streamlit as st
import plotly.express as px
import pandas as pd
import pydeck as pdk

from backend.weather_api import get_weather
from backend.data_loader import load_climate_data


def run_dashboard():

    # ---------------- HERO SECTION ----------------
    st.markdown(
        """
        <div style="
        padding:30px;
        border-radius:15px;
        background: linear-gradient(90deg,#0f2027,#203a43,#2c5364);
        text-align:center;
        margin-bottom:20px;
        ">
        <h1 style="color:white;">🌍 Global Climate Intelligence Platform</h1>
        <p style="color:#d0e7ff;font-size:18px;">
        Analyze atmospheric data, climate anomalies, risk zones and explore Earth using interactive visualizations.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- HEADER ----------------
    st.markdown(
        """
        <h1 style='text-align:center;'>🌍 PyClimaExplorer</h1>
        <h3 style='text-align:center;color:#00eaff;'>Climate Intelligence Dashboard</h3>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ---------------- SIDEBAR ----------------
    st.sidebar.header("Dashboard Controls")

    city = st.sidebar.selectbox(
        "Select City",
        ["Varanasi", "Delhi", "Mumbai"]
    )

    st.sidebar.markdown("### Comparison Mode")

    dataset_a = st.sidebar.selectbox(
        "Dataset A",
        ["1990", "2000", "2010"]
    )

    dataset_b = st.sidebar.selectbox(
        "Dataset B",
        ["2015", "2020", "2023"]
    )

    story_mode = st.sidebar.checkbox("Enable Story Mode")

    # ---------------- WEATHER DATA ----------------
    weather = get_weather(city)

    # ---------------- WEATHER METRICS ----------------
    st.markdown("## 🌤 Current Weather")

    c1, c2, c3 = st.columns(3)

    c1.metric("Temperature", f"{weather['temperature']} °C")
    c2.metric("Wind Speed", f"{weather['windspeed']} km/h")
    c3.metric("Weather Code", weather["weathercode"])

    st.markdown("---")

    # ---------------- CLIMATE CHARTS ----------------
    st.markdown("## 📊 Climate Trend Analysis")

    data = {
        "Day": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "Temperature": [27,28,30,29,31,32,30],
        "Wind": [8,10,9,11,13,12,10]
    }

    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)

    with col1:
        fig_temp = px.line(df, x="Day", y="Temperature", markers=True)
        st.plotly_chart(fig_temp, use_container_width=True, key="temp_chart")

    with col2:
        fig_wind = px.bar(df, x="Day", y="Wind")
        st.plotly_chart(fig_wind, use_container_width=True, key="wind_chart")

    st.markdown("---")

    # ---------------- LOAD CLIMATE DATA ----------------
    climate_df = load_climate_data()

    # ---------------- TIME FILTER ----------------
    st.sidebar.markdown("### Climate Filters")

    time_values = climate_df["time"].unique()

    selected_time = st.sidebar.selectbox("Select Time", time_values)

    filtered_df = climate_df[climate_df["time"] == selected_time]

    # ---------------- GLOBAL TEMPERATURE MAP ----------------
    st.markdown("## 🌍 Global Temperature Distribution")

    sample_df = filtered_df.sample(2000)

    fig_global = px.scatter_mapbox(
        sample_df,
        lat="lat",
        lon="lon",
        color="air",
        size="air",
        zoom=1,
        height=600,
        color_continuous_scale="Turbo"
    )

    fig_global.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig_global, use_container_width=True, key="global_map")

    # ---------------- ANIMATED CLIMATE EVOLUTION ----------------
    st.markdown("---")
    st.markdown("## ⏳ Animated Climate Evolution")

    anim_df = climate_df.sample(4000)

    fig_anim = px.scatter_mapbox(
        anim_df,
        lat="lat",
        lon="lon",
        color="air",
        size="air",
        animation_frame="time",
        zoom=1,
        height=600,
        color_continuous_scale="Turbo"
    )

    fig_anim.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig_anim, use_container_width=True, key="animated_map")

    # ---------------- ROTATABLE GLOBE ----------------
    st.markdown("---")
    st.markdown("## 🌍 Interactive Global Climate Globe")

    globe_df = climate_df.sample(2500)

    fig_globe = px.scatter_geo(
        globe_df,
        lat="lat",
        lon="lon",
        color="air",
        projection="orthographic",
        color_continuous_scale="Turbo"
    )

    fig_globe.update_geos(showcountries=True, showcoastlines=True)

    st.plotly_chart(fig_globe, use_container_width=True, key="globe_chart")

    # ---------------- GEOGRAPHIC MAP ----------------
    st.markdown("---")
    st.markdown("## 🌍 Geographic Climate Map")

    map_data = pd.DataFrame({
        "city": ["Varanasi","Delhi","Mumbai"],
        "lat": [25.3176,28.6139,19.0760],
        "lon": [82.9739,77.2090,72.8777],
        "temperature": [30,32,29]
    })

    fig_map = px.scatter_mapbox(
        map_data,
        lat="lat",
        lon="lon",
        size="temperature",
        color="temperature",
        zoom=3
    )

    fig_map.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig_map, use_container_width=True, key="geo_map")

    # ---------------- CLIMATE STATISTICS ----------------
    st.markdown("---")
    st.markdown("## 📊 Climate Statistics")

    avg_temp = climate_df["air"].mean()
    max_temp = climate_df["air"].max()
    min_temp = climate_df["air"].min()

    c1, c2, c3 = st.columns(3)

    c1.metric("Average Temperature", f"{avg_temp:.2f}")
    c2.metric("Max Temperature", f"{max_temp:.2f}")
    c3.metric("Min Temperature", f"{min_temp:.2f}")

    # ---------------- DATASET EXPLORER ----------------
    st.markdown("---")
    st.markdown("## 🔎 Climate Dataset Explorer")

    st.dataframe(climate_df.sample(500))

    # ---------------- DATASET COMPARISON ----------------
    st.markdown("---")
    st.markdown("## 📊 Dataset Comparison")

    colA, colB = st.columns(2)

    with colA:
        st.subheader(dataset_a)
        st.plotly_chart(fig_temp, use_container_width=True, key="compare_chart_a")

    with colB:
        st.subheader(dataset_b)
        st.plotly_chart(fig_temp, use_container_width=True, key="compare_chart_b")

    # ---------------- CLIMATE ALERTS ----------------
    st.markdown("---")
    st.markdown("## ⚠ Climate Alerts")

    if weather["temperature"] > 35:
        st.error("🔥 Heatwave Warning Detected")
    elif weather["temperature"] < 5:
        st.warning("❄ Extreme Cold Conditions")
    else:
        st.success("🌤 Weather Conditions Normal")

    # ---------------- INSIGHTS ----------------
    st.markdown("---")
    st.markdown("## 🔍 Climate Insights")

    st.write(f"""
    • Current temperature in **{city}** is **{weather['temperature']}°C**

    • Wind speed recorded: **{weather['windspeed']} km/h**

    • Weather condition code: **{weather['weathercode']}**
    """)

    if story_mode:
        st.success("Temperature trend shows gradual warming.")

    # ---------------- FOOTER ----------------
    st.markdown("""
    ---
    <center>
    🌍 Climate Intelligence Platform • Built with Streamlit
    </center>
    """, unsafe_allow_html=True)
