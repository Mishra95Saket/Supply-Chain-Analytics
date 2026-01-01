import pandas as pd

df = pd.read_csv('data/raw/raas_synthetic_data.csv')

assert df.isnull().sum().sum() == 0, "Missing values detected"
assert (df['robot_utilization_pct'] <= 100).all()

print("Data validation checks passed.")
