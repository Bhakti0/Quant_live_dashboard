
This is a **real-time quantitative analytics dashboard** using Binance WebSocket tick data.
It demonstrates:
Live data ingestion
Resampling (1s / 1m / 5m)
Spread, Z-score, correlation
Simple alerting
Interactive visualization

Backend + Frontend is implemented using **Python + Streamlit**.



Python 3.9+
Streamlit (Frontend)
Binance WebSocket (Data source)
Pandas / NumPy / Statsmodels
SQLite (local storage)



pip install -r requirements.txt
streamlit run app.py


Open browser at: http://localhost:8501



Live price chart
Spread & Z-score
Rolling correlation
OLS hedge ratio
Z-score alerts
CSV export

WebSocket → Ingestion → SQLite → Analytics Engine → Streamlit UI

