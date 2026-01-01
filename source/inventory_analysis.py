import pandas as pd
import yaml
from scipy.stats import norm

with open("config.yaml") as f:
    config = yaml.safe_load(f)

df = pd.read_csv('data/raw/raas_synthetic_data.csv')

inventory = df.groupby(['robot_type', 'region']).agg(
    avg_monthly_demand=('monthly_units_committed', 'mean'),
    demand_std=('monthly_units_committed', 'std'),
    avg_lead_time=('robot_lead_time_days', 'mean')
).reset_index()

z = norm.ppf(config['inventory']['service_level'])

inventory['safety_stock'] = z * inventory['demand_std'] * (inventory['avg_lead_time'] / 30) ** 0.5
inventory['reorder_point'] = inventory['avg_monthly_demand'] * (inventory['avg_lead_time'] / 30) + inventory['safety_stock']

inventory.to_csv('outputs/metrics/inventory_policy.csv', index=False)

print("Inventory policy calculated.")
