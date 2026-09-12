from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/raw/orders.csv',parse_dates=['order_date'])
snapshot=df.order_date.max()+pd.Timedelta(days=1)
rfm=df.groupby('customer_id').agg(recency=('order_date',lambda x:(snapshot-x.max()).days),frequency=('order_id','nunique'),monetary=('net_revenue','sum')).reset_index()
rfm['r_score']=pd.qcut(rfm.recency.rank(method='first'),5,labels=[5,4,3,2,1]).astype(int)
rfm['f_score']=pd.qcut(rfm.frequency.rank(method='first'),5,labels=[1,2,3,4,5]).astype(int)
rfm['m_score']=pd.qcut(rfm.monetary.rank(method='first'),5,labels=[1,2,3,4,5]).astype(int)
def seg(r):
    if r.r_score>=4 and r.f_score>=4:return 'Champions'
    if r.r_score>=3 and r.f_score>=3:return 'Loyal'
    if r.r_score<=2 and r.f_score>=3:return 'At Risk'
    if r.r_score>=4 and r.f_score<=2:return 'New / Promising'
    return 'Regular'
rfm['segment']=rfm.apply(seg,axis=1)
rfm.to_csv(ROOT/'data/processed/rfm_segments.csv',index=False)
print(rfm.segment.value_counts())
