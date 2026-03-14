PyClimaExplorer 🌍
Climate Intelligence & Global Atmospheric Visualization Platform

PyClimaExplorer is an interactive climate analytics dashboard that visualizes global atmospheric data using advanced geospatial visualization, interactive maps, and climate trend analysis.

The platform allows users to explore climate data across time, detect anomalies, and analyze global temperature distribution using interactive visual tools such as maps, 3D globe visualization, and animated climate evolution.

Features
Global Climate Visualization

Interactive global temperature maps built using real atmospheric datasets.

Animated Climate Evolution

Visualize climate changes over time using animated geospatial plots.

Interactive 3D Globe

Explore climate data on a rotatable Earth globe using geographic projections.

Climate Trend Analysis

Analyze weekly temperature and wind trends with interactive charts.

Geographic Climate Mapping

Visualize city-level climate data using geospatial mapping.

Climate Statistics

View global temperature indicators including:

Average temperature

Maximum temperature

Minimum temperature

Dataset size

Dataset Explorer

Interactively explore raw climate dataset samples directly in the dashboard.

Climate Alerts

Detect extreme conditions such as:

Heatwave warnings

Extreme cold alerts

Technologies Used

Python
Streamlit
Plotly
PyDeck
Pandas
Xarray
NetCDF Climate Dataset

Dataset

The project uses atmospheric temperature data stored in NetCDF format:

air.sig995.2012.nc


This dataset contains global atmospheric temperature measurements across:

Latitude

Longitude

Time

The dataset is processed using Xarray and converted to DataFrame format for visualization.

Project Structure
PyClimaExplorer
│
├── app.py
│
├── frontend
│   └── dashboard.py
│
├── backend
│   ├── weather_api.py
│   └── data_loader.py
│
├── assets
│   └── styles.css
│
├── data
│   └── air.sig995.2012.nc
│
└── README.md

Installation

Move into the project directory:

cd PyClimaExplorer


Install required libraries:

pip install -r requirements.txt

Run the Application

Start the Streamlit app:

streamlit run app.py


The dashboard will open in your browser.

Example Dashboard Sections

Global Temperature Distribution

Animated Climate Evolution

Interactive Global Globe

Climate Trend Analysis

Dataset Explorer

Climate Alerts

Future Improvements

Planned enhancements include:

AI-based climate prediction

Satellite Earth visualization

Climate anomaly detection models

Multi-year climate comparison

Advanced WebGL Earth visualization

Author

Mahima Prajapati
Climate Data Visualization Project

License

This project is open-source and available for educational and research purposes.

If you want, I can also help you add one more section that impresses judges a lot:

Project screenshots

Live demo GIF

architecture diagram

Those make the README look much more professional.
