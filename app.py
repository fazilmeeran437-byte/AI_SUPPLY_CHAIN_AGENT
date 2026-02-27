import streamlit as st
import asyncio
from database import create_database, get_data
from lstm_model import train_lstm
from rl_agent import route_optimization
from agents_async import run_agents
from api_service import fetch_weather
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🔥 Ultra AI Supply Chain System")

create_database()
data = get_data()

st.subheader("📦 Current Data")
st.dataframe(data)

# LSTM Forecast
forecast = train_lstm(data)
st.success(f"LSTM Predicted Demand: {forecast}")

# Async Multi-Agent Execution
st.subheader("🤖 Async Multi-Agent Decisions")

for _, row in data.iterrows():
    inv, ship = asyncio.run(run_agents(row, forecast))
    best_route = route_optimization(row["distance_km"], row["fuel_cost"])
    st.write(row["product"])
    st.write("Inventory:", inv)
    st.write("Shipping:", ship)
    st.write("Best Route (RL):", best_route)
    st.write("---")

# Real-Time Auto Refresh
st.button("🔄 Refresh Data")

# Charts
st.subheader("📊 Analytics")
fig, ax = plt.subplots()
ax.plot(data["demand"])
st.pyplot(fig)

# API Weather
st.subheader("🌦 External Weather API")
weather = fetch_weather()
st.json(weather)