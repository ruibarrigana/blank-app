import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 Rui's streamlit app")

"""
Here's our first attempt at using data to create a table:
"""

# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    spreadsheet="comprovativo (2)",
    worksheet="comprovativo (2)",
    ttl="10m",
    usecols=range(7),
    nrows=4,
)

# Print results.
st.dataframe(df)