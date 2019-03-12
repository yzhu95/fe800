import pandas as pd
import numpy as np
#from scipy import stats
#%%
df = pd.read_csv('pd.csv', index_col=0)
df.dropna(axis=1, inplace=True)
columns = [x.split(' ')[0] for x in list(df.columns)]
df.columns = columns

#%% Traditonal Sectors
spx = pd.read_csv('spy500.csv')
spx = spx[spx['Symbol'].isin(df.columns)]
#%%
sectors = spx['Sector'].unique()
sectors = {x: spx[spx['Sector'] == x]['Symbol'].values
           for x in sectors
          }
#%% Calculate Correlation
first = True
for sector in sectors.keys():
    corr = df[sectors[sector]].corr(method='spearman') 
    desc = pd.Series(corr.values[np.triu_indices(
            n = len(corr),
            k = 1
        )]).describe()
    
    if first:
        res = desc.to_frame(sector)
        first = False
    else:
        res[sector] = desc
        
res = res.transpose() 
res2= res.round(2).sort_values('mean', ascending=0)

#%% New Sectors
new = pd.read_csv('new_sectors.csv', index_col=0)
new = new[new['Symbol'].isin(df.columns)]
#%%
sectors = new['group'].unique()
sectors = {x: new[new['group'] == x]['Symbol'].values
           for x in sectors
          }
#%% Repeat Calculate Correlation




