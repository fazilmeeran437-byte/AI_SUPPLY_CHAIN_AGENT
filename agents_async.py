import asyncio

async def inventory_agent(row, forecast):
    await asyncio.sleep(0.1)
    if row["inventory"] < forecast:
        return "Reorder"
    return "Inventory OK"

async def shipping_agent(row):
    await asyncio.sleep(0.1)
    if row["distance_km"] > 600:
        return "Optimize Route"
    return "Route OK"

async def run_agents(row, forecast):
    inv = await inventory_agent(row, forecast)
    ship = await shipping_agent(row)
    return inv, ship