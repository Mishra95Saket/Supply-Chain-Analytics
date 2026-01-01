import pandas as pd

df = pd.read_csv('data/raw/raas_synthetic_data.csv')

sla = df.groupby(['robot_type', 'region']).agg(
    sla_breach_rate=('sla_breach', 'mean'),
    avg_downtime=('downtime_hours', 'mean')
).reset_index()

sla.to_csv('outputs/metrics/sla_performance.csv', index=False)

print("SLA performance analysis completed.")
