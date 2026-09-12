from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
orders=pd.read_csv(ROOT/'data/raw/orders.csv',parse_dates=['order_date'])
customers=pd.read_csv(ROOT/'data/raw/customers.csv')
df=orders.merge(customers,on='customer_id',how='left')
print('Rows:',len(df))
print('Revenue:',round(df.net_revenue.sum(),2))
print('Orders:',df.order_id.nunique())
print('Customers:',df.customer_id.nunique())
print('Return rate:',round(df.returned.mean(),4))
monthly=(df.assign(month=df.order_date.dt.to_period('M').astype(str))
           .groupby('month',as_index=False)
           .agg(revenue=('net_revenue','sum'),orders=('order_id','nunique'),customers=('customer_id','nunique')))
monthly['aov']=monthly.revenue/monthly.orders
monthly.to_csv(ROOT/'data/processed/monthly_kpis.csv',index=False)
