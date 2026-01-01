import pandas as pd

df = pd.read_csv('data/raw/raas_synthetic_data.csv')

util = df.groupby('robot_type').agg(
    avg_utilization=('robot_utilization_pct', 'mean'),
    revenue=('monthly_revenue_usd', 'sum')
).reset_index()

util['underutilized_flag'] = util['avg_utilization'] < 70

util.to_csv('outputs/metrics/utilization_summary.csv', index=False)

print("Utilization analysis completed.")
