
import streamlit as st
import pandas as pd
import sqlite3
import time
from ingest import start_ws
from analytics import compute_analytics
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📈 Quant Live Analytics Dashboard")

symbol = st.selectbox("Symbol", ["btcusdt", "ethusdt"])
start_ws(symbol)

conn = sqlite3.connect("ticks.db", check_same_thread=False)

placeholder = st.empty()

alert_z = st.slider("Z-Score Alert Threshold", 0.5, 3.0, 2.0)

while True:
    df = pd.read_sql("SELECT * FROM ticks ORDER BY timestamp DESC LIMIT 300", conn)
    if len(df) < 10:
        time.sleep(1)
        continue

    df = df.sort_values("timestamp")
    mean, std, z = compute_analytics(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Mean Price", round(mean, 2))
    col2.metric("Std Dev", round(std, 2))
    col3.metric("Z-Score", round(z, 2))

    if abs(z) > alert_z:
        st.error(f"⚠ ALERT: Z-Score {round(z,2)}")

    fig = px.line(df, x="timestamp", y="price", title="Live Price")
    st.plotly_chart(fig, use_container_width=True)

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "ticks.csv"
    )

    time.sleep(2)
