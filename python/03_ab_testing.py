from pathlib import Path
import pandas as pd
from scipy.stats import ttest_ind,chi2_contingency
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/raw/orders.csv')
c=df.loc[df.ab_group=='control','net_revenue']; v=df.loc[df.ab_group=='variant','net_revenue']
_,p=ttest_ind(c,v,equal_var=False)
ct=pd.crosstab(df.ab_group,df.returned); _,rp,_,_=chi2_contingency(ct)
print('control mean revenue',round(c.mean(),2))
print('variant mean revenue',round(v.mean(),2))
print('revenue p-value',round(p,5))
print('return-rate p-value',round(rp,5))
