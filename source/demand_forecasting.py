import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

df = pd.read_csv('data/raw/raas_synthetic_data.csv')
df['month'] = pd.to_datetime(df['contract_start_date']).dt.to_period('M')

monthly_demand = df.groupby('month')['monthly_units_committed'].sum().to_timestamp()

model = SARIMAX(monthly_demand, order=(1,1,1))
results = model.fit(disp=False)

forecast = results.forecast(6)
forecast.to_csv('outputs/metrics/6_month_demand_forecast.csv')

print("Demand forecast generated.")
