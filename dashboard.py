import os
import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from config.settings import EVENT_LOG
from config.settings import ALERT_LOG
from config.settings import AUTO_REFRESH

st.set_page_config(
    page_title="Ransomware Defense Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Ransomware Defense Dashboard")

st.caption("Real-Time Monitoring and Detection System")

st_autorefresh(interval=AUTO_REFRESH, key="refresh")

# ---------------------------------------
# Read Event Log
# ---------------------------------------

def read_log(path):

    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


events = read_log(EVENT_LOG)
alerts = read_log(ALERT_LOG)

# ---------------------------------------
# Metrics
# ---------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "📂 Total Events",
    len(events)
)

col2.metric(
    "🚨 Alerts",
    len(alerts)
)

col3.metric(
    "🟢 System Status",
    "Running"
)

st.divider()

# ---------------------------------------
# Recent Events
# ---------------------------------------

st.subheader("Recent File Events")

if events:

    df = pd.DataFrame(
        {"Event": events[::-1]}
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=350
    )

else:

    st.info("No events recorded yet.")

# ---------------------------------------
# Alerts
# ---------------------------------------

st.subheader("Detection Alerts")

if alerts:

    for alert in reversed(alerts):

        st.error(alert)

else:

    st.success("No ransomware activity detected.")

st.divider()

st.caption("Final Year Project - Resilient Low-Cost Ransomware Defense System")