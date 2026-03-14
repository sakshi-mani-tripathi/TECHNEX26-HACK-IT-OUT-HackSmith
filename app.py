
import streamlit as st
from frontend.dashboard import run_dashboard


st.set_page_config(
    page_title="PyClimaExplorer",
    page_icon="🌍",
    layout="wide"
)


# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "home"


# ---------- LANDING PAGE ----------
if st.session_state.page == "home":

    st.markdown("""
    <style>

    body{
    background-color:#0b0f2a;
    }

    .hero{
    text-align:center;
    padding:120px 20px;
    border-radius:20px;
    background: linear-gradient(120deg,#0f2027,#203a43,#2c5364);
    }

    .title{
    font-size:70px;
    font-weight:800;
    color:white;
    }

    .subtitle{
    font-size:24px;
    color:#cfe9ff;
    margin-top:20px;
    }

    .feature{
    background:#121738;
    padding:25px;
    border-radius:15px;
    text-align:center;
    }

    .feature h3{
    color:#00eaff;
    }

    </style>
    """, unsafe_allow_html=True)


    # ---------- HERO SECTION ----------

    st.markdown("""
    <div class="hero">

    <div class="title">
    🌍 PyClimaExplorer
    </div>

    <div class="subtitle">
    Global Climate Intelligence Platform
    </div>

    <div class="subtitle">
    Analyze atmospheric data, visualize global climate patterns and explore Earth with advanced geospatial tools.
    </div>

    </div>
    """, unsafe_allow_html=True)


    st.write("")
    st.write("")


    # ---------- BUTTON ----------

    c1,c2,c3 = st.columns([1,2,1])

    with c2:
        if st.button("🚀 Launch Climate Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()


    st.write("")
    st.write("")


    # ---------- FEATURES ----------

    st.markdown("## 🌟 Platform Features")

    f1,f2,f3 = st.columns(3)

    with f1:
        st.markdown("""
        ### 🌍 Global Climate Maps
        Explore real atmospheric temperature data across the globe.
        """)

    with f2:
        st.markdown("""
        ### 🌎 Interactive 3D Earth
        Rotate and explore Earth using climate visualization tools.
        """)

    with f3:
        st.markdown("""
        ### 📊 Climate Analytics
        Discover trends, patterns and climate insights.
        """)


    st.write("")
    st.write("")


    # ---------- STATS ----------

    st.markdown("## 📈 Climate Intelligence Highlights")

    s1,s2,s3,s4 = st.columns(4)

    s1.metric("Global Data Points", "100K+")
    s2.metric("Countries Covered", "190+")
    s3.metric("Climate Variables", "Temperature / Wind")
    s4.metric("Interactive Maps", "5+")


    st.write("")
    st.write("")


    # ---------- FOOTER ----------

    st.markdown("""
    ---
    <center>

    🌍 PyClimaExplorer • Climate Intelligence Platform

    </center>
    """, unsafe_allow_html=True)



# ---------- DASHBOARD ----------
elif st.session_state.page == "dashboard":

    run_dashboard()
