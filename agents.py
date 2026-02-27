def inventory_agent(row, predicted_demand):
    if row["inventory"] < predicted_demand:
        return "⚠️ Reorder Stock"
    elif row["inventory"] > predicted_demand * 1.5:
        return "📦 Reduce Stock"
    else:
        return "✅ Inventory OK"

def shipping_agent(row):
    if row["delivery_days"] > 7:
        return "🚚 Optimize Transport"
    elif row["shipping_cost"] > 700:
        return "💰 Reduce Shipping Cost"
    else:
        return "✅ Shipping OK"

def supplier_agent(row):
    if row["supplier_rating"] < 3:
        return "❌ Replace Supplier"
    else:
        return "✅ Supplier Good"