import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from entsoe import EntsoePandasClient
from entsoe_token import token

# Energy data is obtained from the ENTSOE API
@st.cache
def get_energy_data(country_code):
    load_dotenv()
    client = EntsoePandasClient(api_key=token)
    end = pd.Timestamp.now(tz='Europe/London')
    start = end - pd.DateOffset(months=1)
    df = client.query_generation(country_code, start=start,end=end, psr_type=None)
    #Ensuring the dataframe consists of an hourly frequency,
    df = df.resample('H').mean()
    return df
