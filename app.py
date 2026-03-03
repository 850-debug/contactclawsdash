import streamlit as st
import pandas as pd
from filters import apply_filters
from config import INDUSTRIES, PROVINCES

st.set_page_config(layout="wide")

st.title("🇨🇦 CCC Hybrid B2B Directory Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/companies.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")

industry = st.sidebar.selectbox(
    "Industry",
    ["All"] + INDUSTRIES
)

province = st.sidebar.selectbox(
    "Province",
    ["All"] + PROVINCES
)

keyword = st.sidebar.text_input("Keyword Search")

filtered = df.copy()

if industry != "All":
    filtered = apply_filters(filtered, industry, None, None)

if province != "All":
    filtered = apply_filters(filtered, None, province, None)

if keyword:
    filtered = apply_filters(filtered, None, None, keyword)

st.metric("Companies Found", len(filtered))

st.dataframe(filtered, use_container_width=True)

csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    "⬇ Export CSV",
    csv,
    "ccc_companies.csv",
    "text/csv"
)