
import xarray as xr
import pandas as pd


def load_climate_data():

    dataset = xr.open_dataset("data/air.sig995.2012.nc")

    df = dataset["air"].to_dataframe().reset_index()

    df = df.dropna()

    return df