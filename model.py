import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
#%%
df = pd.read_csv('fundamentals_data/data.csv', index_col=0)
#%%
def ratio(Series):
    return Series / Series[0]

df = df.apply(ratio, axis=1)
#%%
df2 = df.drop(['GROSS PROFIT', 'TOTAL ASSETS'], axis=1)
df2 = np.log(df2 + 0.000001)
df2['GROSS PROFIT'] = df['GROSS PROFIT']
df = df2
#%%
df.hist(bins=50, figsize=(16, 12))
#%%
df.plot(
        kind="scatter", 
        x="TOTAL ASSETS", 
        y="Cash & Equivalents", 
        alpha=1
    )
#%%
pip = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('std_scaler', StandardScaler()),
    ])
#%%
train_set = pip.fit_transform(df)
#%%
clustering = AgglomerativeClustering(
        n_clusters=10,
        linkage='complete'
    )
#%%
res = clustering.fit_predict(train_set)
np.unique(res, return_counts=True)
#%% Plot results
res = pd.DataFrame({
        'Symbol': df.index,
        'group': res
    })
#%%
res.to_csv('fundamentals_data/new_sectors.csv')
#%%
spy = pd.read_csv('fundamentals_data/spy500.csv')[['Symbol', 'Sector']]
#%%
res = res.merge(spy, on='Symbol')
#%%
table = res.groupby('Sector').nunique()
table.drop('Sector', axis=1, inplace=True)
table.columns = ['Company Numbers', 'New Group Numbers']    








