import pandas as pd
import numpy as np

np.random.seed(42)

n_records = 12000

robot_types = ['AMR', 'PickerBot', 'SorterBot']
regions = ['US-East', 'US-West', 'EU', 'APAC']
industries = ['E-commerce', 'Manufacturing', 'Retail', '3PL']

data = {
    'contract_id': np.arange(1, n_records + 1),
    'robot_type': np.random.choice(robot_types, n_records),
    'region': np.random.choice(regions, n_records),
    'industry': np.random.choice(industries, n_records),
    'contract_start_date': pd.date_range('2021-01-01', periods=n_records, freq='D'),
    'monthly_units_committed': np.random.randint(5, 120, n_records),
    'robot_lead_time_days': np.random.randint(30, 120, n_records),
    'spare_parts_lead_time_days': np.random.randint(10, 45, n_records),
    'robot_utilization_pct': np.random.uniform(55, 98, n_records),
    'downtime_hours': np.random.exponential(scale=4, size=n_records),
    'sla_threshold_hours': 8,
    'monthly_revenue_usd': np.random.randint(15000, 250000, n_records),
    'spare_parts_cost_usd': np.random.randint(500, 8000, n_records)
}

df = pd.DataFrame(data)
df['sla_breach'] = df['downtime_hours'] > df['sla_threshold_hours']

df.to_csv('data/raw/raas_synthetic_data.csv', index=False)

print("Synthetic RaaS supply chain dataset generated.")
