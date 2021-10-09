import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from entsoe import EntsoePandasClient
from entsoe.mappings import TIMEZONE_MAPPINGS
import os

# Energy data is obtained from the ENTSOE API
@st.cache
def get_energy_data(country_code):
    load_dotenv()
    api_key = os.environ.get("token")
    client = EntsoePandasClient(api_key='c44339b3-0286-4fc4-b135-680770596714')
    #end = pd.Timestamp.now(tz='Europe/London')
    end = pd.Timestamp.now(tz=TIMEZONE_MAPPINGS[country_code])
    start = end - pd.DateOffset(months=1)
    df = client.query_generation(country_code, start=start, end=end, psr_type=None)
    #Ensuring the dataframe consists of an hourly frequency
    df = df.resample('H').mean()
    return df
