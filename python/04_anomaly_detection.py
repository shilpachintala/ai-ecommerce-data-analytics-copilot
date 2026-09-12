from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/processed/daily_kpis.csv',parse_dates=['order_date'])
df['rolling_7d_revenue']=df.revenue.rolling(7,min_periods=1).mean()
df['rolling_30d_revenue']=df.revenue.rolling(30,min_periods=1).mean()
model=IsolationForest(contamination=.03,random_state=42)
df['anomaly_flag']=model.fit_predict(df[['revenue','orders','return_rate']])
df['is_anomaly']=(df.anomaly_flag==-1).astype(int)
df.to_csv(ROOT/'data/processed/daily_kpis_with_anomalies.csv',index=False)
print('anomaly days',int(df.is_anomaly.sum()))
