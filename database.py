from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///supply_chain.db")

def create_database():
    data = pd.DataFrame({
        "product": ["Laptop", "Mobile", "Tablet", "Camera"],
        "inventory": [50, 300, 40, 180],
        "demand": [120, 200, 60, 90],
        "distance_km": [800, 200, 650, 400],
        "fuel_cost": [1000, 300, 900, 500]
    })
    data.to_sql("supply_data", engine, if_exists="replace", index=False)

def get_data():
    return pd.read_sql("supply_data", engine)