import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from entsoe import EntsoePandasClient
import os

# Energy data is obtained from the ENTSOE API
@st.cache
def get_energy_data(country_code):
    load_dotenv()
    api_key = os.environ["token"]
    client = EntsoePandasClient(api_key=api_key)
    end = pd.Timestamp.now(tz='Europe/London')
    start = end - pd.DateOffset(months=1)
    df = client.query_generation(country_code, start=start, end=end, psr_type=None)
    #Ensuring the dataframe consists of an hourly frequency
    df = df.resample('H').mean()
    return df
