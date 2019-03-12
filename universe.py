import pandas as pd
import numpy as np
#%%
df = pd.read_csv('spy500.csv')
#%%
df.sort_values('Sector', inplace=True)
#%%
df['Sector'].unique()
#%%
df['Symbol'].to_csv(
        'download_list.txt',
        sep='\n',
        header=False,
        index=False
    )
#%% Select Universe
import get_data as gd
#%%
def select_universe(year):
    features = [
            'TOTAL ASSETS', 
            'Cash & Equivalents',
            'Receivables - Total (Net)',
            'Inventories - Total',
            'Sales (Net)',
            'Cost of Good Sold',
            'GROSS PROFIT'
        ]
    
    data = gd.get_data(year, features)
    data.dropna(axis=0, inplace=True)
    df_new = df[df['Symbol'].isin(data.index)]
    
    return df_new
#%%
years = np.arange(2010, 2019)
for year in years:
    df = select_universe(year)
#%%
df['Symbol'].to_csv('universe.csv', index=False)





  